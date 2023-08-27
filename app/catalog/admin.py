from django.contrib import admin
from catalog.models import Category
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, MyAdmin)
