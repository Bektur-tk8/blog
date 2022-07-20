from django.shortcuts import get_object_or_404, render
from blog.models import *



class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact = slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})


