from django.contrib import admin
from .models import CatProfile, AnimalColoration, Litter, Culture, Title, Gallery, HashTag, HomeGallery, Kitten, \
    Citation

# Register your models here.
admin.site.register(CatProfile)
admin.site.register(AnimalColoration)
admin.site.register(Litter)
admin.site.register(Culture)
admin.site.register(Title)
admin.site.register(Gallery)
admin.site.register(HashTag)
admin.site.register(HomeGallery)
admin.site.register(Kitten)
admin.site.register(Citation)

