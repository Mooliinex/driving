from django import forms


class Planning(forms.Form):
    date = forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker'}), label="date", max_length=35)
