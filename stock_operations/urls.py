from django.urls import path
from . import views

urlpatterns = [

    path("", views.home,name="home" ),
    path("recently-searched", views.recently_searched_stocks,name="recently_searched_stocks" ),
]