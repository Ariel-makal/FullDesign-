from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
from .models import Product, Category

def home(request):
    products = Product.objects.filter(is_active=True)[:8]  # Limite à 8 produits par exemple
    return render(request, "home/home.html", {"products": products})


def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query, is_active=True) if query else []
    return render(request, 'search/search_results.html', {'results': results, 'query': query})


def ensembles(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('categorie', 'all')
    if selected_category == 'all':
        products = Product.objects.filter(is_active=True)
    else:
        products = Product.objects.filter(is_active=True, category__slug=selected_category)
    return render(request, 'ensembles/ensembles.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    })

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        numero = request.POST.get('numero')
        commentaire = request.POST.get('commentaire')

        # Contenu de l'e-mail
        subject = f"Message de {nom} via le formulaire de contact via le site web FullDesign"
        message_body = f"Nom : {nom}\nEmail : {email}\nTéléphone : {numero}\n\nMessage : {commentaire}"

        try:
            send_mail(
                subject,
                message_body,
                'makalyav6@gmail.com',  # Adresse e-mail de l'expéditeur
                ['makalyav6@gmail.com'],  # Adresse e-mail du destinataire
                fail_silently=False,
            )
            messages.success(request, "Votre message a été envoyé avec succès.")
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite : {e}")
    return render(request, 'contact/contact.html')
