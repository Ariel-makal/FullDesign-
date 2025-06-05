from django.urls import path
from blog.views import home, contact, search, ensembles
urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path('recherche/', search, name='search'),
    path('ensembles/', ensembles, name='ensembles'),
]