from django.urls import path
from . import views

urlpatterns = [
    path('', views.choisir_enfant, name='choisir_enfant'),
    path('enfant/<int:enfant_id>/', views.taches_enfant, name='taches_enfant'),
    path('enfant/<int:enfant_id>/recompense/', views.recompense, name='recompense'),
    path('enfant/<int:enfant_id>/recommencer/', views.recommencer, name='recommencer'),
]
