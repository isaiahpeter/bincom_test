from django import forms

LGA_CHOICES = (
        (1, 'Aniocha North'),
        (2, 'Aniocha - South'),
        (5, 'Ethiope East'),
        (6, 'Ethiope West'),
        (7, 'Ika North - East'),
        (8, 'Ika - South'),
        (9, 'Isoko North'),
        (10, 'Isoko South'),
        (11, 'Ndokwa East'),
        (12, 'Ndokwa West'),
        (13, 'Okpe'),
        (14, 'Oshimili - North'),
        (15, 'Oshimili - South'),
        (16, 'Patani'),
        (17, 'Sapele'),
        (18, 'Udu'),
        (19, 'Ughelli North'),
        (20, 'Ughelli South'),
        (21, 'Ukwuani'),
        (22, 'Uvwie'),
        (31, 'Bomadi'),
        (32, 'Burutu'),
        (33, 'Warri North'),
        (34, 'Warri South'),
        (35, 'Warri South West')
    )


class AddPollingUnitResultForm(forms.Form):
    polling_unit_unique_id = forms.IntegerField()
    party_abbreviation = forms.CharField()
    party_score = forms.IntegerField()
    entered_by_user = forms.CharField(label='Agent Name')
    user_ip_address = forms.CharField()


class PollingUnitForm(forms.Form):
    polling_unit_unique_id = forms.CharField(label='Select Local Government',widget=forms.Select(choices=LGA_CHOICES))
 
class PollResultForm(forms.Form):
    polling_unit_id = forms.IntegerField(label='Enter Polling Unit Id')