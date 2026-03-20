from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Enfant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=50)
    avatar = models.CharField(max_length=10, default='🧒')
    
    def __str__(self):
        return self.prenom

class Tache(models.Model):
    enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, related_name='taches')
    titre = models.CharField(max_length=100)
    icone = models.CharField(max_length=10, default='⭐')
    ordre = models.IntegerField(default=1)
    terminee = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.titre} - {self.enfant.prenom}"

class Session(models.Model):
    enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateTimeField(default=timezone.now)
    temps_total = models.IntegerField(default=0)
    terminee = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Session de {self.enfant.prenom} - {self.date}"
