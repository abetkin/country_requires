
from django.db.models import F
from .models import Requirement

class Admin:
    def get_model_perms(self, request):
        return {
            'change': True,
            'add': True,
            'delete': True
        }

class CountryMixin:
    def get_queryset(self, request):
        qs = self.super().get_queryset(request)
        if qs.model != Requirement:
            return qs.none()
        return qs.filter(countries__users=request.user.pk)


class Editor(CountryMixin):
    def get_model_perms(self, request):
        return {
            'change': True,
            'add': True,
        }
    

class ReadOnly(CountryMixin):
    def get_model_perms(self, request):
        return {
            'change': request.method == 'GET'
        }


class External(ReadOnly):
    
    def get_queryset(self, request):
        qs = CountryMixin.get_queryset(self, request)
        return qs.only('name')

    def get_exclude(self, request, obj=None):
        return [
            'description', 'picture_image',
        ]