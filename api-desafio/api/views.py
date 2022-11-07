from api.models import User
from django.contrib.auth.models import User as DjangoUser
from rest_framework import viewsets, filters, permissions
from api.serializers import UserSerializer
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-born_date')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


    def create(self, request):
        try:
            user = User()
            user.name = request.data['name']
            user.born_date = request.data['born_date']
            user.register = self.autoincrement()

            du = DjangoUser()
            du.email = request.data['email']
            du.username = request.data['email']
            du.set_password(request.data['password'])
            du.save()

            user.django_user = du
            user.save()

        except Exception as e:
            return HttpResponse(
                str(e), 
                content_type='text/plain', 
                status=500
            )

        return HttpResponse(status=200)

    def update(self, request, pk):
        try:
            user = User.objects.get(register = pk)
            user.name = request.data['name']
            user.born_date = request.data['born_date']

            user.django_user.email = request.data['email']
            user.django_user.username = request.data['email']
            user.django_user.set_password(request.data['password'])

            user.django_user.save()
            user.save()

        except Exception as e:
            return HttpResponse(
                str(e), 
                content_type='text/plain', 
                status=500
            )

        return HttpResponse(status=201)

    def autoincrement(self):
        no = User.objects.count()
        if no == None:
            return 1000
        else:
            return no + 1
