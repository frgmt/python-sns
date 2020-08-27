import logging
import random
from time import sleep

from credentials import INSTAGRAM_ID, INSTAGRAM_PASSWORD
from drivers import Driver

logger = logging.getLogger('sns.instagram')


class Instagram(Driver):
    def __init__(self):
        super(Instagram, self).__init__()
        self.page = None

    def login(self):
        try:
            self.get('https://www.instagram.com/accounts/login/')
            sleep(3)
            sign_box = self.find_element_by_tag_name('form')
            sign_box.find_element_by_name('username').send_keys(INSTAGRAM_ID)
            sign_box.find_element_by_name('password').send_keys(INSTAGRAM_PASSWORD)
            login_btn = sign_box.find_element_by_xpath('//button[@type="submit"]')
            login_btn.click()
            logger.info('login succeeded')
            sleep(3)
            dialog_box = self.find_element_by_xpath('//div[@role="dialog"]')
            btn = dialog_box.find_element_by_tag_name('button')
            btn.click()
        except Exception:
            pass

    def search(self, keyword):
        self.get('https://www.instagram.com/explore/tags/{}/'.format(keyword))
        sleep(3)
        articles = self.find_element_by_tag_name('main').find_element_by_tag_name('article').find_elements_by_tag_name('a')
        links = []
        for article in articles:
            links.append(article.get_attribute('href'))
        self.page = links[random.randrange(len(links))]
        logger.info('search succeeded')

    def follow(self):
        self.get(self.page)
        sleep(3)
        main = self.find_element_by_tag_name('main').find_element_by_tag_name('header')
        button = main.find_element_by_xpath('//button[@type="button"]')
        if ('フォロー中' not in button.text and 'フォロー' in button.text) or ('Following' not in button.text and 'Follow' in button.text):
            button.click()
            self.notify(self.page)
            logger.info('follow succeeded')
        else:
            logger.error('follow failed')

    def like(self):
        self.get(self.page)
        sleep(3)
        div = self.find_element_by_tag_name('main').find_element_by_tag_name('article').find_elements_by_xpath("./div")[-1]
        button = div.find_elements_by_xpath("./section")[0].find_elements_by_xpath("./span")[0].find_element_by_tag_name('button')
        button.click()
        self.notify(self.page)
        logger.info('good succeeded')
