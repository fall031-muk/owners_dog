#from django.shortcuts import render
# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog


class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name=data['owner'],
            email=data['owner_email'],
            age=data['owner_age']
        )
        return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dog_list = []
            results.append(
                {
                    "owner": owner.name,
                    "owner_email": owner.email,
                    "owner_age": owner.age,
                    "dog_list": dog_list
                }
            )
            dogs = owner.dog_set.all()
            for dog in dogs:
                dog_list.append(
                    {
                        "dog_name": dog.name,
                        "dog_age": dog.age,
                    }
                )

        return JsonResponse({'results': results}, status=200)

    # def get(self, request):
    #     owners = Owner.objects.all()

    #     results = []
    #     for owner in owners:
    #         dogs = owner.dog_set.values()
    #         results.append(
    #             {
    #                 "owner": owner.name,
    #                 "owner_email": owner.email,
    #                 "owner_age": owner.age,
    #                 "dog_list": dogs.name,
    #             }
    #         )
    #     return JsonResponse({'results': results}, status=200)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            owner_id=data['owner_id'],
            name=data['dog'],
            age=data['dog_age']
        )
        return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "owner": dog.owner.name,
                    "dog": dog.name,
                    "dog_age": dog.age
                }
            )
        return JsonResponse({'results': results}, status=200)
