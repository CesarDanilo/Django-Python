from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
# Create your views here.
from .forms import ProdutoModelForm, ClientesModelsForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()

        else:
            messages.error(request, 'Erro ao enviar o E-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'erro ao salvar o produto')
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }

    return render(request, 'produto.html', context)


def cliente(request):
    if str(request.method) == 'POST':
        form = ClientesModelsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Cadastrado com sucesso')
            form = ClientesModelsForm()
        else:
            messages.error(request, 'erro no cadastro')
    else:
        form = ClientesModelsForm()

    context = {
        'form': form
    }
    return render(request, 'cliente.html', context)
