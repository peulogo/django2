from django.shortcuts import render

from task1.forms import UserRegister
from task1.models import Game, Buyer


# Create your views here.

def main_view(request):
    return render(request, 'fourth_task/index.html')


def games_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart_view(request):
    return render(request, 'fourth_task/cart.html')

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка условий
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Сохранение нового пользователя в базу данных
                Buyer.objects.create(name=username, balance=0.0, age=age)
                info['success'] = f'Приветствуем, {username}!'
                form = UserRegister()  # Сброс формы после успешной регистрации

        info['form'] = form
    else:
        info['form'] = UserRegister()  # Пустая форма при GET запросе

    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()
        age = request.POST.get('age', '').strip()

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif not age.isdigit() or int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        else:
            # Сохранение нового пользователя в базу данных
            Buyer.objects.create(name=username, balance=0.0, age=int(age))
            info['success'] = f'Приветствуем, {username}!'

    return render(request, 'fifth_task/registration_page.html', info)
