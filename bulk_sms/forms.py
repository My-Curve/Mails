from django import forms



class SmsForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
    
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise forms.ValidationError('Phone number must start with a +')
        return phone_number