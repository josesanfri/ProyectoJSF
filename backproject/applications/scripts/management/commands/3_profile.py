# Django imports
from django.core.management.base import BaseCommand
from applications.base.location.models import Address

# Local imports
from applications.base.profileUser.models import CustomerProfile, StaffProfile , Department
from applications.base.user.models import User

# python imports
import random , time

class Command(BaseCommand):
    help = 'Register different profiles to do tests for all users in database '

    def handle(self, *args, **options):
      
      start_time = time.process_time()
              
      msg = """ Alert :
      To add profiles it is necessary to have users created before, this script will not work if no users are detected in any of their types (renter,owner,profile,staff). 
          You need to run the command "python manage.py 1_users" first
      It is also necessary to have addresses, first execute the command 'python manage.py 2_location'
      
      """
      customers =  User.objects.filter(type_user = User.CUSTOMER)
      staff =  User.objects.filter(type_user = User.STAFF)
      adresses = Address.objects.all()

      if not customers or not staff or not adresses :
        print("\n\n",msg)
        return None
      
      # renters profiles
      
      for customer in customers :

        customer_profile = CustomerProfile.objects.create(
          user = User.objects.get(id=customer.id),
          first_name = (customer.email).split("@")[0],
          last_name = "profile",
          birth_date = "1988-03-20",
          prefix_phone = "34",
          phone = "616661166",
          address =  Address.objects.get(id=adresses[random.randint(0,(len(adresses)-1))].id)
        )
        
        self.stdout.write(self.style.SUCCESS('Successfuly registered customerProfile with id  %s' % customer_profile.id))
     
      
      # staff profiles

      for stf in staff :
        
        stf_profile = StaffProfile.objects.create(
          user = User.objects.get(id=stf.id),
          first_name = (stf.email).split("@")[0],
          last_name = "profile",
          birth_date = "1988-03-20",
          prefix_phone = "34",
          phone = "616661166",
          address =  Address.objects.get(id=adresses[random.randint(0,(len(adresses)-1))].id),
        )
        
        self.stdout.write(self.style.SUCCESS('Successfuly registered staffProfile with id  %s' % stf_profile.id))  
        
      print("--- %s  ---" % (time.process_time() - start_time))