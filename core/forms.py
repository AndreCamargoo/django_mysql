from django import forms
from django.core.mail.message import EmailMessage
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, min_length=3)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Sua mensagem', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\n E-mail: {email}\n Assunto: {subject}\n Messagem: {message}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema django',
            body=content,
            from_email='contato@seudominio.com.br',
            to=['andre.camargo@msn.com'],
            headers={'Reply-To': email},
        )
        mail.send()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image')
