from django.shortcuts import render
from rest_framework import viewsets, generics

from django.db.models import Q

from .models import User, Garage, Asset
from .serializers import UserSerializer, GarageSerializer, AssetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GarageViewSet(viewsets.ModelViewSet):
    # queryset = Garage.objects.all()
    serializer_class = GarageSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Garage.objects.all()
        query = self.request.GET.get("asset")
        if query:
            queryset = queryset.filter(Q(asset=None))
        return queryset

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer