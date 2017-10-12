from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    description_attrs = {
        'type': 'text',
        'cols': 100,
        'rows': 4,
        'class': 'todo-form-textarea',
        'placeholder':'Masukan deskripsi...'
    }
    description = forms.CharField(label="", required=True,max_length=130, widget=forms.Textarea(attrs=description_attrs))
