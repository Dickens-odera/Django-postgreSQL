from django.conf.urls import url
from django.urls import path,include
from students.views import Student

urlpatterns = [
    url('', Student.as_view(), name="student-index" ),
    
]