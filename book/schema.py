import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from book.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ('name', 'ingredients')
        interfaces = (graphene.relay.Node,)


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    category = graphene.relay.Node.Field(CategoryNode)
    all_category = DjangoFilterConnectionField(CategoryNode)

    ingredient = graphene.relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)


