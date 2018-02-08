
from django.contrib import admin
from django import forms
from django.forms import formsets


from .models import *
from .forms import Link, PropertyField

class RequirementsInlineForm(forms.ModelForm):
    change_history = PropertyField(
        property='change_history',
        widget=Link(attrs={'label': 'History'}),
        required=False,
    )
    


class RequirementsInline(admin.TabularInline):
    model = CountryRequirement
    form = RequirementsInlineForm

    fields = [
        'name', 'description', 'status', 'change_history',
    ]

    def get_formset(self, request, obj=None, **kwargs):
        kwargs.update(form=self.form, fields=self.fields)
        fs = super().get_formset(request, obj=obj, **kwargs)
        return fs



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [
        RequirementsInline
    ]

inverse_status_choices = {v: k for k, v in Requirement.STATUS_CHOICES}

def set_published_status(modeladmin, request, queryset):
    value = 'Published'
    db_value = inverse_status_choices[value]
    queryset.update(status=db_value)
set_published_status.short_description = f"Set PUBLISHED status"

def set_draft_status(modeladmin, request, queryset):
    value = 'Draft'
    db_value = inverse_status_choices[value]
    queryset.update(status=db_value)
set_draft_status.short_description = f"Set DRAFT status"

def set_deleted_status(modeladmin, request, queryset):
    value = 'Deleted'
    db_value = inverse_status_choices[value]
    queryset.update(status=db_value)
set_deleted_status.short_description = f"Set DELETED status"

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    actions = [set_published_status, set_draft_status, set_deleted_status]

    def get_actions(self, *args, **kw):
        actions = super().get_actions(*args, **kw)
        actions.pop('delete_selected')
        return actions