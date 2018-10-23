#!/usr/bin/env python3
# arthricia/purge.py

# purge.py
# Purge your tweets and likes

## Imports
import argparse
import json
import sys
import time
import os
import signal
import twitter


def delete(api):

    if os.path.isfile("tweet.js") is False: 
        error("No tweet.js file found.")

    with open('tweet.js') as file:
        jsonData = file.read()
        data = json.loads(jsonData)
        count = 0

        for line in data:
            tweet_id = line["id_str"]
            tweet_date = line["created_at"]

            try:
                print("Deleting tweet #{} ({})".format(tweet_id, tweet_date))
                api.DestroyStatus(tweet_id)
                count += 1
                time.sleep(0.2)

            except twitter.TwitterError as err:
                err = err.message[0]
                if err['code'] == 144:
                    print("Error({}): {} (It was probably deleted)\n".format(err['code'], err['message']))
                else: 
                    print("Error({}): {}\n".format(err['code'], err['message']))


    print("Number of deleted tweets: {}\n".format(count))


def unlike(api):

    if os.path.isfile("like.js") is False: 
        error("No like.js file found.")

    with open('like.js') as file:
        jsonData = file.read()
        data = json.loads(jsonData)
        count = 0

        for line in data:
            tweet_id = line['like']['tweetId']

            try:
                print("Unliking tweet #{}".format(tweet_id))
                # api.CreateFavorite(status_id=tweet_id)
                # See: https://medium.com/@melissamcewen/how-to-completely-delete-your-twitter-likes-5a41c35aefb8
                api.DestroyFavorite(status_id=tweet_id)
                count += 1
                time.sleep(0.2)

            except twitter.TwitterError as err:
                err = err.message[0]
                if err['code'] == 144:
                    print("Error({}): {} (It was probably already unliked)\n".format(err['code'], err['message']))
                else: 
                    print("Error({}): {}\n".format(err['code'], err['message']))

    print("Number of unliked tweets: {}\n".format(count))


def error(msg, exit_code=1):
    sys.stderr.write("Error: {}\n".format(msg))
    exit(exit_code)


def ctrl_c(sig, frame):
    print("\n{} chose to quit via CTRL+C!".format(os.environ['USER']))
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Purge your tweets and likes")
    parser.add_argument("-t", action='store_true', 
                        help="Purge all tweets")
    parser.add_argument("-l",  action='store_true',
                        help="Unlike all likes")
    parser.add_argument("-b",  action='store_true',
                        help="Purge tweets and likes")
    args = parser.parse_args()

    signal.signal(signal.SIGINT, ctrl_c)

    if not ("TWITTER_CONSUMER_KEY" in os.environ and
                "TWITTER_CONSUMER_SECRET" in os.environ and
                "TWITTER_ACCESS_TOKEN" in os.environ and
                "TWITTER_ACCESS_TOKEN_SECRET" in os.environ):
        error("No consumer key/secret and/or access token/secret set.")

    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    if args.t: 
        delete(api)
    elif args.l:
        unlike(api)
    elif args.b:
        delete(api)
        unlike(api)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
