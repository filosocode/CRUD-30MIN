from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer


# Create your views here.
class TareaViews(viewsets.ModelViewset):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
