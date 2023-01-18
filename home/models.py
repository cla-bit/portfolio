from django.db import models
from django.urls import reverse
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Skills(models.Model):
    skills = models.CharField(max_length=100, blank=True, null=False)
    value_max = models.PositiveSmallIntegerField(default=0)
    value_min = models.PositiveSmallIntegerField(default=0)
    intro = models.TextField(blank=True, null=False)

    class Meta:
        indexes = [
            models.Index(fields=('skills',))
        ]
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skills

    def get_absolute_url(self):
        return reverse('home:home')


class Services(models.Model):
    intro = models.TextField(blank=True, null=False)
    services = models.CharField(max_length=100, blank=True, null=False)
    description = models.CharField(max_length=100, blank=True, null=False)
    fiver_url = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    upwork_url = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)

    class Meta:
        indexes = [
            models.Index(fields=('services',))
        ]
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.services

    def get_absolute_url(self):
        return reverse('home:home')


class Portfolio(models.Model):
    about_me = models.TextField(blank=True, null=False)
    job_position = models.CharField(max_length=100, blank=True, null=False)
    website_link_on = models.BooleanField(default=False)
    website = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=30, blank=True, null=False)
    git_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    email = models.EmailField()
    freelance_on = models.BooleanField(default=False)
    freelance = models.CharField(max_length=30, blank=True, null=True)
    little_description = models.TextField(blank=True, null=False)
    facts = models.TextField(blank=True, null=False)
    skills = models.ManyToManyField(Skills, related_name='portfolio_skills')
    cv = models.FileField(upload_to='resume')
    services = models.ManyToManyField(Services, related_name='portfolio_services')
    linkedin_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    github_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    total_projects = models.PositiveSmallIntegerField(default=0)
    total_clients = models.PositiveSmallIntegerField(default=0)
    service_hour = models.PositiveSmallIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=('job_position', 'website',)),
            models.Index(fields=('phone_number', 'city',)),
        ]
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home:home')


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:home')


class Project(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    name_slug = models.SlugField(max_length=50, blank=True, null=False)
    git_url_on = models.BooleanField(default=False)
    git_url = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    video_link_on = models.BooleanField(default=False)
    video_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    date_done = models.DateField(auto_now_add=True)
    detail = models.TextField(blank=True, null=False)
    small_img = models.ImageField(upload_to='project_small', null=True)
    big_img = models.ImageField(upload_to='project_big', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='project_categories')
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:project_detail', args=[self.name_slug])


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Your Name')
    email = models.EmailField(null=True, verbose_name='Your Email')
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name

    def send_email(self, email):
        try:
            self.email = Contact.objects.filter(email=email).last()
            template = render_to_string('email_sending.html', {'Name': self.email, 'Email': self.email.email})
            email_send = EmailMessage(
                'Message Notification',
                template,
                settings.EMAIL_HOST_USER,
                [self.email.email],
            )
            email_send.send(fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid Header found')
        return HttpResponseRedirect(reverse('home:contact'))

