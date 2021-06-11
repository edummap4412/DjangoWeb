from django.contrib import admin
from .models import  ProdutosModel


@admin.register(ProdutosModel)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo', 'descricao' )
