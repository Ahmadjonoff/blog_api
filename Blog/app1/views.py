from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class MaqolaViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSer
    filter_backends = [filters.OrderingFilter,]
    ordering_fields = ['sarlavha', 'id', 'sana']
    # search_fields = ['sarlavha', 'id', 'sana']

    def get_queryset(self):
        maqola = Maqola.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            maqola = Maqola.objects.annotate(
                similarity=TrigramSimilarity("sarlavha", soz)
            ).filter(similarity__gte=0.1).order_by("-similarity")
        return maqola

class TalksViewSet(ModelViewSet):
    queryset = Talks.objects.all()
    serializer_class = TalksSer