import json
import re
import codecs

#files = ["./HCData/HCPosts.txt","./HCData/HCPostsAfterElection.txt"]
#files = ["./DTData/DTPosts.txt","./DTData/DTPostsAfterElection.txt"]
#files = ["./GJData/GJPosts.txt"]
files = ["./JSData/JSPosts.txt"]

data = {}
punc = {"'","\"",",",".","?","!"}

def process(raw_data):
    for entry in raw_data:
        numLikes = entry['likes']
        msg = entry['message']
        for c in punc:
            msg = msg.replace(c," ")
        words = re.split("\s+",msg)
        for word in words:
            word = word.lower()
            if word in data:
                data[word][0] = data[word][0] + 1
                data[word][1] = data[word][1] + numLikes
            else:
                data[word] = [1,numLikes]

for entry in files:
    with open(entry,'r') as f:
        process(json.load(f))

for key, value in data.iteritems():
    data[key].append(value[1]/value[0])

with codecs.open("JSResFavWords.txt",'w','utf-8') as f:
    for key,value in sorted(data.iteritems(), key=lambda (k,v):(v[2],k)):
        f.write(u"%-20s %-10d %-10d  %-10d\n"%(key,value[0],value[1],value[2]))
