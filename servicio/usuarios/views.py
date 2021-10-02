from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import action

from usuarios.serializers import UserSerializer
from usuarios.models import User

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    #def create(self, request):
    #    pass

    #def update(self, request, pk=None):
    #    pass

    #def partial_update(self, request, pk=None):
    #    pass

    #def destroy(self, request, pk=None):
    #    pass

    @action(detail=False, methods=['put'])
    def update1(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            pass
            return Response(serializer.data)
