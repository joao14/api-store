from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import StoreViewSet

router = DefaultRouter()

app_name = 'store'

urlpatterns = [
    path('store', StoreViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

]
