from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home'
    }
    return render(request, 'main/index.html', data)


def contacts(request):
    data = {
        'title': 'Contacts'
    }
    return render(request, 'main/contacts.html',data)


def about(request):
    data = {
        'title': 'About me'
    }
    return render(request, 'main/about.html', data)
