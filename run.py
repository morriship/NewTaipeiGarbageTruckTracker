#!/usr/bin/python3

import time
import subprocess

import argparse

from rubbish_truck import get_rubbish_trucks


QUERY_INTERVAL_SEC = 2 * 60


def run(args):
    rubbish_trucks = get_rubbish_trucks()
    for rubbish_truck in rubbish_trucks:
        if rubbish_truck.line_id == args.line_id:
            print(rubbish_truck)
            if args.street is not None and rubbish_truck.on_street(args.street):
                notify()


def notify():
    if has_cmd('sl') and has_cmd('xterm'):
        for i in range(10):
            subprocess.run(['xterm', '-e', 'sl'])


def has_cmd(cmd: str) -> bool:
    return not subprocess.run(['which', cmd]).returncode


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--street', type=str, help='sub-name of the street. this app notify user while rubbish truck arrives that street.')
    parser.add_argument('-l', '--line_id', type=str, help='line id')
    args = parser.parse_args()
    while True:
        run(args)
        time.sleep(20)
