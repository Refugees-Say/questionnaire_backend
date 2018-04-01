from django import forms
from .models import QuestionOrder


class QuestionOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in ['radio', 'rank', 'selection']:
            self.fields[f].required = False

    def is_valid(self, *args, **kwargs):
        super().is_valid(*args, **kwargs)
        attrs = self.cleaned_data
        if attrs['radio'] and attrs['rank'] is None and attrs['selection'] is None:
            return True
        if attrs['radio'] is None and attrs['rank'] and attrs['selection'] is None:
            return True
        if attrs['radio'] is None and attrs['rank'] is None and attrs['selection'] is None:
            return True
        raise forms.ValidationError('Only one field should be selected from radio, rank and selection')

    class Meta:
        model = QuestionOrder
        fields = ('radio', 'rank', 'selection', 'order', 'questionnaire', )
