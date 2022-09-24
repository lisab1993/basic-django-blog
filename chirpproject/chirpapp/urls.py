from django.urls import path
from . import views

app_name = 'chirpapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('show_edit/<int:id>/', views.show_edit, name='show_edit'),
    path('submit_edit/<int:id>/', views.submit_edit, name='submit_edit'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post')
]
