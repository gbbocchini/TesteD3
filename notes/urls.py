from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'notes'

urlpatterns = [
    path('', views.CreateNote.as_view(), name='create'),
    path('<username>/<pk>/', views.DetailNote.as_view(), name ='single'),
    path('list/', views.ListNote.as_view(), name='list'),
    path('delete/<username>/<pk>/', views.DeleteNote.as_view(), name='delete'),
    path('update/<username>/<pk>/', views.UpdateNote.as_view(), name='update'),

]