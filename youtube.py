from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import requests
import json
import datetime
from operator import attrgetter

DEVELOPER_KEY='AIzaSyCf8XJ0p65S6iWzLvj0-WhnOa3bsUuq3Ac'
YOUTUBE_API_VERSION='v3'


BASE_URL = 'https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics,snippet&id='

# popular videos based on search parameter
def get_popular_ids(options):
	youtube = build('youtube', YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
	results = youtube.search().list(
			q=options.q,
			maxResults=options.n,
			part='id',
			publishedAfter=datetime.datetime.now().replace(day=datetime.datetime.now().day-1).isoformat('T') + 'Z'
			).execute().get('items')
	return [i['id']['videoId'] 
			for i in results
				if i['id']['kind']=='youtube#video']




def get_video_data(options):
	video_ids = get_popular_ids(options)	# list of video ids
	video_ids_string = ','.join(video_ids)

	resp = requests.get(BASE_URL + video_ids_string + '&key=' + DEVELOPER_KEY)
	json_data = json.loads(resp.text).get('items')
	
	return [{
		'id': i['id'],
		'duration': i['contentDetails']['duration'],
		'kind': i['kind'],
		'channel': {
			'id': i['snippet']['channelId'],
			'title': i['snippet']['channelTitle']
		},
		'description': i['snippet']['description'],
		'title': i['snippet']['title'],
		'publishedAt': i['snippet']['publishedAt'],
		'tags': i['snippet']['tags'] 
				if 'tags' in i['snippet'] 
				else None,
		'thumbnails': i['snippet']['thumbnails'],
		'commentCount': i['statistics']['commentCount'] 
					if 'commentCount' in i['statistics'] 
					else None,
		'dislikeCount': i['statistics']['dislikeCount'] 
					if 'dislikeCount' in i['statistics'] 
					else None,
		'likeCount': i['statistics']['likeCount'] 
					if 'likeCount' in i['statistics'] 
					else None,
		'viewCount': i['statistics']['viewCount']
	} for i in json_data]
	




if __name__=='__main__':
	argparser.add_argument('--q', help='search term', default='Rick Ross')
	argparser.add_argument('--n', help='num results', default=50)
	args = argparser.parse_args()

	try:
		video_data = get_video_data(args)

		for item in sorted(video_data,reverse=True, key=lambda k: k['viewCount']):
			print item['viewCount']

	except HttpError, e:
		print "Experienced error", e
