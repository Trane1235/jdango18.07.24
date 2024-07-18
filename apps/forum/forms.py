from django import forms
from . import models


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = models.Forum
        fields = ('content', )

        labels = {
            "content": 'содержание текста',
            "sender_id": 'id отправителя',
            "date": 'дата создания'
        }

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 16,
                    'cols': 64
                }
            )
        }
