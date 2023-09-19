from django.urls import path
from food_card.views import index, recipe


urlpatterns = [
    path("", index, name='index'),
    path("recipe<int:id>/", recipe, name='recipe')
]
