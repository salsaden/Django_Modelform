from django import forms
from Sals_DjangoModelForm.models import StudenteMobilis

class EmpForm(forms.ModelForm):
    class Meta:
        model=StudenteMobilis
        fields="__all__"