from django.views.generic.base import View
from django.http import HttpResponse
from rest_framework import viewsets


class MockView(View):
    def get(self, request):
        return HttpResponse('hey')


def mock_view(request):
    return HttpResponse('hey')


class MockViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
