from uuid import uuid4

from django.contrib.admin import ModelAdmin, TabularInline, register, HORIZONTAL, RelatedOnlyFieldListFilter
from django.db.models import NullBooleanField
from django.forms import CheckboxSelectMultiple, ChoiceField, ModelChoiceField
from django.utils.lorem_ipsum import sentence
from django.utils.translation import ugettext_lazy as _

from topology.fields import CategoryChoiceField
from topology.filters import CreationMonthListFilter, ModificationMonthListFilter, RandomMonthListFilter
from topology.forms import TestForm
from topology.models import (
    Category,
    Tag,
    Theme,
    Mapping,
    Test,
)
from topology.widgets import NullBooleanRadioSelect


@register(Tag)
class TagAdmin(ModelAdmin):
    search_fields = ("label",)


@register(Theme)
class ThemeAdmin(ModelAdmin):
    search_fields = ("label",)


@register(Category)
class CategoryAdmin(ModelAdmin):
    search_fields = ("label",)


class MappingInline(TabularInline):
    model = Mapping
    autocomplete_fields = ("tag",)
    min_num = 1
    max_num = 3
    extra = 1


@register(Test)
class TestAdmin(ModelAdmin):
    form = TestForm
    fieldsets = (
        (None, {
            "fields": (
                ("label", "slug", "active"),
                ("owner", "url", "key", "highlight"),
                ("lorem",)
            )
        }),
        (_("Relations"), {
            "fields": (
                ("category", "themes"),
                ("category2", "themes2"),
                ("category3", "themes3"),
                ("category4", "themes4"),
                ("category5", "category6"),
                ("themes5", "themes6"),
            )
        }),
        (_("Numbers"), {
            "fields": (
                ("number", "percent", "progress", "grade"),
            )
        }),
        (_("Dates"), {
            "fields": (
                ("creation_date", "last_modification_date", "random_date"),
                ("creation_datetime", "last_modification_datetime", "random_datetime"),
                ("creation_time", "last_modification_time", "random_time"),
                ("duration",)
            )
        }),
        (_("IP"), {
            "fields": (
                ("ip", "ipv4", "ipv6_forced", "ipv6"),
            )
        }),
        (_("raw data / Uploads"), {
            "fields": (
                ("raw_data", "file", "image", "path"),
            )
        }),
    )
    readonly_fields = ("creation_date", "last_modification_date", "creation_datetime", "last_modification_datetime",
                       "creation_time", "last_modification_time", "lorem")

    prepopulated_fields = {
        "slug": ("label",),
    }
    autocomplete_fields = ("category2", "themes2")
    radio_fields = {
        "category3": HORIZONTAL,
    }
    filter_horizontal = ("themes5",)
    filter_vertical = ("themes6",)
    inlines = [MappingInline]
    formfield_overrides = {
        NullBooleanField: {"widget": NullBooleanRadioSelect},
    }
    raw_id_fields = ("category4", "themes4")

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "themes3":
            kwargs.update({"widget": CheckboxSelectMultiple()})
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category5":
            return CategoryChoiceField(
                required=False,
                # empty_label="---------",
                queryset=Category.objects.all()
            )
        elif db_field.name == "category6":
            field = ModelChoiceField(required=False, queryset=Category.objects.filter(parent__parent__isnull=True))
            field.choices = list(e for e in field.choices if not e[0]) + list(
                (group.label, list((option.id, option.label) for option in Category.objects.filter(parent=group)))
                for group in Category.objects.filter(parent__isnull=True)
            )
            return field
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    search_fields = ("label", "description")
    list_filter = (
        "category",
        ("category2", RelatedOnlyFieldListFilter),
        CreationMonthListFilter,
        ModificationMonthListFilter,
        RandomMonthListFilter,
    )
    list_display = ("number", "label", "highlight", "key", "go", "lorem")
    list_display_links = ("key", "go")
    list_editable = ("number", "label")

    def lorem(self, obj):
        return sentence()
    lorem.short_description = _("lorem ipsum sentence")
    lorem.allow_tag = True

    def go(self, obj):
        return obj.label
    go.short_description = _("lien vers la fiche")

    def action_message(self, request, rows_updated):
        if rows_updated == 0:
            self.message_user(request, _("No row updated"))
        elif rows_updated == 1:
            self.message_user(request, _("1 row updated"))
        else:
            self.message_user(request, _("{} rows updated").format(rows_updated))

    def highlight_on(self, request, queryset):
        rows_updated = queryset.update(highlight=True)
        self.action_message(request, rows_updated)
    highlight_on.short_description = _("Turn Highlight on")

    def highlight_off(self, request, queryset):
        rows_updated = queryset.update(highlight=False)
        self.action_message(request, rows_updated)
    highlight_off.short_description = _("Turn Highlight off")

    def highlight_cancel(self, request, queryset):
        rows_updated = queryset.update(highlight=None)
        self.action_message(request, rows_updated)
    highlight_cancel.short_description = _("Cancel Highlight")

    def reset_key(self, request, queryset):
        for obj in queryset.all():
            obj.key = uuid4()
            obj.save()
        self.action_message(request, queryset.count())
    reset_key.short_description = _("Reset key")

    actions = [highlight_on, highlight_off, highlight_cancel, reset_key]

    def has_module_permission(self, request):  # pylint: disable=no-self-use,unused-argument
        """Can be accessed from home page"""
        return True

    def has_add_permission(self, request):  # pylint: disable=no-self-use,unused-argument
        """Can add an object"""
        return True

    def has_delete_permission(self, request, obj=None):  # pylint: disable=no-self-use,unused-argument
        """Can delete an object"""
        return True

    def has_change_permission(self, request, obj=None):  # pylint: disable=no-self-use,unused-argument
        """Can update an object"""
        return True

    def has_view_permission(self, request, obj=None):  # pylint: disable=no-self-use,unused-argument
        """Can view an object"""
        return True
