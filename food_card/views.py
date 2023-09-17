from django.shortcuts import render


def index(request):
    context = {
        'title': 'План питания на неделю, меню, рецепты, список покупок. Классическое меню, безуглеводное меню'
    }
    return render(request, 'food_card/index.html', context)
