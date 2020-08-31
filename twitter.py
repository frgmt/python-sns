import logging
import random
from time import sleep

from credentials import TWITTER_ID, TWITTER_PASSWORD
from drivers import Driver

logger = logging.getLogger('sns.twitter')


class Twitter(Driver):
    def __init__(self):
        super(Twitter, self).__init__()
        self.user = None
        self.like_btn = None

    def login(self):
        try:
            self.get('https://twitter.com/login')
            sleep(3)
            sign_box = self.find_element_by_tag_name('form')
            sign_box.find_element_by_name('session[username_or_email]').send_keys(TWITTER_ID)
            sign_box.find_element_by_name('session[password]').send_keys(TWITTER_PASSWORD)
            login_btn = sign_box.find_element_by_xpath('//div[@role="button"]')
            login_btn.click()
            logger.info('login succeeded')
        except Exception:
            pass

    def search(self, keyword):
        self.get('https://twitter.com/search?q={}&src=typed_query&f=live'.format(keyword))
        sleep(3)
        articles = self.find_elements_by_tag_name('article')
        links = []
        likes = []
        for article in articles:
            links.append(article.find_element_by_tag_name('a').get_attribute('href'))
            likes.append(article.find_element_by_xpath('//div[@data-testid="like"]'))
        self.user = links[random.randrange(len(links))]
        self.like_btn = likes[random.randrange(len(likes))]
        logger.info('search succeeded')

    def follow(self):
        self.get(self.user)
        sleep(3)
        main = self.find_element_by_tag_name('main')
        buttons = main.find_elements_by_xpath('//div[@role="button"]')
        for button in buttons:
            if button.get_attribute('data-testid') and 'unfollow' not in button.get_attribute(
                    'data-testid') and 'follow' in button.get_attribute('data-testid'):
                button.click()
                self.notify(self.user)
                logger.info('follow succeeded')
                return
        logger.error('follow failed: {}'.format(self.user))

    def like(self):
        self.like_btn.click()
        logger.info('good succeeded')

