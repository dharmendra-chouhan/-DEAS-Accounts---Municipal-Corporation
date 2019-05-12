from django import forms


from .models import Subledger_master


class SearchForm(forms.Form):
    query = forms.CharField()



class Subledger_masterForm(forms.ModelForm):
    class Meta:
        model = Subledger_master
        fields = ('function_id', 'object_id','lookupdet_bug','opening_bal','lookupdet_opening_drcr','opening_bal_date','subledger_code','subledger_desc','status','budget_provion_required')

    def __init__(self, *args, **kwargs):
        super(Subledger_masterForm, self).__init__(*args, **kwargs)
        self.fields['budget_provion_required'].label = ''

