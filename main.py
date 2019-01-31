import test
import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True)
# tweets=api.home_timeline(count=1, tweet_mode='extended')
# for i in tweets:
# 	start_id=i.id_str
count=0
used_ids=[]
while True:
	tweets=api.home_timeline(count=10, tweet_mode='extended')
	print(count)
	for i in tweets:
		# print(i.full_text)
		# print('id=', i.id_str, '\nused_ids=', used_ids, '\nretweeted=', str(i._json['retweeted']))
		# print('id', i.id_str in used_ids)
		if i.id_str not in used_ids:
			print(i.full_text)
			id1 =i.id_str
			media_urls=[]
			post=""
			username=i._json['user']['name']
			if username[-1] in 'աէըիօու' or username[-1] in 'աէըիօու'.upper():
				post+="_[%s](http://twitter.com/%s)ն"%(username, i._json['user']['screen_name'])
			elif username[-1] in 'բգդզթժլխծկհձղճմյնշչպջռսվտրցփքֆ' or username[-1] in 'բգդզթժլխծկհձղճմյնշչպջռսվտրցփքֆ'.upper():
				post+="_[%s](http://twitter.com/%s)ը"%(username, i._json['user']['screen_name'])
			elif username[-1] in 'AEIOU' or username[-1] in 'AEIOU'.lower():
				post+="_[%s](http://twitter.com/%s)-ն"%(username, i._json['user']['screen_name'])
			else:
				post+="_[%s](http://twitter.com/%s)-ը"%(username, i._json['user']['screen_name'])
			post+= " [գրում ա](http://twitter.com/%s/status/%s)`_\n\n"%(username, id1)
			# print('username=  ', username)
			# print('post=  ', post)
			# print(i._json['user']['screen_name'])
			if 'media' in i._json['entities']:
				for media_iter in range(len(i._json['extended_entities']['media'])):
					media_urls.append(i._json['extended_entities']['media'][media_iter]['media_url_https'])
			if 'https://t.co/' in i.full_text:
				post+='  '+str(i.full_text[:i.full_text.index('https://t.co/')])
			else:
				post+='  '+str(i.full_text)
			if len(media_urls)!=0:
				post+='\n'
				for i in media_urls:
					post+='![](%s) '%(str(i))
			test.post(post)
			count+=1
			print(count)
			print(type(i))
			if type(i)=='str': print( i)
			used_ids.append(id1)
		else:
			print('count=',count, ' continued')
			continue