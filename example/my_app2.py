
import sys
import time
import logging


def main(*argv):
    logging.basicConfig(level=logging.INFO)
    while 1:
        logging.info('hello world my_app2')
        time.sleep(3)


if __name__ == '__main__':
    main(*sys.argv)
