from django import forms
from django.core import validators

def name_for_s(value):
    if value[0].lower() != "s":
        raise forms.ValidationError("Name should start with S")

class FormName(forms.Form):
    name = forms.CharField(validators=[name_for_s])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Verify Email")
    address = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    """def clean_botcatcher(self):
        bot_catcher = self.cleaned_data['botcatcher']
        if len(bot_catcher) != 0:
            raise forms.ValidationError("Hidden Field Passed")
        return bot_catcher"""

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email and Verify Email are not matching")
