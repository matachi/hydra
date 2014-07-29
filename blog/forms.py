from django import forms
from django_comments_xtd.forms import XtdCommentForm


class SpamProtectedCommentForm(XtdCommentForm):
    """Extend the XtdCommentForm with an additional spam protection question.
    """

    spam_question = forms.CharField(
        label='Who is the original creator of Linux? (Most permutations are '
              'valid)',
        widget=forms.TextInput(
            attrs={'placeholder': 'spam protection question'}
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SpamProtectedCommentForm, self).__init__(*args, **kwargs)
        self.fields['url'].label = 'URL'

    def clean_spam_question(self):
        spam_question_answer = self.cleaned_data.get('spam_question')
        for word in spam_question_answer.lower().split():
            if word not in [
                'linus',
                'linux',
                'torvalds',
                'torvald',
                'benedict',
            ]:
                raise forms.ValidationError('Wrong answer')
