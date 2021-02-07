from django.urls import path, include
from rest_framework import routers
from .views import RequirementsViewSet, index
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('requirements', RequirementsViewSet, basename='requirements')

urlpatterns = [
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls)),
    path('', views.index, name='index'),
    #path('viewset/', views.viewset, name='viewset'),
    #path('list/', req_list),
    #path('list/', RequirementsAPIView.as_view()),
    #path('detail/<int:pk>/', req_detail),
    #path('detail/<int:id>/', RequirementsDetails.as_view()),
    #path('generic/<int:id>/', GenericAPIView.as_view()),
]