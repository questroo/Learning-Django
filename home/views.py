from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context = {'name': 'Justin', 'poggers': 'yes'}
    return render(request, 'home.html', context)
    
def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        desc = request.POST['desc']
        contact = Contact(firstname=firstname, lastname=lastname, email=email, desc=desc)
        contact.save()
        print("data saved into db")

    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')