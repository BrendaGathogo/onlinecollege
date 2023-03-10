from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def courses(request):
    return render(request,'courses.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)






