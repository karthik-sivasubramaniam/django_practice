from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<str:slug>', views.blogpost),
    path('<str:slug>/update/', views.update_post),
    path('<str:slug>/delete/', views.delete_post),
]