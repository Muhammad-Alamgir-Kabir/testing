from django import forms 

class ContactForm(forms.Form):
   

    name=forms.CharField(label="Full Name: ",help_text="Enter Name",widget=forms.Textarea(attrs={'placeholder': 'Enter Your Nmae'}))
    email=forms.EmailField()
    age=forms.IntegerField()
    weight=forms.FloatField()
    balance=forms.DecimalField()
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.TimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    size=forms.ChoiceField(choices=[('S','Small'),('M','Medium'),('L','Large')], widget=forms.RadioSelect)    
    pizza=forms.MultipleChoiceField(choices=[('P','Pepperoni'),('C','Cheese'),('M','Mushroom')],widget=forms.CheckboxSelectMultiple)    
    file=forms.FileField()
    check=forms.BooleanField()

    



