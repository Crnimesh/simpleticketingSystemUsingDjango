from django.shortcuts import render
from django.http import HttpResponse
from .models import Tickets
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
# Create your views here.
def FirstPageController(request):
    return HttpResponse("<h1>My First Django Project Page</h1>")

def IndexPageController(request):
    return HttpResponse("<h1>This is index page</h1>")

def HtmlPageController(request):
	return render(request,"htmlpage.html")

def HtmlPageControllerWithData(request):
	data1= "this is data 1 pasing to HTML page"
	data2= "this is data 2 pasing to HTML page"
	return render (request, "htmlpage_with_data.html",{'data': data1,'data1': data2})

def PassingDatatoController(request,url_data):
	return HttpResponse("<h2>This is data coming Via URL: "+url_data)

def addData(request):
	return render(request, "add_data.html")

def add_tickets(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Now Allowed</h2>")
    else:
    	file=request.FILES['profile']
    	fs=FileSystemStorage()
    	profile_img=fs.save(file.name,file)
    	try:
    		tickets=Tickets(name=request.POST.get('name',''),email=request.POST.get('email',''),address=request.POST.get('address',''),movie_id=request.POST.get('movie_id',''),desc=request.POST.get('desc',''),profile_image=profile_img)
    		tickets.save()
    		messages.success(request,"Hurry!Ticket Booked Successfully!!!")
    	except: 
    		messages.error(request,"Failed To Booked Your Ticket At This Moment!!!")
    	return HttpResponseRedirect("/addData")