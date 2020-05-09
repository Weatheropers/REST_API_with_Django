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