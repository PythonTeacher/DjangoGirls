from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에게 알려줌
    class Meta:
        model = Post
        fields = ('title', 'text',)