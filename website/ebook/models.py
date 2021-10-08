from django.db import models

# Create your models here.



class Video_lession(models.Model):
    youtube_link=models.CharField(max_length=1200)
    title=models.CharField(max_length=300)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.title



class ViartualCounselling(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    ielts_before=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SpeaekingPartner(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name







class EbookCollection(models.Model):
    book_name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    book=models.FileField(upload_to='ebook')
    price=models.IntegerField()

    def __str__(self):
        return self.book_name
class Booking_class(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    data=models.DateField()
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    def __str__(self):
        return self.name



class ShortTrick(models.Model):


    Question=models.CharField(max_length=500)
    ans=models.CharField(max_length=2000)
    file=models.FileField(upload_to='Tricks')
    sub=models.CharField(max_length=100)

    def __str__(self):
        return self.sub



class ShortTrickGet(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email


class ContactUs(models.Model):

    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=300)
    def __str__(self):
        return self.name





