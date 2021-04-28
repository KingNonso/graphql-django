import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery

from accounts.graphql.schema import AccountsMutation
from book.models import Category, Ingredient
from links import schema as links


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'ingredients')


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'notes', 'category')


class BookQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_ingredients = graphene.List(IngredientType)
    all_category = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # we can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_all_category(root, info):
        # we can easily optimize query count in the resolve method
        return Category.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class Query(links.Query, BookQuery, UserQuery, MeQuery, graphene.ObjectType):
    pass


class CategoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        text = graphene.String(required=True)

    # The class attributes define the response of the mutation
    create = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, text):
        name = Category.objects.create(name=text)
        # Notice we return an instance of this mutation
        return CategoryMutation(create=name)


# class CreateIngredient(graphene.Mutation):
#     name = graphene.String()
#     category = graphene.Int()
#
#     class Arguments:
#         notes = graphene.String()


class Mutation(AccountsMutation, links.Mutation, graphene.ObjectType):
    new_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
