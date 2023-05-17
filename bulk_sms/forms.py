from django.forms import forms



class SmsForm(forms.Form):
    message = forms.CharField(max_length=160)
    phone_number = forms.CharField(max_length=12)
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise forms.ValidationError('Phone number must start with a +')
        return phone_number