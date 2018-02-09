import uuid

from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class DefaultBaseModel(TimestampedModel):
    slug = models.SlugField(max_length=36, unique=True, null=False, blank=False)

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()

        super().save(**kwargs)

    class Meta:
        abstract = True


class WatchList(DefaultBaseModel):
    tmdb_id = models.IntegerField(blank=False, null=False)
    seen = models.NullBooleanField()
    
    def __str__(self):
        return self.tmdb_id

    class Meta:
        ordering = ('tmdb_id',)
        verbose_name_plural = 'watchlist'

