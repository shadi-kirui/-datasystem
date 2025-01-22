from django import forms
from .models import LivestockFarmer, FodderFarmer, Infrastructure, CapacityBuilding

class LivestockFarmerForm(forms.ModelForm):
    class Meta:
        model = LivestockFarmer
        fields = '__all__'

class FodderFarmerForm(forms.ModelForm):
    class Meta:
        model = FodderFarmer
        fields = '__all__'

class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = '__all__'

class CapacityBuildingForm(forms.ModelForm):
    class Meta:
        model = CapacityBuilding
        fields = '__all__'
