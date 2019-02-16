from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy


class NullBooleanRadioSelect(RadioSelect):
    template_name = 'django/forms/widgets/horizontal_radio.html'

    def __init__(self, *args, **kwargs):
        choices = (
            (None, ugettext_lazy('Unknown')),
            (True, ugettext_lazy('Yes')),
            (False, ugettext_lazy('No'))
        )
        super(NullBooleanRadioSelect, self).__init__(choices=choices, *args, **kwargs)

    _empty_value = None
