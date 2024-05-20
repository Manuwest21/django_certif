from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    
    path('', views.home, name='home'),
    path('view', views.logina, name='view'),
    path('logout/', views.logout_user, name='logout'),
    path('homes/', views.homes, name='homes'),
    path('accounts/login/', views.LoginPageView.as_view(), name='login'),
    path('signup/', views.signup_page, name='signup'),
    # path('about/', views.about, name='about'),
    # path('special/', views.special_view, name='special'),
    # path('signup/', views.SignupPage.as_view(), name='signup'),
  
    
# urlpatterns = [
#     path('', LoginView.as_view(
#             template_name='authentication/login.html',
#             redirect_authenticated_user=True),
#         name='login'),
#     path('logout/', authentication.views.logout_user, name='logout'),
# ]
]