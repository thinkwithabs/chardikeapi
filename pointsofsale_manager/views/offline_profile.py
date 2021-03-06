
'''
this file contains pos logic
    - createview

'''
from accounts.models.profile import Profile
from orders.database.cart_order import Order
from pointsofsale_manager.serializers.pos_profile_serializers import UserOfflineProfileSerializers
from pointsofsale_manager.serializers.pos_info_serializers import (
    OrderAPI_POS
)
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import  Response

from rest_framework import status
from rest_framework.decorators import permission_classes
from django.contrib.auth.hashers import make_password
from MainApplication.scripts.phone_SMS_settings import SMS_for_Phone_Message

from accounts.models.user_model import User


'''
Logic for offline(pos) profile create
'''

class OfflineProfileCreateView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserOfflineProfileSerializers

    def post(self,request):
        phone = request.data.get('phone')
        password = "123456" 

        apifetch = UserOfflineProfileSerializers(data=request.data)
        if apifetch.is_valid():
            if Profile.objects.filter(phone=apifetch.validated_data['phone']):
                    return Response(
                        {'Error':'Phone Number Already in Used'},
                    status= status.HTTP_406_NOT_ACCEPTABLE)
            else:
                authInfo = {
                    'password':make_password(password),
                    'confirm_password':make_password(password)
                    }
                user = User(**authInfo)
                user.save()
            
            apifetch.validated_data['user'] = user
            apifetch.save()
            
            profile_ID=user.profile.id

            p = Profile.objects.get(id=profile_ID)
            p.is_phone_verified = True
            p.save()

            message = f"Thanks for joining Charike.com \n Your Phone Number is {phone} \n Your Password is {password} \
                            \n You can change the Password in your dashboard"
            SMS_for_Phone_Message(phone,message).start()

            return Response(
                    {'Success':'Profile is created','profile_ID': profile_ID},
                status=status.HTTP_201_CREATED)
        else:
            return Response(apifetch.errors)
        




'''
Point of Sale of
    Order Method
'''

class POS_OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderAPI_POS