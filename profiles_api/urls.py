from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet

# This is how you register URLs for ViewSets i.e., using routers
router = DefaultRouter()
router.register('hello_viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls)),

]
