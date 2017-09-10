from oauth2client.tools import argparser
from data_collection import get_video_data
import datetime

def date_to_string(dt):
	return dt.strftime("%d/%m/%y") + ' ' + str(dt.hour) + ':' + str(dt.minute) + ':' + str(dt.second)

def write_report(video_data, file_name):
	of = open(file_name, 'w')

	# first line
	of.write(date_to_string(datetime.datetime.now().replace(day=datetime.datetime.now().day-1)))
	of.write('\t' + date_to_string(datetime.datetime.now()) + '\n')

	for i in video_data:
		of.write((i['id'] + '\t' + i['title'] + '\t' + str(i['viewCount']) + '\n').encode('utf-8'))







if __name__=='__main__':
	argparser.add_argument('--term', help='search term', default='landslide')
	argparser.add_argument('--report', help='file to save report to', default='report.txt')
	args = argparser.parse_args()

	video_data = get_video_data(args.term)
	video_data = sorted(video_data, key=lambda k: k['viewCount'], reverse=True)[:10]

	write_report(video_data, args.report)
