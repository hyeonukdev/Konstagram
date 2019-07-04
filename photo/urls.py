from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo, Board

app_name = 'photo'

urlpatterns = [
    path('', photo_list,name='photo_list'),
    path('detail/<int:pk>/',DetailView.as_view(model=Photo,template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),

    path('board/', board,name='board'),
    path('detailboard/<int:pk>/',DetailView.as_view(model=Board,template_name='photo/detailcomment.html'), name='board_detail'),
    path('uploadboard/', BoardUploadView.as_view(), name='board_upload'),
    path('deleteboard/<int:pk>/', BoardDeleteView.as_view(), name='board_delete'),
    path('updateboard/<int:pk>/', BoardUpdateView.as_view(), name='board_update'),
]
