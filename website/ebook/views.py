from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Video_lession,EbookCollection,Booking_class,ViartualCounselling,SpeaekingPartner,ShortTrick,ShortTrickGet,ContactUs
from django.conf import settings
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
import random


# Create your views here.
def home(request):

    return render(request, 'home.html')

def about_us(request):
    return render(request,'about_us.html')
def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact=ContactUs.objects.all()
        for object in contact:
            if (subject==object.subject) &(message==object.message) &(email==object.email):
                messages.info(request,'Your already submit this message and subject !!!')
                return render(request, 'contact_us.html')


        contact_us=ContactUs(name=name,phone=phone,email=email,subject=subject,message=message)
        contact_us.save()
        return render(request, 'contact_us.html')

    return render(request,'contact_us.html')
def services(request):
    return render(request,'services.html')

def newform(request,myid):
    my=EbookCollection.objects.filter(id=myid)
    # order_id = request.session.get('order_id')

    amount=my.first().price
    book_name = my.first().book_name

    pdf=False


    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amount),
        'item_name': book_name,
        # 'invoice': '1234',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'new.html', {'id': my,'pdf':pdf, 'form': form})






def live_session(request):
    return render(request, 'live_session.html')
def booking_class(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        country = request.POST['country']
        city = request.POST['city']
        booking=Booking_class.objects.all()
        for persion in booking:
            if email==persion.email:
                messages.info(request, 'Your class  have already booked ! we will notify for more datail !! check your email for more datail')
                return render(request, 'home.html')




        book_class=Booking_class(name=name,phone=phone,email=email,data=date,city=city ,country=country)
        book_class.save()
        messages.info(request, 'Your class  has been booked successfully! we will notify for more datail !  check your email for more datail')
        return render(request, 'home.html')


    return render(request,'booking_class.html')

def virtual_counselling(request):

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        country = request.POST['country']
        city = request.POST['city']
        Ielts=request.POST['ielts']

        vitrual_class=ViartualCounselling.objects.all()
        for persion in vitrual_class:
            if email==persion.email:
                messages.info(request, 'Your class  have already booked virtual counselling ! we will notify for more datail ! check your email for more datail')
                return render(request, 'home.html')

        book_class=ViartualCounselling(name=name,phone=phone,email=email,city=city ,country=country,ielts_before=Ielts)
        book_class.save()
        messages.info(request, 'Your virtual counselling   has been booked successfully! we will notify for more datail !  check your email for more datail')
        return render(request, 'home.html')


    return render(request, 'virtual.html')
def videos_lession(request):

    length=Video_lession.objects.all()
    return render(request, 'video_lession.html',{'video':length})
def speaking_partner(request):


    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        country = request.POST['country']
        city = request.POST['city']
        booking=SpeaekingPartner.objects.all()
        for persion in booking:
            if email==persion.email:
                messages.info(request, 'Your speaking partner  have already booked ! we will notify for more datail !! check your email for more datail')
                return render(request, 'home.html')




        book_class=SpeaekingPartner(name=name,phone=phone,email=email,city=city ,country=country)
        book_class.save()
        messages.info(request, 'Your speaking partner  has been booked successfully! we will notify for more datail !  check your email for more datail')
        return render(request, 'home.html')


    return render(request, 'speaking_partner.html')
def Essay_correction(request):
    return render(request, 'Essay_correction.html')
def mock_test(request):
    return render(request, 'mock_test.html')
def short_trick(request):
    tricks=ShortTrick.objects.all()
    tricks=random.choices(tricks, k=3)
    if request.method == 'POST':
        email = request.POST['email']
        emails=ShortTrickGet.objects.all()
        for email1 in emails:
            if email == email1.email:
                messages.info(request, 'Your already join with us !! be get daily tricks ')
                return render(request, 'short_trick.html',{'tricks':tricks})


        get_trick=ShortTrickGet(email=email)
        get_trick.save()

        messages.info(request,'Your will be get daily tricks ')
        return render(request, 'short_trick.html',{'tricks':tricks})




    return render(request, 'short_trick.html',{'tricks':tricks})


def ebookCollection(request):

    ebook=EbookCollection.objects.all()
    return render(request,'ebookCollection.html',{'collection':ebook})




@csrf_exempt
def payment_done(request):



    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):

    return render(request, 'payment_cancelled.html')




