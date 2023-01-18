from django.urls import path
from .views import home, project_view


app_name = 'home'

urlpatterns = [
    path('', home, name="home"),
    # path('download-cv/<str:filename>/', download_cv, name='download'),
    path('category', home, name='category'),
    path('about/', home, name='about'),
    path('resume/', home, name='resume'),
    path('portfolio/', home, name='portfolio'),
    path('services/', home, name='services'),
    path('contact/', home, name='contact'),
    path('project-view/<slug:slug>', project_view, name='project_detail'),
]