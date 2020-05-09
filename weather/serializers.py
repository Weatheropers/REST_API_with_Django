from rest_framework import serializers
from .models import Gu0
from .models import Gu1
from .models import Gu2
from .models import Gu3
from .models import Gu4
from .models import Header


class Gu0Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gu0