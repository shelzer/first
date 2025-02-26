from django.shortcuts import render

data = {
        'title' : 'Главная страница',
        'values' : ['Some', 'Hello', '123'],
        'obj' : {
            'car' : 'BMW',
            'age' : '18',
            'hobby' : 'Football'
        }
    }

def homepage(request):
    return render(request, 'main/homepage.html', data)

def about(request):
    return render(request, 'main/about.html', data)

def contacts(request):
    return render(request, 'main/contacts.html', data)