import json
import requests

#Get query info from user
blog = input("Blog target (eg: staff.tumblr.com): ")
type = input("Post type (eg: text, photo): ")
apikey = input("API Key (check the readme to find this): ")

#Variable Moment
target='http://api.tumblr.com/v2/blog/' + blog + '/posts/' + type + '?api_key=' + apikey
data = requests.get(target).json()
postcount = data['response']['total_posts']

#Print query
print("Total Posts: ", postcount)
for post in data['response']['posts']:
	if(post['tags'] != []): #Only post if tags exist
		print("URL: ", post['post_url'])
		print("Date: ", post['date'])
		print("Post: ", post['summary'])
		print("Tags: ", post['tags'])
		print('')
	
