from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'api'


router = DefaultRouter()

router.register('todolists', views.TodoList, basename='todolist')
urlpatterns = router.urls
