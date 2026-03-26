from django.db import models
from django.utils.text import slugify

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SlugMixin(models.Model):
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            if hasattr(self, "name"):
                self.slug = slugify(self.name)
        super().save(*args, **kwargs)
