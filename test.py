# -*- coding: utf-8 -*-
import json
import sys
import jieba
reload(sys)
sys.setdefaultencoding('utf-8')
file=open('sample','r+')
weibo_text=[json.loads(line) for line in file]
len=len(weibo_text)
keys=[]
for key in weibo_text[0]:
	keys.append(key)
print 'weibo number:',len,type(weibo_text[0])
print "the first one: content",weibo_text[0]["content"]
# print u'各项包括',keys
weibo_fenci=[]
for weibo in weibo_text:
	seg_list=jieba.cut(weibo["content"],cut_all=False)
	weibo_fenci.append(seg_list)

for i,value in enumerate(weibo_fenci):
	print i,
	for word in value:
		print word,
	print " "