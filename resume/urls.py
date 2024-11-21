from django.urls import path
from . import views

urlpatterns = [
   path("",views.home,name="home"),
   path("about/", views.about,name="about"),
   path("experience/", views.experience,name="experience"),
   path("education/", views.education,name="education"),
   path("publications/", views.publications,name="publications"),
   path("skills/", views.skills,name="skills"),
   path("projects/", views.projects,name="projects"),
   path("awards/", views.awards,name="awards")
   
   
]
