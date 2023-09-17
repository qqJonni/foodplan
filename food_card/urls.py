from django.urls import path
from food_card.views import index


urlpatterns = [
    path("", index, name='index'),
]