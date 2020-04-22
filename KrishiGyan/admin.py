from django.contrib import admin

from .models import Crops,Diseases,Pesticides,PesticideDisease,Rating,Question,Answers

admin.site.register(Crops)

admin.site.register(Diseases)

admin.site.register(PesticideDisease)

admin.site.register(Pesticides)
 
admin.site.register(Rating)

admin.site.register(Question)
 
admin.site.register(Answers)