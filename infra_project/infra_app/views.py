from django.http import HttpResponse


def index(request):
    return HttpResponse('Тестим и смотрим кто тут у нас КРАСАВЧИК)))!')


def second_page(request):
    return HttpResponse('А это вторая страница')
