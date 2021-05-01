from django import forms
from .models import Pizza, Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        label={"Comment:":''}
        widgets = {'comment':forms.Textarea(attrs={'cols':80})}
