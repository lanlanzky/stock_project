#coding=utf8
#!/usr/bin/env python
import twitter
import os
import sys
api = twitter.Api(consumer_key='7n0BTmcI3IzyebJsehYqfWrl1',consumer_secret='X3JdnxXiT25I7TFsYw6eeiWOMpapiLxMmqiNIk8kLnZGEkXcN9', access_token_key='2419117297-tDWblY55PR0KXdM5lbirj4W8qGZhPQdlh5XAOdL', access_token_secret='TEyRPc4l2b2sX4jBD8wM2qrIUbSbSJlXhN0C0m4XXPAu6')
print 'ok'
statuses = api.GetStatus()
print [s.text for s in statuses]
print dir(api)
print 'ok'

print '获得一个用户的所有 发出的所有消息tweet'
statuses = api.GetUserTimeline('liulanlan')
print [s.text for s in statuses]
print [s.GetId() for s in statuses]
print '获得所有相关 发出的所有消息tweet'
statuses = api.GetHomeTimeline()
print [s.text for s in statuses]
print '获得追随者列表 我收听的别人'
users = api.GetFriends()
print [u.name for u in users]
'''
# 获取
print 'To fetch the most recently posted public Twitter status messages:'
statuses = api.GetPublicTimeline()
print [s.user.name for s in statuses]
# cannot post date
#status = api.PostUpdate('I love python-twitter!')                             
import re,urllib2,urllib
 
user = {'session[username_email]':'liulanlan','session[password]':'lll19891202'}
data = {
    'status':"""
Send by Python!
""",
    'tab':'home',
    'source':'web',
    }
 
def u(s, encoding):
    if isinstance(s, unicode):
        return s
    else:
        try:
            return unicode(s, encoding)
        except:
            return s
 
def send(user=user,data=data):
    c = urllib2.HTTPCookieProcessor()
    builder = urllib2.build_opener(c)
    url = 'https://twitter.com/sessions'
    request = urllib2.Request(
        url=url,
        data = urllib.urlencode(user)
        )
    d = builder.open(request)
    r = re.compile('<input name="authenticity_token" type="hidden" value="(.*?)" />')
    x = d.read()
    if len(re.compile(r"name=\"session\[username_or_email\]\"").findall(x))>0:
        print "Login Error!"
        return False
    auth = {'authenticity_token':r.findall(x)[0]}
    send = '%s&%s'%(
        urllib.urlencode(auth),
        urllib.urlencode(data)
        )
    request = urllib2.Request(
        url='http://twitter.com/status/update',
        data = send ,
        )
    builder.open(request)
    return True
 
if __name__=="__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1]!="":
        data["status"] = u(" ".join(sys.argv[1:]),"gb2312").encode("utf-8")
    if send():
        print 'ok'

'''
