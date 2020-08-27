# -*- coding: utf-8 -*-
import requests

from credentials import DISCORD_WEBHOOK


class Notifier:
    discord_webhook = None

    @staticmethod
    def notify_discord(text):
        data = {'content': '{}'.format(str(text).strip())}
        try:
            requests.post(DISCORD_WEBHOOK, data=data)
        except Exception as e:
            print(e)
