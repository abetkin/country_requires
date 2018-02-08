from django.db import models
from django.utils.html import format_html

class Country(models.Model):
    ISO_CODE = models.CharField(max_length=10)
    name = models.CharField(max_length=200, db_column='country_name')
    users = models.ManyToManyField('users.User')

    def __str__(self):
        return self.name

class Requirement(models.Model):
    id = models.AutoField(primary_key=True, db_column='requirement_id')
    name = models.CharField(max_length=100, db_column='requirement_name')
    description = models.CharField(max_length=1000)
    picture_image = models.ImageField()
    countries = models.ManyToManyField('Country', through='CountryRequirement')
    STATUS_CHOICES = (
        ('PB', 'Published'),
        ('DR', 'Draft'),
        ('DL', 'Deleted'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def delete(self, **kw):
        self.status = 'DL'
        self.save()

    def __str__(self):
        return self.name


class CountryRequirement(Requirement):
    country = models.OneToOneField('Country', on_delete=models.CASCADE)

    @property
    def change_history(self):
        return f"/admin/app/requirement/{self.pk}/history/"