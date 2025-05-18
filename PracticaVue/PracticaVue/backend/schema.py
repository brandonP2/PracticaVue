import graphene
from models import products

class ProductType(graphene.ObjectType):
    id          = graphene.Int()
    nombre      = graphene.String()
    precio      = graphene.Float()
    stock       = graphene.Int()
    disponible  = graphene.Boolean()

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info):
        return products

class IncrementStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    product = graphene.Field(ProductType)
    ok      = graphene.Boolean()

    def mutate(self, info, id):
        p = next((x for x in products if x["id"] == id), None)
        if not p:
            return IncrementStock(product=None, ok=False)
        p["stock"] += 1
        p["disponible"] = p["stock"] > 0
        return IncrementStock(product=p, ok=True)

class DecrementStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    product = graphene.Field(ProductType)
    ok      = graphene.Boolean()

    def mutate(self, info, id):
        p = next((x for x in products if x["id"] == id), None)
        if not p:
            return DecrementStock(product=None, ok=False)
        if p["stock"] > 0:
            p["stock"] -= 1
        p["disponible"] = p["stock"] > 0
        return DecrementStock(product=p, ok=True)

class Mutation(graphene.ObjectType):
    increment_stock = IncrementStock.Field()
    decrement_stock = DecrementStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
