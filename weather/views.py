from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Gu0
from .models import Gu1
from .models import Gu2
from .models import Gu3
from .models import Gu4
from .models import Header
from .serializers import Gu0Serializer

# Create your views here.
@api_view(['GET'])
def hiAPI(request):
    return Response("Hi I'm Django REST framework!")


@api_view(['GET'])
def gu_0(request):
    totaldata = Gu0.objects.all()
    serializer = Gu0Serializer(totaldata, many=True)
    return Response(serializer.data)