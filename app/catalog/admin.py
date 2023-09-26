from django.contrib import admin
from django.db.models import Count
from catalog.models import (Category,
                             ProductClass,
                             ProductAttribute, Option,
                             ProductRecommendation)
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, MyAdmin)

class AttributeCountFilter(admin.SimpleListFilter):
    title =("count of attributes")
    parameter_name = "countof"
    def lookups(self, request, model_admin):
        return [
            ("less_5", ("less than 5")),
            ("more_5", ("more than 5")),
        ]
    def queryset(self, request, queryset):
        if self.value() == "less_5":
            return queryset.annotate(
                attr_count=Count("attributes")
            ).filter(attr_count__lt=5)
        if self.value() == "more_5":
            return queryset.annotate(
                attr_count=Count("attributes")
            ).filter(attr_count__gte = 5)
            
class ProductAttributeInline(admin.TabularInline):      #TabularInline, StackedInline
    model = ProductAttribute
    extra = 2                                           #number of forms
class ProductRecommendationInline(admin.TabularInline): #TabularInline, StackedInline
    model = ProductRecommendation
    extra = 2
    fk_name = "primary"                                 #Foreign_key: a field in the 'ProductRecommendation' model
@admin.register(ProductClass)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "track_stock", "require_shipping", "attribute_count"]
    list_filter = [ "track_stock", "require_shipping", AttributeCountFilter]
    actions = ["enable_track_stock", "disable_track_stock", "enable_require_shipping", "disable_require_shipping",]
    inlines = [
        ProductAttributeInline,
        ProductRecommendationInline
    ]
    def attribute_count(self, obj):
        return obj.attributes.count() #"attributes" is a relatedname
    #Custom Actions
    def enable_track_stock(modeladmin, request, queryset):
        queryset.update(track_stock=True)
    def disable_track_stock(modeladmin, request, queryset):
        queryset.update(track_stock=False)
    def enable_require_shipping(modeladmin, request, queryset):
        queryset.update(require_shipping=True)
    def disable_require_shipping(modeladmin, request, queryset):
        queryset.update(require_shipping=False)

admin.site.register(Option)
# admin.site.register(OptionGroup)
admin.site.site_title = "djshop"
admin.site.index_title = "djshop"
admin.site.site_header = "djshop"