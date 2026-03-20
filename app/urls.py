from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_login, name='login'),
    path('taches/', views.page_taches, name='taches'),
    path('cocher/<int:tache_id>/', views.cocher_tache, name='cocher_tache'),
    path('relancer/', views.relancer_taches, name='relancer'),
    path('recompense/', views.page_recompense, name='recompense'),
    path('logout/', views.page_logout, name='logout'),
]
