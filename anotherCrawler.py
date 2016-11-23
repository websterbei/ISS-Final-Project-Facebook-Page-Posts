import time
import datetime
import json
import requests

#hcUrl = "https://graph.facebook.com/hillaryclinton/feed?access_token=1808895612725183|Fjm00832L4zLhnqg4mwI7x3uHCU"

hcUrl = "https://graph.facebook.com/DonaldTrump/feed?access_token=1808895612725183|Fjm00832L4zLhnqg4mwI7x3uHCU"

likesUrl = "https://graph.facebook.com/{}/likes?summary=true&access_token=1808895612725183|Fjm00832L4zLhnqg4mwI7x3uHCU"

stoppingTime = 1478720620.0
flag = True
Result = []
i = 0
while True:
	if not flag:
		break
	res = requests.get(hcUrl)
	raw_data = json.loads(res.text)
	postData = raw_data['data']
	for entry in postData:
		raw_time = entry['created_time'].split('+')[0]
		timestamp = time.mktime(datetime.datetime.strptime(raw_time, "%Y-%m-%dT%H:%M:%S").timetuple());
		if timestamp<stoppingTime:
			flag = False
			break
		try:
			message = entry['message']
		except:
			continue
		postInfo = requests.get(likesUrl.format(entry['id']))
		raw_post_info = json.loads(postInfo.text)
		summary = raw_post_info['summary']
		resDict = {}
		resDict['time'] = timestamp;
		resDict['message'] = message;
		resDict['likes'] = summary['total_count']
		Result.append(resDict)
	i = i+1
	print "Finished #{} Retrieval....".format(i+1)
	hcUrl = raw_data['paging']['next']

jsonResult = json.dumps(Result)
#print jsonResult

f = open('DTData/DTPostsAfterElection.txt','w')
f.write(jsonResult)
f.close()
#raw_data = json.loads(res.text)

#print raw_data['data']
