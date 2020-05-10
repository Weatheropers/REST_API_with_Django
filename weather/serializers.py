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
        fields = ('num', 'gu', 'time_difference', 'hour', 'temp', 'day_high_temp', 'day_low_temp', 'sky_state', 
        'weather_state', 'weather_kor', 'rain_persent', 'expect_rain_6h', 'expect_rain_12h', 'expect_snow_6h', 
        'expect_snow_12h', 'wind_speed', 'wind_way', 'wind_text', 'humi', 'fine_dust', 'small_fine_dust')

class Gu1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gu1
        fields = ('num', 'gu', 'time_difference', 'hour', 'temp', 'day_high_temp', 'day_low_temp', 'sky_state', 
        'weather_state', 'weather_kor', 'rain_persent', 'expect_rain_6h', 'expect_rain_12h', 'expect_snow_6h', 
        'expect_snow_12h', 'wind_speed', 'wind_way', 'wind_text', 'humi', 'fine_dust', 'small_fine_dust')

class Gu2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gu2
        fields = ('num', 'gu', 'time_difference', 'hour', 'temp', 'day_high_temp', 'day_low_temp', 'sky_state', 
        'weather_state', 'weather_kor', 'rain_persent', 'expect_rain_6h', 'expect_rain_12h', 'expect_snow_6h', 
        'expect_snow_12h', 'wind_speed', 'wind_way', 'wind_text', 'humi', 'fine_dust', 'small_fine_dust')

class Gu3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gu3
        fields = ('num', 'gu', 'time_difference', 'hour', 'temp', 'day_high_temp', 'day_low_temp', 'sky_state', 
        'weather_state', 'weather_kor', 'rain_persent', 'expect_rain_6h', 'expect_rain_12h', 'expect_snow_6h', 
        'expect_snow_12h', 'wind_speed', 'wind_way', 'wind_text', 'humi', 'fine_dust', 'small_fine_dust')

class Gu4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gu4
        fields = ('num', 'gu', 'time_difference', 'hour', 'temp', 'day_high_temp', 'day_low_temp', 'sky_state', 
        'weather_state', 'weather_kor', 'rain_persent', 'expect_rain_6h', 'expect_rain_12h', 'expect_snow_6h', 
        'expect_snow_12h', 'wind_speed', 'wind_way', 'wind_text', 'humi', 'fine_dust', 'small_fine_dust')

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ('num', 'update_year', 'update_month', 'update_date')


