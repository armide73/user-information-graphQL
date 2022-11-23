import graphene
from graphene_django import DjangoObjectType
from .models import user


class userType(DjangoObjectType):
    class Meta:
        model=user
        fields=('name','email','phone')


class Query(graphene.ObjectType):
    users=graphene.List(userType)

    def resolve_users(root,info):
        return user.objects.all()


class createUser(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        email=graphene.String(required=True)
        phone=graphene.String(required=True)    

    user=graphene.Field(userType) 

    @classmethod
    def mutate(cls,root,info,name,email,phone):
        user1=user(
            name=name,
            email=email,
            phone=phone
        )  
        user1.save()
        return createUser(user=user1)   

class Mutation(graphene.ObjectType):
    userCreation=createUser.Field()     

schema = graphene.Schema(query=Query, mutation=Mutation)            