from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('liste_ideas/', views.IdeasListView.as_view(), name='liste_ideas'),
    path('idee_detail/<int:pk>',views.IdDetailView.as_view(), name="idee_detail"),
    path('vote/<str:id_user>', views.vote, name="vote"),
    path('creer_idees', views.creer_idee, name="creer"),
    path('idees_popu', views.idees_popu, name="idees_popu"),
    path('bets', views.bets_faits_view.as_view(), name="bets_faits"),
    path('creer_paris', views.creer_paris, name="creer_paris")
    # path('func_create/',views.FunctionalityCreateView.as_view(), name="func_create")
    # path('special/', views.special_view, name='special'),
    # path('signup/', views.SignupPage.as_view(), name='signup'),
    
]
  
  
