from django import forms
from .models import BlogComment, Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category',
                  'title',
                  'content',
                  ]


class CommentForm(forms.ModelForm):
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4',
    }), label='')

    class Meta:
        model = BlogComment
        fields = ['comment_content']
