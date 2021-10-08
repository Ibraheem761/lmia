from django.shortcuts import render
from home.models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, subject, message) 
        ins = Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
        messages.success(request, "Merci ! Votre message a été bien envoyé.")
        return render(request, 'home.html', {})


    else:
        return render(request, 'home.html', {})



def equipe(request):
    return render(request, 'equipe.html', {})