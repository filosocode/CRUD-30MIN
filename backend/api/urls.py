from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet  # ← Correcto

router = DefaultRouter()
router.register(r"tareas", TareaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
