from django.shortcuts import render


def index(requst):
    return render(requst, 'mainApp/homePage.html')


def contacts(request):
    return render(
        request, 'mainApp/basic.html', {
            'valuses': ['Если у ваc остались вопросы - звоните', '+71234567899']
        }
    )

