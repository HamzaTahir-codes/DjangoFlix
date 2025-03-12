from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Video, PublishedStateOptions

class VideoModelTestCase(TestCase):
    def setUp(self):
        self.test_a = Video.objects.create(title="This is my title", video_id="abc")
        self.test_b = Video.objects.create(title="This is my title", state=PublishedStateOptions.PUBLISH, video_id="abcd")

    # Test Validation
    def test_valid_title(self):
        title = "This is my title"
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
    
    def test_slug_field(self):
        title = self.test_a.title
        test_slug = slugify(title)
        self.assertEqual(self.test_a.slug, test_slug)

    # Test for the Created count
    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 2)

    # Test for the Draft state
    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishedStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)
    
    # Test for the Publish state
    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishedStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(published_timestamp__lte=now)
        self.assertTrue(published_qs.exists())
    
    def test_publish_manager(self):
        published_qs = Video.objects.all().published()
        now = timezone.now()
        qs = Video.objects.filter(state=PublishedStateOptions.PUBLISH, published_timestamp__lte=now)
        self.assertEqual(published_qs.count(), qs.count())