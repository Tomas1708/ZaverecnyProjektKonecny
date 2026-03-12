from django import  forms
from .models import Policyholder, Insurance
import re

class PolicyholderForm(forms.ModelForm):

    class Meta:
        model = Policyholder
        fields = ["first_name",
                  "last_name",
                  "age",
                  "phone_number",
                  "email",
                  "street",
                  "city",
                  "postal_code",]

        widgets = {
            "age": forms.NumberInput(attrs={"min": 0}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #zavola pôvodný konštruktor z ModelForm a Django vytvorí self.fields

        for field in self.fields.values():  #self.fields -> slovník všetkých polí formulára, .values() berie len hodnoty
            field.widget.attrs.update({     #widget -> html prvok, CharField -> <input type="text">
                'class': "form-control"     #field.widget.attrs -> slovník HTML atribútov
            })

class InsuranceForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = ["insurance_type",
                  "insured_object",
                  "description",
                  "amount",
                  "valid_from",
                  "valid_to",
                  ]
        widgets = {
            "description": forms.Textarea(attrs={'rows': 3}),
            "amount": forms.NumberInput(attrs={"min": 0, "step": 0.01}),
            "valid_from": forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
            "valid_to": forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
        }

class PolicyholdersSearchForm(forms.Form):
    first_name = forms.CharField(
        required=False,
        label="Meno",
    )
    last_name = forms.CharField(
        required=False,
        label="Priezvisko"
    )




