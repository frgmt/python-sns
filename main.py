import logging
import random
import argparse

from credentials import KEYWORDS
from instagram import Instagram
from twitter import Twitter
from utils import init_loggers, random_sleep

logger = logging.getLogger('sns.main')

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == '__main__':
    init_loggers()

    parser = argparse.ArgumentParser()
    parser.add_argument('--sns', default='twitter')
    parser.add_argument('--follow', default=True, type=str2bool)
    args = parser.parse_args()
    i = 0
    refresh_point = 5

    if args.sns == 'twitter':
        twitter = Twitter()
        while True:
            keyword = KEYWORDS[random.randrange(len(KEYWORDS))]
            try:
                twitter.login()
                twitter.search(keyword)
                if args.follow:
                    twitter.follow()
                    if i % refresh_point == 0:
                        twitter.refresh()
                else:
                    if i % refresh_point == 0:
                        twitter.like()
                        twitter.follow()
                        twitter.refresh()
                    else:
                        twitter.like()
            except Exception as e:
                print(e)
            finally:
                # twitter.quit()
                random_sleep(300, 600)
                i += 1
    else:
        instagram = Instagram()
        while True:
            keyword = KEYWORDS[random.randrange(len(KEYWORDS))]
            try:
                instagram.login()
                instagram.search(keyword)
                if args.follow:
                    instagram.follow()
                    if i % refresh_point == 0:
                        instagram.refresh()
                else:
                    if i % refresh_point == 0:
                        instagram.like()
                        instagram.follow()
                        instagram.refresh()
                    else:
                        instagram.like()
            except Exception as e:
                print(e)
            finally:
                # instagram.quit()
                random_sleep(300, 600)
                i += 1
