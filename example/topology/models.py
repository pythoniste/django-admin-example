from functools import partial
from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    Model,
    CharField,
    EmailField,
    URLField,
    UUIDField,
    SlugField,
    TextField,
    BooleanField,
    NullBooleanField,
    DateField,
    DateTimeField,
    TimeField,
    PositiveSmallIntegerField,
    GenericIPAddressField,
    DurationField,
    DecimalField,
    FloatField,
    IntegerField,
    BinaryField,
    FilePathField,
    FileField,
    ImageField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
)
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class Tag(Model):

    label = CharField(
        verbose_name=_("menu label"),
        help_text=_("used in the menu when fully deployed"),
        max_length=127,
        blank=False,
        db_index=True,
        unique=True,
    )

    def __str__(self):
        """Return a string that represent the current object to an end user."""
        return self.label

    class Meta:  # pylint: disable=too-few-public-methods
        """Tag Meta class"""

        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        ordering = ("label",)


class Theme(Model):

    COLORS = (
        ("#ffffff", _("White")),
        ("#ff0000", _("Red")),
        ("#00ff00", _("Green")),
        ("#0000ff", _("Blue")),
        ("#000000", _("Black")),
    )

    label = CharField(
        verbose_name=_("label"),
        max_length=127,
        blank=False,
        db_index=True,
        unique=True,
    )

    color = CharField(
        verbose_name=_("color"),
        choices=COLORS,
        max_length=1,
        blank=False,
        db_index=True,
        unique=True,
    )

    def __str__(self):
        """Return a string that represent the current object to an end user."""
        return self.label

    class Meta:  # pylint: disable=too-few-public-methods
        """Theme Meta class"""

        verbose_name = _("theme")
        verbose_name_plural = _("themes")
        ordering = ("label",)


class Category(Model):

    parent = ForeignKey(
        verbose_name=_("parent"),
        related_name="child_set",
        to="self",
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    label = CharField(
        verbose_name=_("label"),
        max_length=127,
        blank=False,
        db_index=True,
        unique=True,
    )

    @property
    def depth(self):
        if self.parent_id:
            return self.parent.depth + 1
        return 0

    @property
    def full_label(self):
        if self.parent_id:
            return self.parent.full_label + " > " + self.label
        return self.label

    @property
    def deep_label(self):
        return "\u2003" * ((self.depth - 1) * 2 - 1) + (self.depth and "\u2514\u2500" or "") + self.label

    def __str__(self):
        """Return a string that represent the current object to an end user."""
        return self.label

    class Meta:  # pylint: disable=too-few-public-methods
        """Category Meta class"""

        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("label",)


class Test(Model):

    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    label = CharField(
        verbose_name=_("label"),
        max_length=32,
        blank=False,
        db_index=True,
        unique=True,
    )

    category = ForeignKey(
        verbose_name=_("category"),
        related_name="tag_set",
        to=Category,
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    themes = ManyToManyField(
        verbose_name=_("themes"),
        related_name="tag_set",
        to=Theme,
        blank=True,
    )

    category2 = ForeignKey(
        verbose_name=_("category 2"),
        related_name="tag2_set",
        to=Category,
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    themes2 = ManyToManyField(
        verbose_name=_("themes 2"),
        related_name="tag2_set",
        to=Theme,
        blank=True,
    )

    category3 = ForeignKey(
        verbose_name=_("category 3"),
        related_name="tag3_set",
        to=Category,
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    themes3 = ManyToManyField(
        verbose_name=_("themes 3"),
        related_name="tag3_set",
        to=Theme,
        blank=True,
    )

    category4 = ForeignKey(
        verbose_name=_("category 4"),
        related_name="tag4_set",
        to=Category,
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    themes4 = ManyToManyField(
        verbose_name=_("themes 4"),
        related_name="tag4_set",
        to=Theme,
        blank=True,
    )

    category5 = ForeignKey(
        verbose_name=_("category 5"),
        related_name="tag5_set",
        to=Category,
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    themes5 = ManyToManyField(
        verbose_name=_("themes 5"),
        related_name="tag5_set",
        to=Theme,
        blank=True,
    )

    category6 = ForeignKey(
        verbose_name=_("category 6"),
        related_name="tag6_set",
        to=Category,
        null=True,
        blank=True,
        db_index=True,
        on_delete=CASCADE,
    )

    themes6 = ManyToManyField(
        verbose_name=_("themes 6"),
        related_name="tag6_set",
        to=Theme,
        blank=True,
    )

    tag = ManyToManyField(
        verbose_name=_("themes"),
        related_name="tag_set",
        to=Tag,
        through="Mapping",
        blank=True,
    )

    number = PositiveSmallIntegerField(
        verbose_name=_("number"),
        unique=True,
    )

    percent = DecimalField(
        verbose_name=_("percent"),
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    progress = FloatField(
        verbose_name=_("progress"),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    grade = IntegerField(
        verbose_name=_("grade"),
        validators=[MinValueValidator(-10), MaxValueValidator(10)],
    )

    slug = SlugField(
        unique=True,
        max_length=32,
        editable=True,
        db_index=True,
    )

    owner = EmailField(
        verbose_name=_("owner"),
        blank=True,
        null=True,
    )

    url = URLField(
        verbose_name=_("url"),
        blank=True,
        null=True,
    )

    key = UUIDField(
        default=uuid4,
    )

    description = TextField(
        verbose_name=_("description"),
    )

    active = BooleanField(
        verbose_name=_("active"),
    )

    highlight = NullBooleanField(
        verbose_name=_("highlight"),
    )

    creation_date = DateField(
        verbose_name=_("creation date"),
        auto_now_add=True,
    )

    last_modification_date = DateField(
        verbose_name=_("last modification date"),
        auto_now=True,
    )

    random_date = DateField(
        verbose_name=_("random date"),
    )

    creation_datetime = DateTimeField(
        verbose_name=_("creation datetime"),
        auto_now_add=True,
    )

    last_modification_datetime = DateTimeField(
        verbose_name=_("last modification datetime"),
        auto_now=True,
    )

    random_datetime = DateTimeField(
        verbose_name=_("random datetime"),
    )

    duration = DurationField(
        verbose_name=_("duration"),
    )

    creation_time = TimeField(
        verbose_name=_("creation time"),
        auto_now_add=True,
    )

    last_modification_time = TimeField(
        verbose_name=_("last modification time"),
        auto_now=True,
    )

    random_time = TimeField(
        verbose_name=_("random time"),
    )

    ip = GenericIPAddressField(
        verbose_name=_("IP v4 ou 6"),
        protocol="both",
    )

    ipv4 = GenericIPAddressField(
        verbose_name=_("IP v4 as is"),
        protocol="IPv4",
    )

    ipv6_forced = GenericIPAddressField(
        verbose_name=_("IP v6 (ipv4 will be converted)"),
        protocol="both",
        unpack_ipv4=True,
    )

    ipv6 = GenericIPAddressField(
        verbose_name=_("IP v6"),
        protocol="IPv6",
    )

    raw_data = BinaryField(
        verbose_name=_("raw data"),
        max_length=127,
        editable=True,
        blank=True,
    )

    def compute_upload_path(current_object, sub_path, filename):
        """Describe the image storage path"""
        today = now()
        return str(
            Path.joinpath(*list(
                map(
                    Path,
                    (
                        current_object._meta.app_label,  # pylint: disable=protected-access
                        current_object._meta.model_name,  # pylint: disable=protected-access
                        sub_path,
                        str(today.year),
                        str(today.month),
                        str(uuid4()) + Path(filename).suffix)))))

    file = FileField(
        verbose_name=_("file"),
        max_length=256,
        upload_to=partial(compute_upload_path, subpath="file"),
        null=True,
        blank=True,
    )

    image = ImageField(
        verbose_name=_("image"),
        max_length=256,
        upload_to=partial(compute_upload_path, subpath="image"),
        null=True,
        blank=True,
    )

    path = FilePathField(
        verbose_name=_("path"),
        path=settings.STATIC_PATH,
    )

    def __str__(self):
        """Return a string that represent the current object to an end user."""
        return self.label

    class Meta:  # pylint: disable=too-few-public-methods
        """Test Meta class"""

        verbose_name = _("test")
        verbose_name_plural = _("tests")
        ordering = ("number", )


class Mapping(Model):

    test = ForeignKey(
        verbose_name=_("test"),
        related_name="mapping_set",
        to=Test,
        null=False,
        blank=False,
        db_index=True,
        on_delete=CASCADE,
    )

    tag = ForeignKey(
        verbose_name=_("tag"),
        related_name="mapping_set",
        to=Tag,
        null=False,
        blank=False,
        db_index=True,
        on_delete=CASCADE,
    )

    order = PositiveSmallIntegerField(
        verbose_name=_("order"),
    )

    info = CharField(
        verbose_name=_("additional information"),
        max_length=255,
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Mapping Meta class"""

        verbose_name = _("mapping")
        verbose_name_plural = _("mappings")
        ordering = ("test", "tag", "order")
        index_together = (
            ("test", "tag", "order"),
        )
        unique_together = (
            ("test", "tag", "order"),
        )
