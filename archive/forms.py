# -*- coding: utf-8 -*-
from django import forms
import datetime

class UploadDataForm(forms.Form):
    datafile = forms.FileField(
        label='Select a file',
        help_text='import data spreadsheet'
    )
    
class ImportDataForm(forms.Form):
    datafilename = forms.CharField()
