from django.contrib import admin
from .models import CustomUser, Jobs, Bids, Funds
# Register your models here
admin.site.register(CustomUser)
admin.site.register(Jobs)
admin.site.register(Bids)
admin.site.register(Funds)
