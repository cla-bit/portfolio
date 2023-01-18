from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Project, Category, Contact, Portfolio, Services, Skills
from .forms import ContactForm
from django.contrib import messages
import mimetypes
import os
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    now = timezone.now()
    contact_form = ContactForm()
    categories = Category.objects.all()
    services = Services.objects.all()
    skill1 = Skills.objects.all()[:4]
    skill2 = Skills.objects.all()[4:]
    portfolio = Portfolio.objects.all()
    webscraping = categories.get(name='Web Scraping')
    webapps = categories.get(name='Web Apps')
    web_script = categories.get(name='Python Scripting')
    projects = Project.objects.all().filter(done=True)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request, 'Your message has been sent. Thank you!')
            send_contact_email = Contact()
            send_contact_email.send_email(email)
            return redirect('home:home')

        else:
            return render(request, "home.html", form)
    else:
        context = {
            'now': now,
            'categories': categories,
            'projects': projects,
            'webapps': webapps,
            'webscraping': webscraping,
            'scripting': web_script,
            'form': contact_form,
            'services': services,
            'skill1': skill1,
            'skill2': skill2,
            'portfolio': portfolio,
        }
        return render(request, "home.html", context)


def project_view(request, slug):
    now = timezone.now()
    project = Project.objects.get(name_slug=slug)
    context = {
        'now': now,
        'project': project,
    }
    return render(request, "detail.html", context)


# def download_cv(request, filename=''):
#     context = {}
#     if filename != '':
#         base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         filename = 'Peter_Claver_CV_new.pdf'
#         filedirectory = '/media/resume/'
#         filepath = base_dir + filedirectory + filename
#         file_path = open(filepath, 'r')
#         mime_type, _ = mimetypes.guess_type(filepath)
#         response = HttpResponse(file_path, content_type=mime_type)
#         response['Content-Disposition'] = f"attachment; filename={filename}"
#         return response
#     else:
#         return render(request, "home.html", context)
