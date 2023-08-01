from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Skill, Project, Category
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    categories = Category.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body'] + f"\nEmail send form: {form.cleaned_data['email']}"
            email_from = settings.EMAIL_HOST_USER
            to = 'trantuan1902.tt@gmail.com'
            send_mail(subject, body, email_from, [to])
            form.save()
            return HttpResponseRedirect('/#contact')

    return render(request, 'base/home.html', {
        'projects': projects,
        'skills': skills,
        'categories': categories,
        'form': form,
    })