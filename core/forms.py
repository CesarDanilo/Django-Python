from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto, Cliente


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'''
                Nome: {nome}\n
                E-mail: {email}\n
                Assunto: {assunto}\n
                Mensagem: {mensagem}\n
            '''

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema Django_web01!',
            body=conteudo,
            from_email='contato@gmail.com',
            to=['contato@gmail.com'],
            headers={'Replay-To': email},
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']


class ClientesModelsForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'sexo', 'email']
