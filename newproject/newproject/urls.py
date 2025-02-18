
from django.contrib import admin
from django.urls import path
from newproject.view import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('reagistation/',reagistation,name='reagistation'),
]
