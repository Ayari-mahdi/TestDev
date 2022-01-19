from django.urls import path
from . import views

# URLConf
urlpatterns = [

    path('GetArticles/', views.getapi),
    path('AddArticle/', views.addapi),



    ]