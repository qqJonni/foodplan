from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        'Название',
        max_length=300,
        db_index=True
    )
    recipe_items = models.ManyToManyField(
        'RecipeItems',
        related_name='recipes'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Рецепты'
        verbose_name = 'Рецепт'


class RecipeItems(models.Model):
    product = models.ForeignKey(
        'Product',
        related_name='in_recipe_items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('Количество (грамм)')

    def __str__(self):
        return f'{self.product} ({self.quantity}г.)'

    class Meta:
        verbose_name_plural = 'Ингредиенты'
        verbose_name = 'Ингредиент'


class Product(models.Model):
    title = models.CharField(
        'Название',
        max_length=200,
        db_index=True
    )
    calories = models.PositiveIntegerField('Калорийность (на 100г.)')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'
