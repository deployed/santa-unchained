from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from santa_unchained.accounts.constants import RoleChoices


class GroupAdminForm(forms.ModelForm):
    name = forms.ChoiceField(choices=RoleChoices.choices, label=_("Name"))

    class Meta:
        model = Group
        fields = ("name", "permissions")
