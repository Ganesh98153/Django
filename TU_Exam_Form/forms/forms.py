from django import forms
from forms.models import subjects

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = subjects
        fields= ['subject_name', 'subject_code', 'subject_semester', 'subject_type']
