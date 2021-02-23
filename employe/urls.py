from django.urls import path,include
from employe import views

urlpatterns=[
    # path('', views.home),
    path('', views.listEmploye, name='employelist'),
    path('addEmploye', views.addEmploye,name = 'addEmploye'),
    path('employedelete', views.addEmploye,name = 'employedelete')
,
]
