from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout)
]
