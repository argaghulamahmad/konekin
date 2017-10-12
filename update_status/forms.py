from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    description_attrs = {
        'type': 'text',
        'cols': 45,
        'rows': 4,
        'class': 'todo-form-textarea',
        'placeholder':"what's new?"
    }
    description = forms.CharField(label="", required=True, max_length=140, widget=forms.Textarea(attrs=description_attrs))
