import got

import json
import tweepy
import simplejson as json
import datetime
from tweepy import OAuthHandler	
 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tuit):
    print json.dumps(tuit)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text) 

# for tuit in tweepy.Cursor(api.get_user, id="SanCArlos"):
#     process_or_store(tuit._json)



# Variable usuario
usuario = raw_input("Usuario?")

# Variable fecha creacion usuario
u = api.get_user(usuario)
# print u.created_at

# Variable fecha
inicio = u.created_at
date_1 = inicio

# print end_date
end_date = date_1 + datetime.timedelta(days=15)
strInicio = inicio.strftime("%Y-%m-%d")
strEnd = end_date.strftime("%Y-%m-%d")


tweet = False
def main():

	def get_tweets(since, until, user):
		try: 
			# Example 3 - Get tweets by username and bound dates
			tweetCriteria = got.manager.TweetCriteria().setUsername(user).setSince(since).setUntil(until).setMaxTweets(-1)
			# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
			last_tweet = got.manager.TweetManager.getTweets(tweetCriteria)[-1]
			
			print last_tweet.text
			print last_tweet.id
			print last_tweet.date
			print 'hay tweet'
			tweet = True
		except IndexError:
			strInicio = until
			t_until = datetime.datetime.strptime(until, "%Y-%m-%d")
			m_until = t_until + datetime.timedelta(days=15)
			strEnd = m_until.strftime("%Y-%m-%d")
			# print 'no hay tweet'
			# print strInicio
			# print strEnd
			get_tweets(strInicio,strEnd, user)

	while tweet == False:
		get_tweets(strInicio,strEnd, usuario)
		break

if __name__ == '__main__':
	main()
	