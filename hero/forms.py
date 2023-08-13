from django import forms


class CharacterForm(forms.Form):
    strength = forms.IntegerField(min_value=0, initial=20)
    dexterity = forms.IntegerField(min_value=0, initial=20)
    health = forms.IntegerField(min_value=0, initial=20)
    intelligence = forms.IntegerField(min_value=0, initial=20)
    charisma = forms.IntegerField(min_value=0, initial=20)

    def clean(self):
        cleaned_data = super().clean()
        total = (
            cleaned_data.get("strength", 0)
            + cleaned_data.get("dexterity", 0)
            + cleaned_data.get("health", 0)
            + cleaned_data.get("intelligence", 0)
            + cleaned_data.get("charisma", 0)
        )

        if total > 100:
            raise forms.ValidationError("The total attributes must not exceed 100.")
        return cleaned_data
