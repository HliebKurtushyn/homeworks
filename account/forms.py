from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com',
        })
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Ім'я",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введіть ваше ім'я"
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Прізвище",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введіть ваше прізвище"
        })
    )

    age = forms.IntegerField(
        min_value=12,
        max_value=18,
        required=True,
        label="Вік",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Введіть ваш вік"
        })
    )

    phone = forms.CharField(
        max_length=15,        
        required=True,
        label="Телефон",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введіть ваш номер телефону"
        })
    )


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_without_plus = phone.lstrip('+')

        if not phone.startswith('+380') and not phone.startswith('0'):
            raise forms.ValidationError("Номер телефону повинен починатися з '+380' або '0'.")
        
        if not phone_without_plus.isdigit():
            raise forms.ValidationError("Номер телефону повинен містити лише цифри.")

        return phone

    
    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введіть пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Підтвердіть пароль'})


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user


class StudentAuthForm(AuthenticationForm):
    username = forms.EmailField(label="Email") # Зробив логін через email, тому що username в користувача не існує
