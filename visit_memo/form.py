from django import forms

class VisitorForm(forms.Form):
    docfile = forms.FileField(
        label = 'Select a file',
        help_text = 'max.42megabytes'
    )