# Struktur form yang dapat menerima data Product baru

from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product 
        # model yang digunakan untuk form adalah Product
        # Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]