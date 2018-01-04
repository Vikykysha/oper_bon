from django import forms
from .models import Problem_kd,UserProfile
from django.contrib.auth.models import User



class KdForm(forms.Form):

   
    title = forms.CharField(label="Title of the post",max_length=100,required=True)
    text= forms.CharField(label="Text of your problem",widget=forms.Textarea,required=True)
    kd_number = forms.CharField(label="Add number of kd",max_length=100,required=True)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)
    def clean_email(self):
            email = self.cleaned_data["email"]
      
            user = User.objects.filter(email=email)
            if user.exists():             
               raise forms.ValidationError("This email address already exists. Did you forget your password?")
            else:
          
               return email
            return email
    
        

  
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('skill',)
    
    
    

