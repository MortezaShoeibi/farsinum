from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class IndexView(View):
    def get(self, request) -> HttpResponse:
        return render(request, 'index.html', {})
