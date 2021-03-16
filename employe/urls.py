from django.urls import path
from employe import views

urlpatterns = [
    path('', views.listEmploye, name='employelist'),
    path('addEmploye', views.addEmploye, name = 'addEmploye'),
    path('deleteemploye/<str:id>/', views.deleteEmploye, name ='deleteemploye'),
    path('editemploye/<str:id>/', views.editEmploye, name = 'editemploye')
]
