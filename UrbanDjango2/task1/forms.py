from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={"placeholder": "Введите логин"})
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль"})
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=999,
        label="Введите свой возраст",
        widget=forms.NumberInput(attrs={"placeholder": "Введите ваш возраст"})
    )


