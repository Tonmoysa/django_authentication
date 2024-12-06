from django.urls import path
from login_app import views

app_name='login_app'

urlpatterns = [
    path('' ,views.index, name='index')
    
]
