from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
#app name is the pre-req url to get to these endpoints
#i.e.: 127.0.0.1:8000/accounts/login not just 127.0.0.1:8000/login
app_name = 'accounts'

#call the method from the views.py in this directory to run on the backend whenever this url is entered
urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('post/', views.create_post, name="post"),
    path('mood/', views.post_list, name='mood'),
]