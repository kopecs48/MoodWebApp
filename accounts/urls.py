from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('post/', views.create_post, name="post"),
    path('mood/', views.post_list, name='mood'),
]