# Scraplr
Scraplr lets you find Tumblr tags that the not-so-great search feature can't find. 

<h1>Requirements</h1>

* Python 3.x
* [PyTumblr](https://github.com/tumblr/pytumblr)
* Requests `pip install requests` (You may need to do pip3 on macOS)
* A Tumblr API key.
  * If you don't have one, create a [Tumblr App.](https://www.tumblr.com/oauth/register) 
  * You can use this page as the Application Website and Default Callback URL. They aren't necessary for this script.
  * Once you have created the app, your OAuth consumer key will be the API Key you'll use for Scraplr.

<h1>Usage</h1>

1. Execute `python3 scraplr.py`
2. Enter the blog URL to target (ie; staff.tumblr.com). For the post type, you can enter the following:
  `text, photo, quote, link, chat, audio, video`
3. Your API key will be the OAuth consumer key you just made when creating a Tumblr App. If you lost the tab, [click here.](https://www.tumblr.com/oauth/apps)

<h1>Troubleshooting</h1>

Tumblr's API has [a number of funky limits](https://www.tumblr.com/docs/en/api/v2#rate-limits), so be sure to not use the app too much.
