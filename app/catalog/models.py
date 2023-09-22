from django.db import models
from catalog.managers import CategoryQuerySet
from treebeard.mp_tree import MP_Node
from django.utils.translation import gettext_lazy as _
class Category(MP_Node):
    title = models.CharField(max_length=255,  db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,)
    prepopulated_fields = {"slug": ["title",]}
    # node_order_by = ['name']
    objects = CategoryQuerySet.as_manager() #Custom Manager
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class OptionGroup(models.Model):
    title = models.CharField(max_length=255,  db_index=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "option group"
        verbose_name_plural = "option groups"

class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255,  db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "option group value"
        verbose_name_plural = "option groups values"

class ProductClass(models.Model):
    title = models.CharField(max_length=255,  db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True,)
    prepopulated_fields = {"slug": ("title",)}
    track_stock = models.BooleanField(default=True)
    require_shipping = models.BooleanField(default=True)
    options = models.ManyToManyField("Option", blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "ProductClass"
        verbose_name_plural = "ProductClasses"

class ProductAttribute(models.Model):
    class AttributeTypeChoice(models.TextChoices):
        text =  _("text")
        integer =  _("integer")
        float =  _("float")
        option =  _("option")
        multi_option =  _("multi_option")
    title = models.CharField(max_length=255,  db_index=True)
    type = models.CharField(max_length=16,  choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    prodcut_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, related_name="attributes")
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null= True, blank=True)
    required = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Product attribute"
        verbose_name_plural = "Product attributes"

class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text =  _("text")
        integer =  _("integer")
        float =  _("float")
        option =  _("option")
        multi_option =  _("multi_option")
    title = models.CharField(max_length=255,  db_index=True)
    type = models.CharField(max_length=16,  choices=OptionTypeChoice.choices, default=OptionTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null= True, blank=True)
    required = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"