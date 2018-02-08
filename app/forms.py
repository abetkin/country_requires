from django import forms
from django.forms.widgets import Widget
from django.forms.boundfield import BoundField

class PropertyField(forms.Field):
    def __init__(self, *args, **kwargs):
        self._property_name = kwargs.pop('property')
        self._property_widget = kwargs.get('widget')
        super().__init__(*args, **kwargs)

    def get_bound_field(self, form, name):
        obj = form.instance
        value = getattr(obj, self._property_name)
        kw = {}
        if self._property_widget:
            kw['widget'] = self._property_widget
        field = forms.Field(initial=value, **kw)
        return BoundField(form, field, name)


class Link(Widget):
    input_type = 'text'
    template_name = 'app/link.html'
