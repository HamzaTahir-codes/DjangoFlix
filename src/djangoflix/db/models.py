from django.db import models

class PublishedStateOptions(models.TextChoices):
        # Constant = DB_Value, User_display_value
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN', 'Unlisted'
        # PRIVATE = 'PR', 'Private'