from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
import json
import sys
# Create your views here.
def home(request):
	return render(request,"home.html",{})
def a(request):
	return render(request,"bfs.txt",{})
def login(request):
	return render(request,"login.html",{})
def feed(request):
	return render(request,"feed.html",{})

def quest(request):
	return render(request,"quest.json",{})
def test(request):
	return render(request,"test.json",{})

def loginh(request):
	return render(request,"loginh.html",{})
	
def get(request):
	requestdict = request.POST
	source = requestdict["source"]
	lang = requestdict["lang"]
	testcases = requestdict["testcases"]
	output = requestdict["out"]
	timeout=1
	url = "api.hackerrank.com/checker/submission.json"
	api_key = "hackerrank|161256-622|faa76a548e2dce2ef37df6a68d4dc0c75bd760f3"
	r = requests.post("http://api.hackerrank.com/checker/submission.json", data = {
	    "source" : source,
	    "lang" : lang,
	    "testcases" : json.dumps([testcases]),
	    "api_key" : api_key
	})
	result = r.json()
	#if(result['result']['stdout'][0]!="")
	try:
		out=int(result['result']['stdout'][0][0])
	#out=out.replace(" ","")
	#std="["+'"'+out+'"'+"]"
	#std=std.replace(" ","")
		#testcases=int(testcases)
		output=int(output)
		
		if(output==out and int(result['result']['time'][0])<timeout):
			return HttpResponse("Output: "+result['result']['stdout'][0]+ "<br>" +"Compile Time: "+str(result['result']['time'][0])	)
		else:
			return HttpResponse("Expected Output :"+output+"<br>"+"Output:"+result['result']['stdout'][0])

	except TypeError:	
		
		return HttpResponse("Compile error:<br>"+result['result']['compilemessage'])
	except:
		return HttpResponse(output)	

