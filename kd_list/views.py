from django.shortcuts import render
from django.http import HttpResponse
from kd_list.models import Problem_kd,UserProfile
from .forms import KdForm,UserProfileForm,UserForm,KdAdmForm
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.utils import timezone 

# Create your views here.

def list_all(request):
   kd_l = Problem_kd.objects.all()
   user = request.user
   anon = user.is_anonymous
   if not anon:
      
      kd_user = Problem_kd.objects.filter(author=user)
      return render(request, "kd_list.html", {"kd_l":kd_l,"kd_user":kd_user})
   else: 
       return render(request, "kd_list.html", {"kd_l":kd_l})
   #s=""
   #for kd in kd_l:
   #    s+= kd.title + "<br>"   
 


def kd(request, pk):
   one_kd = Problem_kd.objects.get(id = pk)
   #s=one_kd.kd
   
   return render(request, "one_kd.html", {"one_kd":one_kd}) 





def register(request):
    
   
    # Like before, get the request's context.
    
    
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
               
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True                  
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def profile(request):
   
   user = request.user
   user_id  = user.id  
   profile = UserProfile.objects.get(user_id= user_id)
   return render(request, 'profile.html',{'profile':profile})



def kd_remove(request, pk):
    kd = get_object_or_404(Problem_kd, id=pk)
    kd.delete()
    return redirect('list_all')


def kd_new(request):
    
    kd = Problem_kd.objects.order_by('-created_date')
    if request.method == "POST":
        if request.user.is_superuser:

            form = KdAdmForm(request.POST,instance = kd) 
            if form.is_valid():  
                  kd=Problem_kd.objects.create(author = request.user,title=form.cleaned_data["title"],text=form.cleaned_data["text"],kd=form.cleaned_data["kd"],state_kd=form.cleaned_data["state_kd"])
                  kd.save()
        else:
            form = KdForm(request.POST,instance = kd)
            if form.is_valid():  
                  kd=Problem_kd.objects.create(author = request.user,title=form.cleaned_data["title"],text=form.cleaned_data["text"],kd=form.cleaned_data["kd"])
                  kd.save()       
        return redirect('list_all')
    else:
        if request.user.is_superuser:
           form = KdAdmForm()
        else:
           form = KdForm()
    return render(request, 'kd_edit.html', {'form': form})

def kd_edit(request, pk):
    kd = Problem_kd.objects.get( id=pk)


    if request.method == "POST":
       

        if request.user.is_superuser:

            form = KdAdmForm(request.POST,instance = kd)
        else:
            form = KdForm(request.POST,instance = kd)
        

        if form.is_valid():
            kd = form.save(commit=False)
            kd.author = request.user
            kd.published_date = timezone.now()
            kd.save()
            form.save_m2m()
            return redirect('kd', pk=kd.id)
    else:
         if request.user.is_superuser:
             form = KdAdmForm()
         else:
             form = KdForm()
    return render(request, 'kd_edit.html',{'form': form})
