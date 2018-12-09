from django.contrib import admin
from .models import Laptop , Category ,Phone , SourceDetail
# Register your models here.
from django import forms
admin.site.register(Laptop)
admin.site.register(Category)
admin.site.register(Phone)


from ckeditor_uploader.widgets import CKEditorUploadingWidget



class SourceDetailForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = SourceDetail
        exclude = ['id']

class SourceDetailAdmin(admin.ModelAdmin):
    form = SourceDetailForm

admin.site.register(SourceDetail, SourceDetailAdmin)