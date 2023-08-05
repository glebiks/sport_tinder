from django import forms
from .models import Profile

class SportForm(forms.Form):
    sport = forms.ChoiceField(choices=Profile.SPORTS)


class ProfileForm(forms.ModelForm):
    # sport = forms.ChoiceField(choices=Profile.SPORTS, initial=1)
    class Meta:
        model = Profile
        fields = ['bio', 'profileimg', 'location', 'sport']
