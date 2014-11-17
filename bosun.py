import calendar, datetime
import json
import requests
import socket

class bosun_client:
	def __init__(self):
		self.server = 'http://bosun.yourdomain.com'
		self.port = 8070
		self.debug = False

	def write_data(self, metric, value, tags={}, timestamp=None):
		self.metric = metric
		if timestamp == None:
			self.timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
		else:
			self.timestamp = timestamp
		self.value = value
		self.tags = tags

		self.url = self.server + ":" + str(self.port) + "/api/put"

		payload = {
		    "metric": self.metric,
		    "timestamp": self.timestamp,
		    "value": self.value,
		    "tags": {
				"host": str(socket.gethostname()),
			}
		}
		if self.tags != {}:
			payload['tags'].update(self.tags)

		if self.debug == True:
			print "Server -> " + self.url
			print "Tags ->"
			print self.tags
			print "Payload ->"
			print json.dumps(payload)

		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(self.url, data=json.dumps(payload), headers=headers)

		return r.text
