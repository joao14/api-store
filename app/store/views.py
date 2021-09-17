from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from ..core.models import Store
from .serializers import StoreSerializers


# Create your views here.
class StoreViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin ):

    def list(self,request):
        stores = Store.objects.all()
        serializer = StoreSerializers(stores, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StoreSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
