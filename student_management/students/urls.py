from django.contrib import admin
from django.urls import path, include
from students import views  # Importing views from the students app

urlpatterns = [ 
    path('', views.base, name='base'),  
    path('list/', views.student_list, name='student-list'), 
    path('add/', views.student_add, name='student-add'),
path('edit/<int:pk>/', views.student_edit, name='student-edit'),  # Updated to include the pk
    path('delete/<int:pk>/', views.student_delete, name='student-delete'),
]
