# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ''
client = Client(account_sid, auth_token)

tollfree_verification = client.messaging \
    .v1 \
    .tollfree_verifications \
    .create(
         business_street_address='18545 Rio Seco Dr',
         business_street_address2='Apt A',
         business_city='Rowland Heights',
         business_state_province_region='CA',
         business_postal_code='91748',
         business_country='US',
         business_contact_first_name='Mingi',
         business_contact_last_name='Kang',
         business_contact_email='mingikang31@gmail.com.com',
         business_contact_phone='+8187952054',
         additional_information='see our privacy policy here www.johnscoffeeshop.com/privacypolicy',
         external_reference_id='abc123xyz567',
         business_name='Mingi Kang',
         business_website='https://github.com/mkang817415',
         notification_email='support@company.com',
         use_case_categories=['TWO_FACTOR_AUTHENTICATION', 'MARKETING'],
         use_case_summary="This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",
         production_message_sample='lorem ipsum',
         opt_in_image_urls=['https://zipwhiptestbusiness.com/images/image1.jpg', 'https://zipwhiptestbusiness.com/images/image2.jpg'],
         opt_in_type='VERBAL',
         message_volume='10',
         tollfree_phone_number_sid='PN+18777194154'
     )

print(tollfree_verification.sid)
