from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
#from .models import ScoreBoard
import requests
import os
import json
import sys
# Create your views here.
"""registration_details = request.POST
user = User.objects.create_user(registration_details['username'],registration_details['password'])"""
def home(request):
	return render(request,"home.html",{})
def a(request):
	return render(request,"bfs.txt",{})
def login(request):
	return render(request,"login.html",{})
def feed(request):
	registration_details = request.POST
	#user = User.objects.create_user(registration_details['username'],registration_details['password'])
	#user = User.objects.get(registration_details['username'],registration_details['password'])
	if user is not None:
		if user.is_active:
			return render(request,"feed.html",{})
		else:
			return HttpResponse("not registered")
	#return render(request,"feed.html",{})

def quest(request):
	return render(request,"quest.json",{})
def test(request):
	return render(request,"test.json",{})

def logint(request):
	return render(request,"logint.html",{})


def register(request):
    registration_details = request.POST
    if( registration_details['password'] == registration_details['rpassword'] ):
        user = User.objects.create_user(username=registration_details['username'],password=registration_details['password'])
        user.save();
        return render(request,"logint.html",{})

def validate(request):
    form_details = request.POST
    user 	 = authenticate(username=form_details['username'],password=form_details['password']);

    if user is not None:
        if user.is_active:
            return render(request,"feed.html")
    else:
    	return HttpResponse("not registered")
def get(request):
	requestdict = request.POST
	source = requestdict["source"]
	lang = requestdict["lang"]
	testcases = requestdict["testcases"]
	output=requestdict.get("output")
	timeout=1

	url = "api.hackerrank.com/checker/submission.json"
	api_key = "hackerrank|161256-622|faa76a548e2dce2ef37df6a68d4dc0c75bd760f3"
	r = requests.post("http://api.hackerrank.com/checker/submission.json", data = {
	    "source" : source,
	    "lang" : lang,
	    "testcases" : testcases,
	    "api_key" : api_key
	})
	result = r.json()
	try:
		out=int(result['result']['stdout'][0])



		output=int(output)
		if(output==out):
			return HttpResponse("Output: "+result['result']['stdout'][0]+ "<br>" +"Compile Time: "+str(result['result']['time'][0])	)
		else:
			return HttpResponse("Expected Output :"+str(output)+"<br>"+"Output:"+(result['result']['stdout'][0]))
		#return HttpResponse(out)
	except TypeError:
		return HttpResponse(result['result']['compilemessage'])
		#return HttpResponse("Compile error:<br>"+result['result']['compilemessage'])
	except KeyError:
		return HttpResponse("Key error<br> Output format not recognized")
	except:
		return HttpResponse("Compile error<br> Unexcpected output (output type not allowed)")

def sub(request):
	requestdict = request.POST
	source = requestdict["source"]
	lang = requestdict["lang"]
	testcases = requestdict["testcases"]
	output=requestdict.get("output")
	timeout=1

	url = "api.hackerrank.com/checker/submission.json"
	api_key = "hackerrank|161256-622|faa76a548e2dce2ef37df6a68d4dc0c75bd760f3"
	r = requests.post("http://api.hackerrank.com/checker/submission.json", data = {
	    "source" : source,
	    "lang" : lang,
	    "testcases" : testcases,
	    "api_key" : api_key
	})
	result = r.json()
	try:
		out=int(result['result']['stdout'][0])
		output=int(output)
		if(output==out):
			return HttpResponse("Output: "+result['result']['stdout'][0]+ "<br>" +"Compile Time: "+str(result['result']['time'][0])	)
		else:
			return HttpResponse("Expected Output :"+str(output)+"<br>"+"Output:"+(result['result']['stdout'][0]))
		#return HttpResponse(out)
	except TypeError:
		return HttpResponse("TypeError")
		#return HttpResponse("Compile error:<br>"+result['result']['compilemessage'])
	except KeyError:
		return HttpResponse("Key error<br> Output format not recognized")

	except:
		return HttpResponse("Compile error<br> Unexcpected output (output type not allowed)")

def tst(request, ScoreBoard):
	current_user = request.user
	probno = request.probid
	if current_user.is_authenticated():
		userscore = ScoreBoard.get_object_or_404(pk=current_user.Username)
		if probno == 1 and userscore.Prob1 != 10:
			userscore.Prob1 = 10
		elif probno == 2 and userscore.Prob2 != 10:
			userscore.Prob2 = 10
		elif probno == 3 and userscore.Prob3 != 10:
			userscore.Prob3 = 10
		elif probno == 4 and userscore.Prob4 != 10:
			userscore.Prob4 = 10
		elif probno == 5 and userscore.Prob5 != 10:
			userscore.Prob5 = 10
		else
			return Http404("Don't screw with the system")
	else
		return Http404("Maybe you should try logging in and try again... Douche")
