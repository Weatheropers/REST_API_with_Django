from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Gu0
from .models import Gu1
from .models import Gu2
from .models import Gu3
from .models import Gu4
from .models import Header
from .serializers import Gu0Serializer
from .serializers import Gu1Serializer
from .serializers import Gu2Serializer
from .serializers import Gu3Serializer
from .serializers import Gu4Serializer
from .serializers import HeaderSerializer

# Create your views here.
@api_view(['GET'])
def hiAPI(request):
    return Response("Hi I'm Django REST framework!")


@api_view(['GET'])
def gu(request, number):
    if number == 0: totaldata = Gu0.objects.all()
    elif number == 1: totaldata = Gu1.objects.all()
    elif number == 2: totaldata = Gu2.objects.all()
    elif number == 3: totaldata = Gu3.objects.all()
    elif number == 4: totaldata = Gu4.objects.all()
    serializer = Gu0Serializer(totaldata, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def header(request):
    totaldata = Header.objects.all()
    serializer = HeaderSerializer(totaldata, many=True)
    return Response(serializer.data)
