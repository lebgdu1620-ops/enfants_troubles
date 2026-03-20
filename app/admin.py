from django.contrib import admin
from .models import Enfant, Tache, Session

class TacheInline(admin.TabularInline):
    model = Tache
    extra = 3

@admin.register(Enfant)
class EnfantAdmin(admin.ModelAdmin):
    list_display = ['prenom', 'avatar', 'user']
    inlines = [TacheInline]

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ['titre', 'icone', 'enfant', 'terminee', 'ordre']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['enfant', 'date', 'temps_total', 'terminee']
