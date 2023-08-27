from django.db import models

from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    title = models.CharField(max_length=255,  db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, )
    prepopulated_fields = {"slug": ["title",]}
    # node_order_by = ['name']

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
