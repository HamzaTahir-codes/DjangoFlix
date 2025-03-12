from django.utils import timezone
from django.utils.text import slugify
from .models import PublishedStateOptions

def published_video_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishedStateOptions.PUBLISH
    is_draft = instance.state == PublishedStateOptions.DRAFT
    if is_publish and instance.published_timestamp is None:
            instance.published_timestamp = timezone.now()
            instance.active = True
    elif is_draft:
        instance.published_timestamp = None

def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if not slug:
        instance.slug = slugify(title)