from rest_framework import serializers
from .models import Er, Th, ThGr


class Random_Recommand_Theme_serial(serializers.ModelSerializer):
    class Meta:
        model = Th
        fields = [
            'id',
            'Th_Img1',
        ]

class Show_Er_serial(serializers.ModelSerializer):
    class Meta:
        model = Er
        fields = [
            'Er_Brand',
            'Er_Name',
            'Er_Num',
            'ErAd_Add',
            'Er_Homepage',
        ]

class Show_Theme_serial(serializers.ModelSerializer):
    er = Show_Er_serial(read_only=True)
    class Meta:
        model = Th
        fields = [
            'id',
            'er',
            'Th_Name',
            'Th_Genre',
            'Th_Nop',
            'Th_Time',
            'Th_Diff',
            'Th_Fear',
            'Th_Act',
            'Th_Intro',
            'Th_Img1',
        ]

