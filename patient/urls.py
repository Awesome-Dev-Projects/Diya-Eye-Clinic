from django.urls import path
from .views import index, get_otp, verify_otp, save_patient_profile

app_name='patient'

urlpatterns = [
    path('', index, name='index'),
    path('get-otp/', get_otp, name='get-otp'),
    path('verify-otp/', verify_otp, name='verify-otp'),
    path('save-patient-profile/', save_patient_profile,
         name='save-patient-profile'),
]
