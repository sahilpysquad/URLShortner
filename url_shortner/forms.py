from django import forms

from url_shortner.models import URLShortner


class URLShortnerModelForm(forms.ModelForm):
    class Meta:
        model = URLShortner
        fields = ('long_url', 'password')

    def save(self, commit=True):
        obj = super(URLShortnerModelForm, self).save(commit=commit)
        obj.set_password(obj.password)
        obj.save()
        return obj


class VerifyPasswordForm(forms.Form):
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(), required=True)
