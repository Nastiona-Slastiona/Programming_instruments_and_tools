from django import forms
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Mem

class MemCreateForm(forms.ModelForm):
    class Meta:
        model = Mem
        fields = ('title', 'url', 'description')
    def clean_url(self):
        url = self.cleaned_data['url']
        # valid_extensions = ['jpg', 'jpeg']
        # extension = url.rsplit('.', 1)[1].lower()
        # if extension not in valid_extensions:
        #     raise forms.ValidationError('The given' 
        #         'URL does not match valid image extensions.')
        return url
    def save(self, force_insert=False, 
            force_update=False, commit=True):
        mem = super(MemCreateForm, self).save(commit=False)
        mem_url = self.cleaned_data['url']
        mem_name = '{}.{}'.format(slugify(mem.title), 
                    mem_url.rsplit('.', 1)[1].lower())

        response = request.urlopen(mem_url)
        mem.mem.save(mem_name, ContentFile(response.read()), 
                    save=False)
        if commit:
            mem.save()
        return mem