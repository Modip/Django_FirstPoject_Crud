from django.urls import path,include
from employeur import views

urlpatterns=[
    # path('', views.listEmployeur)
    path('', views.listEmployeur, name='employeurlist'),
    path('employeuradd', views.addEmployeur, name='employeuradd'),
    path('/deleteemployeur/<str:id>/', views.deleteEmployeur, name='deleteemployeur'),
    path('/editemployeur/<str:id>/', views.editEmployeur, name='editemployeur')


]
