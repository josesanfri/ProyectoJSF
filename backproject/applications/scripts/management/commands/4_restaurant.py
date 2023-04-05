# Python imports
import random , time

# Django imports
from django.core.management.base import BaseCommand

# Local imports
from applications.base.restaurant.models import Restaurant, MediaRestaurant
from applications.base.user.models import User
from applications.base.location.models import Address

class Command(BaseCommand):
    help = 'Register 20 different users to do tests'

    def handle(self, *args, **options):
      
        start_time = time.process_time()
      

        # Properties
        staff_set = User.objects.filter(type_user=User.STAFF)
        address_set = Address.objects.all()

        counter = 20
        random.randint(0, len(address_set)) 

        for i in range(counter):

            restaurant = Restaurant()
            restaurant.address = address_set[random.randint(0, (len(address_set)-1))]
            restaurant.name_restaurant = "La esquina Gourmet",
            restaurant.square_meters = random.randint(40,150)
            restaurant.caption_user = staff_set[random.randint(0, (len(staff_set)-1))]
            restaurant.primary_phone = str(random.randint(100000000, 999999999));

            restaurant.save()

            self.stdout.write(self.style.SUCCESS('Successfuly registered restaurant: %s' % restaurant))

        print("--- %s  ---" % (time.process_time() - start_time)) 








        

