from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewsSet

router = DefaultRouter()
router.register(r"tareas", TareaViewsSet)


urlpatterns = [
    path("", include(router.urls)),
]
