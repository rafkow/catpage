from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image
from io import StringIO, BytesIO
from datetime import datetime
from sys import getsizeof


class AnimalColoration(models.Model):
    name = models.CharField(max_length=50, null=False)
    short = models.CharField(max_length=3, null=True)
    number = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.short}{self.number} - {self.name}'


class Culture(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.name}'


class Title(models.Model):
    short = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=40, null=False)

    def __str__(self):
        return f'{self.short} - {self.name}'

    def to_description(self):
        return f'{self.short}'


class Citation(models.Model):
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=50, null=True, blank=True)


def fit_image_profile(picture):
    img = Image.open(picture)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    area = tuple()
    if picture.width >= 5 * picture.height / 3:
        x = picture.width - 5 * picture.height / 3
        area = (x/2, 0, x/2 + 5 * picture.height / 3, picture.height)
    else:
        y = picture.height - 3 * picture.width / 5
        area = (0, y/2, picture.width, y/2 + 3*picture.width/5)
    print(area)
    img = img.crop(area)
    img.thumbnail((img.width, img.height), Image.ANTIALIAS)
    output = BytesIO()
    img.save(output, format='JPEG', quality=80)
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField',
                                f"{picture.name.split('.')[0]}_min.jpeg",
                                'image/jpeg', getsizeof(output), None)


class CatProfile(models.Model):
    name = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True, default=None)
    culture = models.ForeignKey(Culture, related_name='cats', null=True, default=None, blank=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(AnimalColoration, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    mother = models.ForeignKey('self', related_name='born', null=True, default=None, blank=True, on_delete=models.SET_NULL)
    father = models.ForeignKey('self', related_name='impregnated', null=True, default=None, blank=True, on_delete=models.SET_NULL)
    sexes = [('1,0', 'Male'), ('0,1', 'Female')]
    sex = models.CharField(max_length=5, choices=sexes, null=True, default=None)
    title = models.ForeignKey(Title, related_name='laureate', null=True, default=None, blank=True, on_delete=models.SET_NULL)
    birth = models.DateField(blank=True, null=True, default=None)
    weight = models.SmallIntegerField(default=0, null=True, blank=True)
    litter = models.ForeignKey('Litter',  related_name='family', null=True, blank=True, on_delete=models.SET_NULL)
    is_with_us = models.BooleanField(default=True)
    display = models.BooleanField(default=True)

    def check_title(self):
        return f'{self.title.short} ' if self.title else ''

    def check_culture(self):
        return f'{self.culture} ' if self.color else ' '

    def sex_explanation(self):
        return 'kocur' if self.sex == '1,0' else 'kotka'

    def life_time(self):
        if self.birth:
            delta = (datetime.date(datetime.now()) - self.birth).days
            if delta == 1:
                return f'{delta} dzień'
            if delta < 22:
                return f'{delta} dni'
            if delta < 35:
                return f'{int(delta/7)} tygodnie'
            if delta < 106:
                return f'{int(delta / 7)} tygodni'
            if delta < 800:
                return f'{(datetime.now().year - self.birth.year) * 12 + (datetime.now().month - self.birth.month)} miesięcy'
            return f'{(datetime.now().year - self.birth.year)} lata'
        return ''

    def __str__(self):
        return f'{self.check_title()}{self.name} {self.check_culture()}{self.color}'

    def save(self, *args, **kwargs):
        self.image = fit_image_profile(self.image) if self.image else None
        super(CatProfile, self).save(*args, **kwargs)


class Litter(models.Model):
    name = models.CharField(max_length=30, null=True)
    mother = models.ForeignKey(CatProfile, related_name='+', null=True, on_delete=models.SET_NULL,
                               limit_choices_to={'sex': '0,1'})
    father = models.ForeignKey(CatProfile, related_name='+', null=True, on_delete=models.SET_NULL,
                               limit_choices_to={'sex': '1,0'})
    birth = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.name} {self.birth}'


class LitterPhoto(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='litter/')


class Kitten(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='kitten/', blank=True)
    litter = models.ForeignKey(Litter, related_name='children', null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.image = fit_image(self.image) if self.image else None
        super(Kitten, self).save(*args, **kwargs)


class HashTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


def fit_image(picture):
    img = Image.open(picture)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.thumbnail((picture.width / 1.5, picture.height / 1.5), Image.ANTIALIAS)
    output = BytesIO()
    img.save(output, format='JPEG', quality=80)
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField',
                                f"{picture.name.split('.')[0]}.jpeg",
                                'image/jpeg', getsizeof(output), None)


def fit_image_miniature(picture):
    img = Image.open(picture)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.thumbnail((350, int((350/picture.width) * picture.height)), Image.ANTIALIAS)
    output = BytesIO()
    img.save(output, format='JPEG', quality=80)
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField',
                                f"{picture.name.split('.')[0]}_min.jpeg",
                                'image/jpeg', getsizeof(output), None)


class Gallery(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    image_min = models.ImageField(upload_to='gallery/min/', default=None, blank=True)
    who_is_in = models.ManyToManyField(CatProfile, related_name='on_picture', blank=True)
    tag = models.ManyToManyField(HashTag, related_name='photos', blank=True)

    def __str__(self):
        return f'{self.image} {self.name}'

    def save(self, *args, **kwargs):
        self.image_min = fit_image_miniature(self.image)
        self.image = fit_image(self.image) if self.image else None
        super(Gallery, self).save(*args, **kwargs)

    def get_filters(self):
        result = ''
        if self.tag:
            filters = ['filter-'+tag.name for tag in self.tag.all()]
            for filter in filters:
                result = result + f' {filter}'
        return f'{result}'

    def get_hashtags(self):
        result = ''
        if self.tag:
            filters = ['#'+tag.name for tag in self.tag.all()]
            for filter in filters:
                result = result + f' {filter}'
        return f'{result}'


class HomeGallery(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='home/')



