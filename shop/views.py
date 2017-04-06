from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from shop.forms import UserForm, SignInForm, SearchForm


# the function executes with the signup url to take the inputs
def home(request):
    sign_up_form = UserForm() 
    search_form  = SearchForm()
    sign_in_form = SignInForm()
    context = {'sign_in_form':sign_in_form,'sign_up_form': sign_up_form, 'search_form':search_form}
    return render(request, 'shop/home.html', context)

def signup(request):
    if request.method == 'POST':  # if the form has been filled
        sign_up_form = UserForm(request.POST)
        # import pdb; pdb.set_trace()
        if sign_up_form.is_valid():  # All the data is valid
            first_name = sign_up_form.cleaned_data['first_name']
            last_name = sign_up_form.cleaned_data['last_name']
            email = sign_up_form.cleaned_data['email']
            password = sign_up_form.cleaned_data['password']
            if sign_up_form.clean_mail(email) == False or sign_up_form.clean_pwd(password) == False:
                sign_in_form = SignInForm()
                context = {'sign_up_form': sign_up_form, 'sign_in_form':sign_in_form}
                return render(request, 'shop/home.html', context)    
            else:
                user = User.objects.create_user(username=email,first_name=first_name, last_name=last_name, password=password)
                user.save()
                if User.objects.get_or_create(username = email):
                    return redirect('shop:profile')
                else:
                    sign_in_form = SignInForm()
                    context = {'sign_up_form': sign_up_form, 'submit_error':'Something went wrong! Try Again', 'sign_in_form':sign_in_form}
                    return render(request, 'shop/home.html', context)
        else:
            sign_in_form = SignInForm()
            context = {'sign_up_form': sign_up_form, 'sign_in_form':sign_in_form}
            return render(request, 'shop/home.html', context)
    else:
        sign_up_form = UserForm()
        sign_in_form = SignInForm()  # an unboundform
        context = {'sign_in_form':sign_in_form,'sign_up_form': sign_up_form}
        return render(request, 'shop/home.html', context)

def signin(request):
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            email = sign_in_form.cleaned_data['email']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:profile')
            else:
                sign_up_form = UserForm()
                context = {'wrong_credentials':'Wrong Email or Password', 'sign_in_form':sign_in_form, 'sign_up_form':sign_up_form}
                return render(request, 'shop/home.html', context)
        else:
            sign_up_form = UserForm() 
            context = {'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form}
            return render(request, 'shop/home.html', context)
    else:
        sign_in_form = SignInForm()
        sign_up_form = UserForm()
        context = {'sign_in_form':sign_in_form,'sign_up_form': sign_up_form}
        return render(request, 'shop/home.html', context)

def profile(request):
    return render(request, 'shop/profile.html')


