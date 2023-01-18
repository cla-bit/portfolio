from django.contrib.sitemaps import Sitemap
from django.contrib import sites
from .models import Portfolio, Skills, Services, Project, Category
from django.urls import reverse


class PortfolioSitemap(Sitemap):
    def items(self):
        return ['home:home']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()


class SkillSitemap(Sitemap):
    def items(self):
        return ['home:home']

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    def items(self):
        return ['home:home']

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    def items(self):
        return ['home:home']

    def location(self, item):
        return reverse(item)
