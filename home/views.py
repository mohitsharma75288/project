from django.shortcuts import render
# Create your views here.
from .models import question
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
def index(request):
	if request.method=='POST':
		name=request.POST["name"]
		age = request.POST["age"]
		gender=request.POST["gender"]
		subject=request.POST.getlist("subject")
		address=request.POST["address"]
		city=request.POST["city"]
		img = request.FILES["image"]
		fs=FileSystemStorage()
		filename=fs.save(img.name, img)


		dsobj=question()
		dsobj.name=name
		dsobj.dob=age
		dsobj.adress=address
		dsobj.hobbies=subject
		dsobj.gender=gender
		dsobj.city=city
		dsobj.aimage=img
		dsobj.save()

	context={}
	return render(request, 'home/index.html', context)

def display(request):
	latest_question_list=question.objects.all().order_by("id")
	context={'questionlist':latest_question_list}
	return render(request, 'home/home.html', context)


def deletefun(request,id):
	question.objects.filter(id=id).delete()
	latest_question_list=question.objects.all().order_by("name")
	context={'questionlist':latest_question_list}
	return render(request, 'home/home.html', context)
 
def editfunction(request,id):
    latest_question_list=question.objects.filter(id=id)
    context={'questionlist':latest_question_list}
    return render(request, 'home/index1.html', context) 


def updatefunction(request,id):
	if request.method ==POST:
		name=request.POS
	 


