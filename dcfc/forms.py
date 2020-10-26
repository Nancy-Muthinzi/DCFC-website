from django import forms


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, label="Name")
    email = forms.EmailField(max_length=500, label="Email")
    residence = forms.CharField(max_length=500, label='Area of Residence')
    comment = forms.CharField(max_length=2000, label='', widget=forms.Textarea(
        attrs={'placeholder': 'Enter your comment here'}))

        
