from django import forms
from .models import BlogComment

class CommentForm(forms.ModelForm):
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = BlogComment
        fields = ['comment_content']