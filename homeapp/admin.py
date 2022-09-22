from django.contrib import admin


from homeapp.models import Departments, Doctors, Booking
from homeapp.views import doctor

admin.site.register(Departments)
admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):
    list_display =('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')

admin.site.register(Booking, BookingAdmin)