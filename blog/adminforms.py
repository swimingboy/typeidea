#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'linghang'

from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='再要', required=False)