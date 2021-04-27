import graphene

from graphql_auth.schema import UserQuery, MeQuery

from accounts.graphql.mutations.authentication import AuthMutation


class AccountsQuery(UserQuery, MeQuery, graphene.ObjectType):
    pass


class AccountsMutation(AuthMutation, graphene.ObjectType):
    pass



