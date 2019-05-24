import graphene
from .query import Queries
# from .mutation import Mutations
# from categories.queries import Query
from categories.mutations import Mutation

# schema = graphene.Schema(query=Queries, mutation=Mutations)
schema = graphene.Schema(query=Queries, mutation=Mutation)
