# python-sns
follow or like on twitter and instagram.

# how to use
- chromedriverダウンロード
	- [こちら](http://chromedriver.chromium.org/downloads)から、自身が使っているchromeのversionに合ったchromedriverをダウンロードし、フォルダに入れる
- credentials.pyを作成し、以下の項目を追加する
	- INSTAGRAM_ID = ''  # intagramのID
	- INSTAGRAM_PASSWORD = ''  # instagramのパスワード
	- TWITTER_ID = ''  # twitterのID
	- TWITTER_PASSWORD = ''  # twitterのパスワード
	- DISCORD_WEBHOOK = ''  # discordに通知を送りたい場合のwebhook
	- KEYWORDS = ['']  # followまたはlikeしたいキーワード(複数可)
- pipの追加
	- pip install -r requirements.txt
- コマンド実行
	- python main.py --sns=instagram --follow=False
		- sns=twitter or instagram
		- follow=follow or like

# Other
- 念の為、ランダムでsleepを入れていますが、使用の際は自由に変えてください
