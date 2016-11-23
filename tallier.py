import json
import re
import codecs

#files = ["./HCData/HCPosts.txt","./HCData/HCPostsAfterElection.txt"]
#files = ["./DTData/DTPosts.txt","./DTData/DTPostsAfterElection.txt"]
#files = ["./GJData/GJPosts.txt"]
files = ["./JSData/JSPosts.txt"]

data = {}
punc = ".,:!'"

def process(raw_data):
    for entry in raw_data:
        msg = entry['message']
        for c in punc:
            msg = msg.replace(c,'')
        words = re.split("\s+",msg)
        for word in words:
            word = word.lower()
            if word in data:
                data[word] = data[word] + 1
            else:
                data[word] = 1

for entry in files:
    with open(entry,'r') as f:
        process(json.load(f))

with codecs.open("JSRes.txt",'w','utf-8') as f:
    for key,value in sorted(data.iteritems(), key=lambda (k,v):(v,k)):
        f.write(u"%-20s %-10d\n"%(key,value))
