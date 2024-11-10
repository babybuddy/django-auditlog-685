from django.db import models
from django.utils.translation import gettext_lazy as _

from auditlog.registry import auditlog
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class MyCustomTag(TagBase):
    note = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class TaggedWhatever(GenericTaggedItemBase):
    # TaggedWhatever can also extend TaggedItemBase or a combination of
    # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
    # allows using the same tag for different kinds of objects, in this
    # example Food and Drink.

    # Here is where you provide your custom Tag class.
    tag = models.ForeignKey(
        MyCustomTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class Food(models.Model):
    name = models.CharField(max_length=200)
    tags = TaggableManager(through=TaggedWhatever)


class Drink(models.Model):
    name = models.CharField(max_length=200)
    tags = TaggableManager(through=TaggedWhatever)


auditlog.register(Food, m2m_fields=["tags"])
auditlog.register(Drink, m2m_fields=["tags"])

