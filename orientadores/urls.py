from django.urls import path
from django.contrib.auth.urls import views as auth_views
from .views import SignUp

urlpatterns = [

path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/', SignUp.as_view(), name='signup'),

]