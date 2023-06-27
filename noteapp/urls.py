from django.urls import path 
from . import views 

urlpatterns =[
    path('',views.note_list),
    path('notes/<int:pk>',views.note_particular),
    path('create',views.note_create),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),

]