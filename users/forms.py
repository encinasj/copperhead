#Django
from django import forms
#ours models
from django.contrib.auth.models import User
from users.models import Profile, Remplacement

class RegisterForm(forms.Form):
    #Signup Forms, this classs is for register user with profile 
    username = forms.CharField(min_length=4, max_length=20,required=True, 
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Usuario',
                                'autocomplete': 'off',
                                }))
    password = forms.CharField(max_length=70, required=True, 
                            widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Contraseña',
                                'autocomplete': 'off',
                                }))
    password_confirmation = forms.CharField(max_length=70, required=True, 
                            widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Confirmar contraseña',
                                'autocomplete': 'off',
                                }))

    first_name = forms.CharField(min_length=2, max_length=50, required=True,
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Nombres',
                                'autocomplete': 'off',
                                }))
    last_name = forms.CharField(min_length=2, max_length=50, required=True,  
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Apellidos',
                                'autocomplete': 'off',
                                }))
    email = forms.EmailField(min_length=6, max_length=30, required=False, 
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Correo',
                                'autocomplete': 'off',
                                }))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput())

    def clean_username(self):
        #Username must be unique.
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Nombre de usuario en uso.')
        return username

    def clean(self):
        #verify password conformation match.
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('La contraseña no coincide.')
        return data

    def save(self):
        #Create user and profile.
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    #Profile forms    
    phone_number = forms.CharField(max_length=20, required=False)
    biography = forms.CharField(max_length=500, required=False)
    picture = forms.ImageField()

class RemplacementForm(forms.ModelForm):
    #remplacement article
    model = Remplacement

    fields = (
        "remplacement"
    )

    labels = {
        "remplacement":""
    }