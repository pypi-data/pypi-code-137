import argparse
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)

if True:
    from alphafed import logger
    from alphafed.examples.fed_avg import DATA_OWNER_3_ID
    from alphafed.examples.fed_avg.demos import (DP, FED_IRM, SECURE, SGD,
                                                 VANILLA, get_scheduler,
                                                 get_task_id)

parser = argparse.ArgumentParser(description='Run data owner 3 demo.')
parser.add_argument('-m', '--mode',
                    type=str,
                    default=VANILLA,
                    help=f'running mode: {VANILLA}(default) | {SGD} | {DP} | {SECURE} | {FED_IRM}')
args = parser.parse_args()

task_id = get_task_id()
scheduler = get_scheduler(mode=args.mode)
logger.debug(f'{type(scheduler)=}')
scheduler._setup_context(id=DATA_OWNER_3_ID, task_id=task_id)
scheduler.data_channel._ports = [i for i in range(21000, 21010)]
logger.info(f'run data owner 3 in {args.mode} mode: {task_id=}')
scheduler._launch_process()
