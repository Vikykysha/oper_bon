from django import forms
from .models import Problem_kd,UserProfile
from django.contrib.auth.models import User



class KdForm(forms.ModelForm):
    
    class Meta:
         model = Problem_kd
         fields = ('title','text','kd',)
    


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
    
    
    

