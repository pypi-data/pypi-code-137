import sys
import argparse

from concurrent.futures import ThreadPoolExecutor

from powerful_pipes import report_exception, write_json_to_stdout

from .config import RunningConfig
from .brokers import connect_bus, BusInterface

def run_queue(queue: str, config: RunningConfig):

    connection: BusInterface = connect_bus(config.bus_connection)

    for message in connection.read_json_messages(queue):

        try:
            write_json_to_stdout(message, force_flush=True)

        except Exception as e:
            report_exception({}, e)

def run(config: RunningConfig):

    with ThreadPoolExecutor(max_workers=len(config.queue_name)) as executor:

        for queue in config.queue_name:
            executor.submit(run_queue, queue, config)

        # Wait for tasks
        executor.shutdown(wait=True)

def main():
    banner = 'Powerful Pipes WatchBus tool'

    parser = argparse.ArgumentParser(
        description=banner
    )
    parser.add_argument('-b', '--banner',
                        default=False,
                        action="store_true",
                        help="displays tool banner")
    parser.add_argument('--debug',
                        default=False,
                        action="store_true",
                        help="enable debug mode")
    parser.add_argument('-c', '--bus-connection',
                        default="redis://",
                        required=True,
                        help="bus connections. Default: 'Redis://'")

    parser.add_argument('-q', '--queue-name',
                        action='append',
                        help="bus name where listen to")

    parsed = parser.parse_args()

    config = RunningConfig.from_cli(parsed)

    if config.banner:
        print(f"[*] Starting {banner}", flush=True, file=sys.stderr)

    # Check Redis connection
    try:
        _con = connect_bus(config.bus_connection)
        del _con
    except Exception as e:
        print(e)
        exit(1)

    else:
        run(config)


if __name__ == '__main__':
    main()
