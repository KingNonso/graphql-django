import graphene
from graphene_django import DjangoObjectType
from graphql_auth.decorators import verification_required



class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'dob', 'is_active')






