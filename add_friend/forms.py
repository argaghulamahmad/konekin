from django import forms

class Add_Friend_Form(forms.Form):
    error_messages={
        'required' :'Tolong isi input ini',
    }
    attrs = {
        'class' : 'form-control'
    }

    name = forms.CharField(label= 'NAME', required = True, max_length = 28, widget = forms.TextInput(attrs=attrs))
    url = forms.URLField(label = 'URL',required = True, widget = forms.URLInput(attrs=attrs))