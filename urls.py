from django.urls import path
from . import views


urlpatterns=[
    path('logout/',views.logoutpage),
    path('',views.loginpage,name='loginurl'),
    path('signup',views.signup,name='signupurl'),
    path('home/',views.homepage,name='homeurl'),    
    path('first/',views.firstform,name='firsturl'),
    path('employee/',views.employeeform,name='employeeurl'),
    path('modelform/',views.employeemodelform,name='employeemodelurl'),
    path('selectemployee/',views.selectemployee,name='selectemployeeurl'),
    path('detailed/<int:eno>',views.detailedinfo,name='detailedurl'),

]