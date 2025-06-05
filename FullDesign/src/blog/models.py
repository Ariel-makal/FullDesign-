from django.db import models
from authenticate.models import CustomUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom de la catégorie")
    image = models.ImageField(upload_to='category/', blank=True, null=True, verbose_name="Image de la catégorie")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du produit")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Catégorie", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.PositiveIntegerField(verbose_name="Stock disponible")
    image_1 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Image du produit 1")
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Image du produit 2")
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Image du produit 3")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    is_active = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)  # L'utilisateur qui passe la commande
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,null=True)
    address = models.TextField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return f"Commande de {self.id} - {self.user.username} fc"
