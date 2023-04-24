# Python imports
import time

# Django imports
from django.core.management.base import BaseCommand

# Local imports
from applications.base.user.models import User

class Command(BaseCommand):
    help = 'Register 20 different users to do tests'

    def handle(self, *args, **options):
        start_time = time.process_time()
        list_user = [
            [User.CUSTOMER, 'customer', False ],
            [User.STAFF, 'staff', True ],
        ]

        counter = 20
        divisor = int(counter/len(list_user))

        for i in range (counter):
            
            result = int(i/divisor)

            user = User()
            user.set_password('123456')
            user.type_user = list_user[result][0]
            user.email = list_user[result][1]+str(i)+'@gmail.com'
            user.is_staff = list_user[result][2]

            user.save()

            self.stdout.write(self.style.SUCCESS('Successfuly registered user: %s' % user))

        print("--- %s  ---" % (time.process_time() - start_time))
                  