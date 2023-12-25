from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import TrigramSimilarity

from drf_yasg.utils import swagger_auto_schema


class QoshiqAPI(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=QoshiqSerializer)
    def post(self, request):
        qoshiq = request.data
        serializer = QoshiqSerializer(data=qoshiq)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class QoshiqchilarAPI(APIView):
    def get(self, request):
        qoshiqchi = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchi, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=QoshiqchiSerializer)
    def post(self, request):
        qoshiqchi = request.data
        serializer = QoshiqchiSerializer(data=qoshiqchi)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors())


class QoshiqchiAPI(APIView):
    def get(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=QoshiqchiSerializer)
    def put(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    @swagger_auto_schema(request_body=QoshiqchiSerializer)
    def delete(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        qoshiqchi.delete()
        return Response(serializer.data)


class AlbomlarModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['sana']
    search_fields = ['nom']

    @action(detail=True)
    def qoshiqlari(self, request, pk):
        albom = self.get_object()
        qoshiqlari = albom.qoshiq_set.all()
        serializer = QoshiqSerializer(qoshiqlari, many=True)
        return Response(serializer.data)


class QoshiqchilarModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['tugilgan_yil']
    search_fields = ['ism', 'davlat']

    @action(detail=True)
    def albomlari(self, request, pk):
        qoshiqchi = self.get_object()
        albomlari = qoshiqchi.albom_set.all()
        serializer = AlbomSerializer(albomlari, many=True)
        return Response(serializer.data)


class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['davomiylik']
    search_fields = ['nom', 'janr']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2

    def get_queryset(self):
        search = self.request.query_params.get('search')
        qoshiqlar = self.queryset
        if search:
            qoshiqlar = Qoshiq.objects.annotate(
                similirity=TrigramSimilarity('nom', search)
            ).filter(similirity__gt=0.3).order_by('-similirity')
        return qoshiqlar
