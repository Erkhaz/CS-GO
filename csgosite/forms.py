from django import forms

from .models import csgo, csgoteam, csgoplayer


class AddcyberSportTypeForm(forms.ModelForm):
    class Meta:
        model = csgo
        fields = '__all__'

class AddTeamForm(forms.ModelForm):
    class Meta:
        model = csgoteam
        fields = '__all__'

class AddplayerForm(forms.ModelForm):
    class Meta:
        model = csgoplayer
        fields = '__all__'

