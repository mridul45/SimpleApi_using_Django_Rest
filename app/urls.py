from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"todo-view-set",views.TodoViewSet, basename='todo')

urlpatterns = [
    path('',views.home,name='home'),
    path('get-todo/',views.get_todo,name='get_todo'),
    path('post-todo/',views.post_todo,name='post_todo'),
    path('todo/',views.TodoView.as_view()),
]


urlpatterns += router.urls