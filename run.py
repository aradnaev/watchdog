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
    check_counter = 0
    restart_counter = 0
    up_counter = 0
    while True:
        check = p.poll()
        check_counter += 1
        if check is not None:
            restart_counter += 1
            logging.warning('Process is terminated. Restart #{}. Last Uptime(h): {}'.format(
                restart_counter, up_counter * monitor_period_s / (3600 * 24))
            p = start_subprocess(command_line)
            up_counter = 0
        else:
            up_counter += 1
            logging.info('Process is alive. poll returned: "{}"'.format(check))
            logging.info('Sleeping for {} seconds. Check counter: {}, restart counter: {}, upttime: {}'.format(
            monitor_period_s, check_counter, restart_counter, up_counter * monitor_period_s / (3600 * 24)))
        sleep(monitor_period_s)


if __name__ == '__main__':
    fire.Fire(main)
