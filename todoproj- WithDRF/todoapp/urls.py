from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="Home"),
    path('<str:pk>',views.details,name='detail'),
    path('create/',views.create,name='Create'),
    path('update/<str:pk>',views.update,name='Update'),
    path('delete/<str:pk>',views.delete,name='Delete')
]
