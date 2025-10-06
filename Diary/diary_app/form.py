from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        # fields = '__all__'
        fields = ['note']

        labels={
            'Note' : 'note',
        }

        widgets={
        "note":forms.Textarea(attrs={
            'rows':10,
            'class':'w-full p-4 border border-gray-200 rounded-md focus:outline-none focus:ring-2 focus:ring-gray-300 focus:border-gray-300 transition-all'
        }),

        }