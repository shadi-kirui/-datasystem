# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import LivestockFarmer, FodderFarmer, Borehole, HayStorage, CapacityBuilding
from django.contrib import messages
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

def loginuser(request):
    page ='login'
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'Username does not exist!')
        user = authenticate(request,username = username, password = password)
        if user != None:
            login(request,user)
            return redirect('dashboard')  
        else:
            messages.error(request,'User name or Password not correct!')      
    context = {'page':page}
    return render(request,'login.html',context)


def registeruser(request):
    form  = UserCreationForm()
    if request.method == 'POST':#this is used to listen to the request from the client or we can say check the request send to the server
        form = UserCreationForm(request.POST)#This line binds the data submitted by the client to the UserCreationForm 
        if form.is_valid():#preparing it for validation
            user = form.save(commit=False)#When commit=False is passed, the form creates the user object but does not yet save it to the database. Instead, it returns the user object, allowing you to modify it before saving it.
            '''Why Use commit=False
                You may need to make additional changes to the user object before saving it, such as:
                Setting additional fields (e.g., is_active, profile_picture, etc.).
                Associating it with related objects or performing other custom logic.'''
            user.username = user.username.lower()
            user.save()
            return redirect('dashboard')
        else:
            messages.error(request,'An error has occurred pleas try again...')
    return render(request,'login.html',{'form':form})

def logoutuser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def dashboard(request):
    # Fetch all LivestockFarmer objects for display if needed
    livestock_data = LivestockFarmer.objects.all()

    if request.method == "POST":
        try:
            with transaction.atomic():  # Ensures all changes happen or none
                # 1. Livestock Farmers
                LivestockFarmer.objects.create(
                    name=request.POST.get('lf-name', '').strip(),
                    id_no=request.POST.get('lf-id', '').strip(),
                    phone_no=request.POST.get('lf-phone', '').strip(),
                    location=request.POST.get('lf-location', '').strip(),
                    male_goats=int(request.POST.get('lf-male', '0') or 0),
                    female_goats=int(request.POST.get('lf-female', '0') or 0),
                    weekly_offtake=int(request.POST.get('lf-offtake', '0') or 0),
                    amount_paid=float(request.POST.get('lf-amount', '0') or 0),
                    vaccin_type=request.POST.get('lf-vaccin', '').strip(),
                    date_administered=request.POST.get('lf-vaccine', '').strip(),
                    goats_given=int(request.POST.get('lf-breeding-no', '0') or 0),
                    tracking_traceability=request.POST.get('lf-traceability', '').strip()
                )

                # 2. Fodder Farmers
                FodderFarmer.objects.create(
                    name=request.POST.get('ff-name', '').strip(),
                    id_no=request.POST.get('ff-id', '').strip(),
                    phone_no=request.POST.get('ff-phone', '').strip(),
                    location=request.POST.get('ff-location', '').strip(),
                    land_acreage_leased=float(request.POST.get('ff-leased', '0') or 0),
                    land_acreage_sharing_model=request.POST.get('ff-sharing', '').strip(),
                    yield_per_harvest=float(request.POST.get('ff-yield', '0') or 0)
                )

                # 3. Infrastructure
                Borehole.objects.create(
                    location=request.POST.get('infra-location', '').strip(),
                    water_used=float(request.POST.get('infra-water', '0') or 0),
                    people_using=int(request.POST.get('infra-people', '0') or 0)
                )

                HayStorage.objects.create(
                    bales_stored=int(request.POST.get('infra-bales-stored', '0') or 0),
                    bales_given_or_sold=int(request.POST.get('infra-bales-sold', '0') or 0),
                    revenue_made=float(request.POST.get('infra-revenue', '0') or 0)
                )

                # 4. Capacity Building
                CapacityBuilding.objects.create(
                    trainings_count=int(request.POST.get('cb-trainings', '0') or 0),
                    modules=request.POST.get('cb-modules', '').strip()
                )

                # Add success message
                messages.success(request, "Data submitted successfully!")
                return redirect('dashboard')  # Redirect to the dashboard view

        except Exception as e:
            # Log and show the error message
            logger.error(f"Error submitting data: {e}")
            messages.error(request, f"Error submitting data: {str(e)}")
            return redirect('dashboard')
    if request.method == "POST":
        try:
            LivestockFarmer.objects.create(
                age_range = request.POST.get('age_range'),
                age_count = int(request.POST.get('age_count', 0)),
                weight_range = request.POST.get('weight_range'),
                weight_count = int(request.POST.get('weight_count', 0)),
            )

                # Update or Create Farmer Data
        
            messages.success(request, "Data saved successfully!")
        except Exception as e:
            messages.error(request, f"Error saving data: {e}")

    # Fetch All Data
    farmers = LivestockFarmer.objects.all()

    # Render the template
    return render(request, 'new.html', {'livestock_data': livestock_data,'farmers': farmers})
