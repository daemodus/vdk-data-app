#!/usr/bin/env python3

import argparse
import logging

from app import dummy

logger = logging.getLogger(__name__)


def configure_logging():
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-15s %(levelname)-4s %(message)s',
        '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(_):
    configure_logging()
    logger.info('Started running')
    print(dummy.dummy())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='VDK Data App',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    main(parser.parse_args())
