from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("addarticle/", views.addarticle, name = "addarticle"),
    path("details/<int:id>/", views.details, name = "details"),
    path("update/<int:id>/", views.update, name = "update"),
    path("delete/<int:id>/", views.delete, name = "delete"),
    path("articles/", views.articles, name = "articles"),
    path("comment/<int:id>/", views.addComment, name = "comment"),    

    
]