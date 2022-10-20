import os
import sys
import logging
from termcolor import colored
import functools
import atexit


# cache the opened file object, so that different calls to `setup_logger`
# with the same file name can safely write to the same file.
@functools.lru_cache(maxsize=None)
def _cached_log_stream(filename):
    # use 1K buffer if writing to cloud storage
    # io = PathManager.open(filename, "a", buffering=1024 if "://" in filename else -1)
    io = open(filename, "a")
    atexit.register(io.close)
    return io



class _ColorfulFormatter(logging.Formatter):
  def __init__(self, *args, **kwargs):
    self._root_name = kwargs.pop("root_name") + "."
    self._abbrev_name = kwargs.pop("abbrev_name", "")
    if len(self._abbrev_name):
      self._abbrev_name = self._abbrev_name + "."
    super(_ColorfulFormatter, self).__init__(*args, **kwargs)

  def formatMessage(self, record):
    record.name = record.name.replace(self._root_name, self._abbrev_name)
    log = super(_ColorfulFormatter, self).formatMessage(record)
    if record.levelno == logging.WARNING:
      prefix = colored("WARNING", "red", attrs=["blink"])
    elif record.levelno == logging.ERROR or record.levelno == logging.CRITICAL:
      prefix = colored("ERROR", "red", attrs=["blink", "underline"])
    else:
      return log
    return prefix + " " + log


def setup_logger(
      output=None,
      distributed_rank=0,
      *,
      color=True,
      name="fvcore",
      abbrev_name=None
):
  """
  Initialize the fvcore logger and set its verbosity level to "DEBUG".

  Args:
      output (str): a file name or a directory to save log. If None, will not save log file.
          If ends with ".txt" or ".log", assumed to be a file name.
          Otherwise, logs will be saved to `output/log.txt`.
      name (str): the root module name of this logger
      abbrev_name (str): an abbreviation of the module, to avoid long names in logs.
          Set to "" to not log the root module in logs.

  Returns:
      logging.Logger: a logger
  """
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  logger.propagate = False

  if abbrev_name is None:
    abbrev_name = name

  plain_formatter = logging.Formatter(
    "[%(asctime)s] %(name)s %(levelname)s: %(message)s", datefmt="%m/%d %H:%M:%S"
  )
  # stdout logging: master only
  if distributed_rank == 0:
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    if color:
      formatter = _ColorfulFormatter(
        colored("[%(asctime)s %(name)s]: ", "green") + "%(message)s",
        datefmt="%m/%d %H:%M:%S",
        root_name=name,
        abbrev_name=str(abbrev_name),
      )
    else:
      formatter = plain_formatter
    ch.setFormatter(formatter)
    logger.addHandler(ch)

  # file logging: all workers
  if output:
    if output.endswith(".txt") or output.endswith(".log"):
      filename = output
    else:
      filename = os.path.join(output, "log.txt")
    if distributed_rank > 0:
      filename = filename + ".rank{}".format(distributed_rank)
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    fh = logging.StreamHandler(_cached_log_stream(filename))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(plain_formatter)
    logger.addHandler(fh)

  return logger
