from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import *
import datetime


class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = "__all__"

    def validate_davomiylik(self, qiymat):
        if qiymat <= datetime.timedelta(minutes=7):
            return qiymat
        else:
            raise ValidationError("Faqat 7 daqiqadan kam bo'lgan mp3 fayllarni yuklang!")

    def validate_fayl(self, qiymat):
        print(qiymat)
        if qiymat.url.endswith('.mp3'):
            return qiymat
        else:
            raise ValidationError("Faqat [.mp3] formatidagi fayl bo'lishi kerak")

    def to_representation(self, instance):
        qoshiq = super(QoshiqSerializer, self).to_representation(instance)
        qoshiq.update({'albom': instance.albom.nom})
        return qoshiq


class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = "__all__"


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"

    def to_representation(self, instance):
        albom = super(AlbomSerializer, self).to_representation(instance)
        albom.update({'qoshiqchi': instance.qoshiqchi.ism})
        return albom
