from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from djangoflix.db.models import PublishedStateOptions
from djangoflix.db.receivers import published_video_pre_save, slugify_pre_save

class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state = PublishedStateOptions.PUBLISH,
            published_timestamp__lte=now
        )

class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=2, choices=PublishedStateOptions.choices, default=PublishedStateOptions.DRAFT)
    published_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = VideoManager()

    @property
    def is_published(self):
        return self.active


class VideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"


pre_save.connect(published_video_pre_save, sender=Video)
pre_save.connect(slugify_pre_save, sender=Video)