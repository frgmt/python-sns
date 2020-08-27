import logging
import random
import argparse

from credentials import KEYWORDS
from instagram import Instagram
from twitter import Twitter
from utils import init_loggers, random_sleep

logger = logging.getLogger('sns.main')

if __name__ == '__main__':
    init_loggers()

    parser = argparse.ArgumentParser()
    parser.add_argument('--sns', default='twitter')
    parser.add_argument('--follow', default=True, type=bool)
    args = parser.parse_args()

    if args.sns == 'twitter':
        twitter = Twitter()
        while True:
            keyword = KEYWORDS[random.randrange(len(KEYWORDS))]
            try:
                twitter.login()
                twitter.search(keyword)
                if args.follow:
                    twitter.follow()
                else:
                    twitter.like()
            except Exception as e:
                print(e)
            finally:
                # twitter.quit()
                random_sleep(150, 600)
    else:
        instagram = Instagram()
        while True:
            keyword = KEYWORDS[random.randrange(len(KEYWORDS))]
            try:
                instagram.login()
                instagram.search(keyword)
                if args.follow:
                    instagram.follow()
                else:
                    instagram.like()
            except Exception as e:
                print(e)
            finally:
                # instagram.quit()
                random_sleep(150, 600)
