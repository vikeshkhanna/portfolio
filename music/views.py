# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from music.models import *
from utils.echonest import identify

import json
import urllib


# POST API for checking the status of the song. 
# Request:
# query=JSON object {'metadata':..., 'code':}
# Response:
# found=yes/no
def status(request):
	jsonq  = None
	code = None

	if request.method=="POST":
		try:
			jsonq = request.POST['query']
			print("Query received as request body parameter")
		except KeyError:
			pass
		
		try:
			if request.FILES['query'].size < 10000:
				jsonq = request.FILES['query'].read()
			else:
				pass #TODO: Return Request Too Large
			print("Query received as uploaded file")
		except KeyError:
			pass

		if jsonq:
			try:
				query = json.loads(jsonq)	
				code = query[0]['code']
			except:
				pass # TODO: Return Bad JSON
		else:
			pass #TODO: Return Bad HTTP Request
	elif request.method=="GET":
		code = request.GET["code"] 
	else:
		pass #TODO: Return Bad HTTP Method
	
	# Code is available. GET Echonest Identify API
	if code:
		response = {}
		echonest_response = identify(code)	
		songs = echonest_response['response']['songs']
		response['songs'] = []
		
		for song in songs:
			id = song['id']
			found = 'no'
			
			try:
				dbsong = Song.objects.get(pid=id)
				found = 'yes'
			except ObjectDoesNotExist:
				pass		
			response['songs'].append({'title': song['title'], 'artist_name':song['artist_name'], 'found':found})
		
		return HttpResponse(json.dumps(response))	
	else:
		pass #TODO: Return Bad paramters sent
	return HttpResponse("Hello")

