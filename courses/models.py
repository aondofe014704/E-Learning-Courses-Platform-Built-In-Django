from django.db import models


class AccessRequired(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email_required"
    DRAFT = "draft", "Draft"


class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"


def handle_upload(instance, filename):
    return f"{filename}"


class Course(models.Model):
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True)

    access = models.CharField(max_length=15,
                              choices=AccessRequired.choices,
                              default=AccessRequired.EMAIL_REQUIRED
                              )
    status = models.CharField(max_length=10,
                              choices=PublishStatus.choices,
                              default=PublishStatus.DRAFT
                              )

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

# Create your models here.
