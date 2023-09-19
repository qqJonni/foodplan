from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    context = {
        'title': 'План питания на неделю, меню, рецепты, список покупок. Классическое меню, безуглеводное меню'
    }
    return render(request, 'food_card/index.html', context)


def recipe(request, id):
    recipe = get_object_or_404(Recipe.objects.prefetch_related('recipe_items', 'recipe_items__product'), id=id)
    recipe_details = {
        'title': recipe.title,
        'products': {}
    }
    calories = 0

    for recipe_item in recipe.recipe_items.all():
        recipe_details['products'].update({f'{recipe_item.product}': recipe_item.quantity})
        calories += (recipe_item.product.calories / 100) * recipe_item.quantity
    recipe_details['calories'] = calories

    return render(
        request,
        template_name=f'food_card/recipe.html',
        context={
            'title': 'План питания на неделю, меню, рецепты, список покупок. Классическое меню, безуглеводное меню',
            'recipe_details': recipe_details
        }
    )
