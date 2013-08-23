# -*- coding: utf-8 -*-
import mimetypes
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404

from djangoapps.myapp.models import *
from djangoapps.myapp.forms import DocumentForm

def main(request, urlKey):
	key = urlKeyList.objects.filter(urlKey__exact=urlKey)
	if len(key) == 0:
		raise Http404
	form = DocumentForm() # A empty, unbound form

	# Load documents for the list page
	documents = None

	# Render list page with the documents and the form
	return render_to_response('myapp/list.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request))

def upload(request, urlKey):
	key = urlKeyList.objects.filter(urlKey__exact=urlKey)
	if len(key) == 0:
		raise Http404
	key.delete()
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		newdoc = UploadedFile()
		newdoc.set_data(request.FILES['docfile'].read())
		newdoc.filename = request.FILES['docfile'].name
		import random
		newdoc.fileKey = str(random.randrange(10000000000, 99999999999))
		newdoc.save()
		
		# Redirect to the document list after POST
		returnString = "<a href=\"../../file/" + newdoc.fileKey + "/" + request.FILES['docfile'].name + "\">link to your file</a/>"
		return HttpResponse(returnString)
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the list page
	documents = Document.objects.all()

	# Render list page with the documents and the form
	return render_to_response(
		'myapp/list.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def download(request, fileKey, filename):
	denis = UploadedFile.objects.filter(fileKey__exact=fileKey).filter(filename__exact=filename)
	if len(denis) == 0:
		raise Http404
	else:
		denis = denis[0]
	# todo check to make sure the file isn't too old
	mime = mimetypes.guess_type(denis.filename, strict=True)
	return HttpResponse(denis.get_data(), content_type=mime)

def createKey(request):
	newKey = urlKeyList()
	import random
	newKey.urlKey = str(random.randrange(10000000000, 99999999999))
	newKey.save()
	
	returnString = "<a href=\"../" + newKey.urlKey + "/\">link to your upload form</a/>"
	return HttpResponse(returnString)
