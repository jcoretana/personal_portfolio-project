from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.every_blogs, name='every_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]