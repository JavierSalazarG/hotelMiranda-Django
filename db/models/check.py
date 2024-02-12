from django import forms

class inputForCheck(forms.Form):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'arrival'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'ledparture'}))