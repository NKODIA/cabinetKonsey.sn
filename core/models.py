from django.db import models

# Create your models here.
from django.db import models

class OffreEmploi(models.Model):
    titre = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    profil_recherche = models.TextField()
    date_limite = models.DateField()
    slug = models.SlugField(unique=True)
    publie = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

class Candidature(models.Model):
    offre = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True)
    cv = models.FileField(upload_to="cvs/")
    date_postulation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)  # <- ici
    author = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titre

    
class Page(models.Model):
    LANG_CHOICES = [
        ('fr', 'Français'),
        ('en', 'Anglais'),
    ]
    titre = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    contenu = models.TextField()
    langue = models.CharField(max_length=2, choices=LANG_CHOICES)

    def __str__(self):
        return f"{self.titre} ({self.langue})"