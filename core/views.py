from django.shortcuts import render, get_object_or_404, redirect
from .models import OffreEmploi, Article  # Article doit venir de core.models
from .forms import CandidatureForm 
from django.urls import path
from . import views # À créer si pas déjà fait

def offres_detail(request, slug):
    offre = get_object_or_404(OffreEmploi, slug=slug)
    success = False
    if request.method == "POST":
        form = CandidatureForm(request.POST, request.FILES)
        if form.is_valid():
            candidature = form.save(commit=False)
            candidature.offre = offre
            candidature.save()
            success = True
            form = CandidatureForm()  # Réinitialiser le formulaire après succès
    else:
        form = CandidatureForm()
    return render(request, "core/offres_detail.html", {
        "offre": offre,
        "form": form,
        "success": success,
    })
    
def offres_list(request):
    offres = OffreEmploi.objects.filter(publie=True).order_by('-date_limite')
    return render(request, 'core/offres_list.html', {'offres': offres})

def about(request):
    return render(request, "core/about.html")

def services(request):
    return render(request, "core/services.html")

def contact(request):
    return render(request, "core/contact.html")

def mentions_legales(request):
    return render(request, "core/mentions_legales.html")

def home(request):
    return render(request, "core/home.html")

def articles_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, "core/articles_list.html", {"articles": articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "core/article_detail.html", {"article": article})

def contact(request):
    service = request.GET.get('service', '')  # récupère le service choisi
    context = {
        'service': service
    }
    return render(request, 'core/contact.html', context)
