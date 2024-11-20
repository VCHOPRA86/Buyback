from django.urls import path
from . import views

urlpatterns = [
    path('revieworder/', views.revieworder, name='revieworder')
]