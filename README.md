# [arthricia](https://giphy.com/gifs/13a81USMXqsTnO/html5)
Purge your tweets and likes

Based on [`koenrh/delete-tweets`](https://github.com/koenrh/delete-tweets) with `unlike` function from [`melissamcewen/unlike.py`](https://gist.github.com/melissamcewen/37125ee31615f3f7f53de47459053bf1).

## Prerequisites

### Configure API access

1. Open [`developer.twitter.com`](https://developer.twitter.com), and [create
  a new app](https://developer.twitter.com/en/apps/create).
1. Get your API keys from the `Keys and tokens` tab
1. `export` your API keys as the following environment variables:

```bash
export TWITTER_CONSUMER_KEY="[your consumer key]"
export TWITTER_CONSUMER_SECRET="[your consumer secret]"
export TWITTER_ACCESS_TOKEN="[your access token]"
export TWITTER_ACCESS_TOKEN_SECRET="[your access token secret]"
```

### Get your Twitter data

1. Open the [Your Twitter data](https://twitter.com/settings/your_twitter_data) page
1. Scroll to the bottom of the page, click `Request data` and wait for the email to arrive.
1. Follow the link in the email to download your Twitter data.
1. Unpack the archive, and **copy** `tweet.js` and `like.js` to the same directory as this script.

### Preprocess `tweet.js` and `like.js`

The first line of both files will contain:
```
window.YTD.like.part0 = [ {
```
Remove:
```
window.YTD.like.part0 = 
```

So that the first line reads: 
```
[ {
```

## Installation

Install the required dependencies.

```
pip install -r requirements.txt
```

## Usage

```
$ ./purge.py
usage: purge.py [-h] [-t] [-l] [-b]

Delete old tweets.

optional arguments:
  -h, --help  show this help message and exit
  -t          Delete all tweets
  -l          Unlike all likes
  -b          Delete all tweets and Unlike all likes
```