from django.forms import ModelForm, CheckboxSelectMultiple, ChoiceField, ModelChoiceField

from topology.fields import CategoryChoiceField
from topology.models import Test, Category


class TestForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(* args, **kwargs)
        # self.fields["category5"] = CategoryChoiceField(
        #     required=False,
        #     # empty_label="---------",
        #     queryset=Category.objects.all()
        # )

        # self.fields["category6"] = ModelChoiceField(required=False,
        #                                             queryset=Category.objects.filter(parent__parent__isnull=True))
        # self.fields["category6"].choices = list(e for e in self.fields["category6"].choices if not e[0]) + list(
        #     (group.label, list((option.id, option.label) for option in Category.objects.filter(parent=group)))
        #     for group in Category.objects.filter(parent__isnull=True)
        # )

    class Meta:
        model = Test
        fields = "__all__"
        # widgets = {
        #     "themes3": CheckboxSelectMultiple(),
        # }
