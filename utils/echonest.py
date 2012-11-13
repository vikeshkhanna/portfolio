from portfolio.settings import *
import json
import urllib

def identify(code):
	'''
	params = urllib.urlencode({'api_key':ECHONEST_API_KEY, 'code':code})
	f = urllib.urlopen(ECHONEST_IDENTIFY_ROOT + "?%s" % params)
	return json.loads(f.read())
	'''
	return {u'response': {u'status': {u'code': 0, u'message': u'Success', u'version': u'4.2'}, u'songs': [{u'title': u'105. Another Brick in the Wall, Pt. 2', u'artist_name': u'Pink Floyd', u'artist_id': u'ARD4C1I1187FB4B0C3', u'score': 143, u'message': u'OK (match type 5)', u'id': u'SOIVZWT12A6D4F3DA9'}]}}
