# Struktur form yang dapat menerima data Product baru

from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product 
        # model yang digunakan untuk form adalah Product
        # Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)