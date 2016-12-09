import json
import re
import codecs

#files = ["./HCData/HCPosts.txt","./HCData/HCPostsAfterElection.txt"]
#files = ["./DTData/DTPosts.txt","./DTData/DTPostsAfterElection.txt"]
#files = ["./GJData/GJPosts.txt"]
files = ["./JSData/JSPosts.txt"]

punc = ".,:!'"

def writeToFile(data,num):
    with codecs.open("./JSData/JSResWeek{}Likes.txt".format(num),'w','utf-8') as f:
        for key,value in sorted(data.iteritems(), key=lambda (k,v):(v,k)):
            f.write(u"%-20s %-10d\n"%(key,value))

startTime = 1467331200
increment = 604800

def process(raw_data):
#    print raw_data
    global startTime
    counter = 1
    data = {}
    for entry in raw_data:
        numLikes = entry['likes']
        msg = entry['message']
	time = entry['time']
        for c in punc:
            msg = msg.replace(c,'')
        words = re.split("\s+",msg)
        if (time>=startTime) and (time<startTime+increment):
            for word in words:
                word = word.lower()
                if word in data:
                    data[word] = data[word] + numLikes
                else:
                    data[word] = numLikes
        elif time>=startTime+increment:
	    writeToFile(data,counter)
	    startTime = startTime+increment
	    counter = counter+1
	    data = {}
	    for word in words:
                word = word.lower()
                if word in data:
                    data[word] = data[word] + numLikes       
                else:
                    data[word] = numLikes
	else:
	    print "Error"

        
source_data = []

for entry in files: 
    with open(entry,'r') as f:
        source_data = json.load(f) + source_data

source_data.reverse()
process(source_data)
