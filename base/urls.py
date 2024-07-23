########### application ############

from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
   path('', views.index),
   path('test', views.test),
   path('login', TokenObtainPairView.as_view()),
   path('priverty', views.priverty),
   path('register', views.register),
   path('book_view', views.book_view),
   path('book_view/<int:id>', views.book_view),
]