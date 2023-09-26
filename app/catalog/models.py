from django.db import models
from catalog.managers import CategoryQuerySet
from treebeard.mp_tree import MP_Node
from django.utils.translation import gettext_lazy as _
from libs.db.fields import UpperCaseCharField
class Category(MP_Node):
    title = models.CharField(max_length=255,  db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode = True)
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
    slug = models.SlugField(unique=True, , allow_unicode = True)
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
        text         =  _("text")
        integer      =  _("integer")
        float        =  _("float")
        option       =  _("option")
        multi_option =  _("multi_option")
    title         = models.CharField(max_length=255,  db_index=True)
    type          = models.CharField(max_length=16,  choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    prodcut_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, related_name="attributes")
    option_group  = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null= True, blank=True)
    required      = models.BooleanField(default=False)
    class Meta:
        verbose_name        = "Product attribute"
        verbose_name_plural = "Product attributes"
    def __str__(self):
        return self.title

class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text =  _("text")
        integer =  _("integer")
        float =  _("float")
        option =  _("option")
        multi_option =  _("multi_option")
    title        = models.CharField(max_length=255,  db_index=True)
    type         = models.CharField(max_length=16,  choices=OptionTypeChoice.choices, default=OptionTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null= True, blank=True)
    required     = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name        = "Option"
        verbose_name_plural = "Options"

class Product(models.Model):
    class ProductTypeChoice(models.TextChoices):
        standalone = "standalone"
        parent     = "parent"
        child      = "child"
    structure        = models.CharField(max_length=16, choices=ProductTypeChoice.choices, default=ProductTypeChoice.standalone )
    title            = models.CharField(max_length=128, null = True, blank= True)
    upc              = UpperCaseCharField(max_length=24, unique=True, blank=True, null=True )                                                      #custom field    
    is_public        = models.BooleanField(default=True)
    meta_title       = models.CharField(null = True, blank= True)
    meta_description = models.TextField(null = True, blank= True)
    parent           = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null = True, blank=True)
    slug             = models.SlugField(unique=True, allow_unicode = True)
    product_class = models.ForeignKey(ProductClass, related_name="products", on_delete=models.PROTECT, null = True, blank= True)
    attributes    = models.ManyToManyField(ProductAttribute, through="ProductAttributeValue")
    recomended_products =  models.ManyToManyField('catalog.Product', through="ProductRecommendation", blank=True)

class ProductAttributeValue(models.Model):#for through 
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)

    value_text         = models.TextField(null = True, blank= True)
    value_integer      = models.IntegerField(null = True, blank= True)
    value_float        = models.FloatField(null = True, blank= True)
    value_option       = models.ForeignKey(OptionGroupValue, on_delete=models.PROTECT)
    value_multi_option = models.ManyToManyField(OptionGroup)

    class Meta:
        verbose_name        = "attribute value"
        verbose_name_plural = "attribute values"
        unique_together     = ("product" , "attribute")

class ProductRecommendation(models.Model):#for through 
    primary         = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="primary_recommendation")
    recomendation   = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute       = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    rank            = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ("primary" , "recomendation")
        ordering        = ("primary", "-rank")
        