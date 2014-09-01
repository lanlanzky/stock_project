# -*- coding: utf-8 -*-

import time
import pycurl
import urllib
import json
import oauth2 as oauth

 
API_ENDPOINT_URL = 'https://stream.twitter.com/1.1/statuses/filter.json'
USER_AGENT = 'TwitterStream 1.0' # This can be anything really
 
# You need to replace these with your own values
OAUTH_KEYS = {'consumer_key': "7n0BTmcI3IzyebJsehYqfWrl1",
              'consumer_secret': "X3JdnxXiT25I7TFsYw6eeiWOMpapiLxMmqiNIk8kLnZGEkXcN9",
              'access_token_key': "2419117297-tDWblY55PR0KXdM5lbirj4W8qGZhPQdlh5XAOdL",
              'access_token_secret': "TEyRPc4l2b2sX4jBD8wM2qrIUbSbSJlXhN0C0m4XXPAu6"}
 
# These values are posted when setting up the connection
POST_PARAMS = {'include_entities': 0,
               'stall_warning': 'true',
               'track': 'GOOG,QIHU,SOHU,SINA,NCTY,PWRD,CTRP,JOBS,LONG,UTSI,CNTF,SMI,VIMC,ACTS,EDU,HMIN,VISN,EJ,AMCN,ACH,CEO'
	      }  # 追踪关键词
 
class TwitterStream:
    def __init__(self):
        self.oauth_token = oauth.Token(key=OAUTH_KEYS['access_token_key'], secret=OAUTH_KEYS['access_token_secret'])
        self.oauth_consumer = oauth.Consumer(key=OAUTH_KEYS['consumer_key'], secret=OAUTH_KEYS['consumer_secret'])
        self.conn = None
        self.buffer = ''
        self.setup_connection()
 
    def setup_connection(self):
        """ Create persistant HTTP connection to Streaming API endpoint using cURL.
        """
        if self.conn:
            self.conn.close()
            self.buffer = ''
        self.conn = pycurl.Curl()
        self.conn.setopt(pycurl.URL, API_ENDPOINT_URL)
        self.conn.setopt(pycurl.USERAGENT, USER_AGENT)
        # Using gzip is optional but saves us bandwidth.
        self.conn.setopt(pycurl.ENCODING, 'deflate, gzip')
        self.conn.setopt(pycurl.POST, 1)
        self.conn.setopt(pycurl.POSTFIELDS, urllib.urlencode(POST_PARAMS))
        self.conn.setopt(pycurl.HTTPHEADER, ['Host: stream.twitter.com',
                                             'Authorization: %s' % self.get_oauth_header()])
        # self.handle_tweet is the method that are called when new tweets arrive
        self.conn.setopt(pycurl.WRITEFUNCTION, self.handle_tweet)


    def get_oauth_header(self):
        params = {'oauth_version': '1.0',
            'oauth_nonce': oauth.generate_nonce(),
            'oauth_timestamp': int(time.time())}
        req = oauth.Request(method='POST', parameters=params, url='%s?%s' % (API_ENDPOINT_URL,
            urllib.urlencode(POST_PARAMS)))
        req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), self.oauth_consumer, self.oauth_token)
        return req.to_header()['Authorization'].encode('utf-8')



    def start(self):
        """ Start listening to Streaming endpoint.
        Handle exceptions according to Twitter's recommendations.
        """
        backoff_network_error = 0.25
        backoff_http_error = 5
        backoff_rate_limit = 20
        while True:
            self.setup_connection()
            try:
                self.conn.perform()
            except:
                # Network error, use linear back off up to 16 seconds
                print 'Network error: %s' % self.conn.errstr()
                print 'Waiting %s seconds before trying again' % backoff_network_error
                time.sleep(backoff_network_error)
                backoff_network_error = min(backoff_network_error + 1, 16)
                continue
            # HTTP Error
            sc = self.conn.getinfo(pycurl.HTTP_CODE)
            if sc == 420:
                # Rate limit, use exponential back off starting with 1 minute and double each attempt
                print 'Rate limit, waiting %s seconds' % backoff_rate_limit
                time.sleep(backoff_rate_limit)
                backoff_rate_limit *= 2
            else:
                # HTTP error, use exponential back off up to 320 seconds
                print 'HTTP error %s, %s' % (sc, self.conn.errstr())
                print 'Waiting %s seconds' % backoff_http_error
                time.sleep(backoff_http_error)
                backoff_http_error = min(backoff_http_error * 2, 320)
    
    def handle_tweet(self, data):
        """ This method is called when data is received through Streaming endpoint.
        """
        self.buffer += data
        if data.endswith('\r\n') and self.buffer.strip():
            # complete message received
            message = json.loads(self.buffer)
            self.buffer = ''
            msg = ''
            if message.get('limit'):
                print 'Rate limiting caused us to miss %s tweets' % (message['limit'].get('track'))
            elif message.get('disconnect'):
                raise Exception('Got disconnect: %s' % message['disconnect'].get('reason'))
            elif message.get('warning'):
                print 'Got warning: %s' % message['warning'].get('message')
            else:
                print 'Got tweet with text: %s' % message.get('text')

#  以下为自己重写
class New_byself(TwitterStream):
    def handle_tweet(self, data):
        self.buffer += data
        if data.endswith('\r\n') and self.buffer.strip():
            # complete message received
            message = json.loads(self.buffer)
            self.buffer = ''
            msg = ''
            if message.get('limit'):
                print 'Rate limiting caused us to miss %s tweets' % (message['limit'].get('track'))
            elif message.get('disconnect'):
                raise Exception('Got disconnect: %s' % message['disconnect'].get('reason'))
            elif message.get('warning'):
                print 'Got warning: %s' % message['warning'].get('message')
            else:
                print message.keys()
	#	print dir(message) message is a dict
                print 'the tweet : %s' % message.get('text')
        


#test = TwitterStream()
test = New_byself()
test.start()
