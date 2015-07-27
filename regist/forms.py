from django import forms

from .models import Record

class RecordForm(forms.ModelForm):
    medic = forms.ModelChoiceField(queryset = Record.objects.all(),empty_label="Выберите проект",widget=forms.Select(attrs={'class':'dropdown'}),label="Проекты")

    class Meta:
        model = Record
        fields = ('medic', 'visitor_first_name', 'visitor_last_name', 'record_date', 'record_time')