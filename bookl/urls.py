#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'bookl'

urlpatterns = [
    # Create a task
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('createauth/', views.AuthorCreateView.as_view(), name='author_create'),
    # Retrieve task list
    path('', views.BookListView.as_view(), name='book_list'),
    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book_detail'),
    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.BookUpdateView.as_view(), name='book_update'),
    # re_path(r'^(?P<pk>\d+)/updateauth/$', views.AuthorUpdateView.as_view(), name='author_update'),
    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.BookDeleteView.as_view(), name='book_delete'),
    # re_path(r'^(?P<pk>\d+)/deleteauth/$', views.AuthorDeleteView.as_view(), name='author_delete')

    # # Create a task
    # path('create/', views.task_create, name='task_create'),
    # # Retrieve task list
    # path('', views.task_list, name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

]