import fire
import subprocess
import logging
import shlex
from time import sleep
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def start_subprocess(command_line):
    logging.info('Executing command_line: {}'.format(
        command_line))
    args = shlex.split(command_line)
    p = subprocess.Popen(args)
    return p


def main(command_line, monitor_period_s=10):
    logging.info('Started watchdog with command line: {}. Monitor period (s): {}'.format(
        command_line, monitor_period_s))
    p = start_subprocess(command_line)
    while True:
        check = p.poll()
        if check is not None:
            logging.warning('Process is terminated. Restarting.')
            p = start_subprocess(command_line)
        else:
            logging.info('Process is alive. poll returned: "{}"'.format(check))
        logging.info('Sleeping for {} seconds.'.format(monitor_period_s))
        sleep(monitor_period_s)


if __name__ == '__main__':
    fire.Fire(main)
