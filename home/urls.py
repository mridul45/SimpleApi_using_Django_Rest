from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    # path('',home,name='home'),
	# path('student/',post_student,name='post_student'),
    # path('update-student/<id>/',update_student,name='update_student'),
    # path('delete-student/<id>/',delete_student,name='delete_student'),
    # path('get-book/',get_book),
    path('',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view()),
    path('generic-student/<id>/',StudentGeneric1.as_view()),
    path('generic-student/',StudentGeneric.as_view()),
]
