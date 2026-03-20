from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from app.models import Enfant, Tache, Session

def choisir_enfant(request):
    enfants = Enfant.objects.all()
    return render(request, 'enfant_app/choisir_enfant.html', {'enfants': enfants})

def taches_enfant(request, enfant_id):
    enfant = get_object_or_404(Enfant, id=enfant_id)
    taches = Tache.objects.filter(enfant=enfant)
    
    if request.method == 'POST':
        tache_id = request.POST.get('tache_id')
        tache = get_object_or_404(Tache, id=tache_id)
        tache.terminee = True
        tache.save()
        
        # Si toutes les tâches sont finies
        if not taches.filter(terminee=False).exists():
            Session.objects.create(
                enfant=enfant,
                date=timezone.now(),
                temps_total=0,
                terminee=True
            )
        return redirect('taches_enfant', enfant_id=enfant_id)
    
    return render(request, 'enfant_app/taches.html', {
        'enfant': enfant,
        'taches': taches,
        'toutes_finies': not taches.filter(terminee=False).exists()
    })

def recommencer(request, enfant_id):
    enfant = get_object_or_404(Enfant, id=enfant_id)
    Tache.objects.filter(enfant=enfant).update(terminee=False)
    return redirect('taches_enfant', enfant_id=enfant_id)

