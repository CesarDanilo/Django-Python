from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug',
                    'criado', 'modificado', 'ativo')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'email',
                    'slug', 'criado', 'modificado', 'ativo')
