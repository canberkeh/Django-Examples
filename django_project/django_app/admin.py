from django.contrib import admin
from .models import Crypto
# Register your models here.
class CryptoAdmin(admin.ModelAdmin):
    list_display = ['coin', 'symbol', 'category', 'publish']
    list_display_links = ['symbol', 'publish']
    list_filter = ['category', 'publish']
    search_fields = ['coin', 'symbol', 'category']
    list_editable = ['coin']
    class Meta():
        model = Crypto

admin.site.register(Crypto, CryptoAdmin)
