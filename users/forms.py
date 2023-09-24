from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User, Order


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLkForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'image')


# class OrderForm(forms.Form):
#     duration = forms.ModelChoiceField(queryset=Order.objects, label='Срок', widget=forms.Select(attrs={'class': 'form-select'}))
#     breakfast = forms.ModelChoiceField(queryset=Order.objects, label='Завтраки', widget=forms.Select(attrs={'class': 'form-select'}))
#     lunches = forms.ModelChoiceField(queryset=Order.objects, label='Обеды', widget=forms.Select(attrs={'class': 'form-select'}))
#     dinner = forms.ModelChoiceField(queryset=Order.objects, label='Ужины', widget=forms.Select(attrs={'class': 'form-select'}))
#     dessert = forms.ModelChoiceField(queryset=Order.objects, label='Десерты', widget=forms.Select(attrs={'class': 'form-select'}))
#     quantity = forms.ModelChoiceField(queryset=Order.objects, label='Кол-во персон', widget=forms.Select(attrs={'class': 'form-select'}))
#     allergies = forms.ModelChoiceField(queryset=Order.objects, label='Аллергии', widget=forms.CheckboxInput(attrs={'class': 'form-select'}))
#
#     class Meta:
#         model = Order
#         fields = ('duration', 'breakfast', 'lunches', 'dinner', 'dessert', 'quantity', 'allergies')
