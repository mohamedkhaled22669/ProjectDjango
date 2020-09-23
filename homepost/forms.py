from django import forms

from PIL import Image

class FormAddPost(forms.Form):
    topic = forms.CharField(max_length = 50)
    content = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 50)
    # picture = forms.FileField()


class FormDeletPost(forms.Form):
    id = forms.IntegerField()
    
    
    
class FormUpdatePost(forms.Form):
    id = forms.IntegerField()
    topic = forms.CharField(max_length = 50)
    content = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 50)