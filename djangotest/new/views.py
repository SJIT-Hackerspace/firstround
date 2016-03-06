from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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
	req = request.POST
	userr=req["user"]
	score=req["scorec"]
	
	score=int(score)
	#score=score+1
	return render(request,"feed.html",{'username':userr,'score':score})
	#return HttpResponse(userr) 



def quest(request):
	return render(request,"quest.json",{})
def test(request):
	return render(request,"test.json",{})

def logint(request):
	return render(request,"logint.html",{})
	

def register(request):
    try:
    	registration_details = request.POST
    	if( registration_details['password'] == registration_details['rpassword'] ):
        	user = User.objects.create_user(username=registration_details['username'],password=registration_details['password'])
        	user.save();
        	#userscore=ScoreBoard.
        	return render(request,"logint.html",{})
    except:
    	return HttpResponse("Already Registered") 

def bye(request):
	req=request.POST
	user=req['user']
	score=req['scorec']	
	with open('static/djangotest/finalresult.json', 'a') as f:
		data={
		user:score
		}
		json.dump(data,f)
	return render(request,"bye.html",{'username':user,'score':score})

def validate(request):
    form_details = request.POST
    user 	 = authenticate(username=form_details['username'],password=form_details['password']);
    
    if user is not None:
        if user.is_active:

        	return render(request,"feed.html",{'username':user,'score':'0'})
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
			return HttpResponse("Success<br>  Output: "+result['result']['stdout'][0]+ "<br>" +"Compile Time: "+str(result['result']['time'][0])	)
		else:
			return HttpResponse("Output Doesn't Match the testcases"+"<br>"+"Your Output:"+(result['result']['stdout'][0]))
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
	userr=requestdict.get("usr")
	output=requestdict.get("output")
	score=requestdict.get("scoref")
	qno=requestdict.get("qno")
	qno=int(qno)
	score=int(score)
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

		#return HttpResponse("user"+str(userr))

		output=int(output)
		if(output==out):
			try:
				score=score+1
				with open('static/djangotest/result.json', 'r+') as f:
					data1 = json.load(f)
					a=data1[userr]
					a=a+1
					pos=f.tell()
					a=a.str()
					us=userr+a
					data={
					us:a
					}
					json.dump(data,f)
								
				#return HttpResponse("Submitted Successfully!")
				return render(request,"home.html",{'username':userr,'score':score,'result':'true'})
			except:
				with open('static/djangotest/result.json', 'a+') as f:
					data={
					userr:qno
					}
					json.dump(data,f)
					return render(request,"feed.html",{'username':userr,'score':score})

		else:
			return render(request,"feed.html",{'username':userr,'score':score})
			#return HttpResponse(out)	
	except TypeError:	
		return HttpResponse("TypeError")	
		#return HttpResponse("Compile error:<br>"+result['result']['compilemessage'])
	except KeyError:
		return HttpResponse("Key error<br> Output format not recognized")	
	
	except Exception:
		return HttpResponse("Compile error<br> Unexcpected output (output type not allowed)"+str(Exception))	
		
