# Python imports
import random , time

# Django imports
from django.core.management.base import BaseCommand

# Local imports
from applications.base.lead.models import ContactForm, JobApplication

class Command(BaseCommand):
    help = 'Register leads in different offices to do tests'

    def handle(self, *args, **options):
        start_time = time.process_time()
      
        # ContactForm
        for i in range (5):
            contact_form = ContactForm.objects.create(
                name = "test_"+str(i+1),
                email = "test_"+str(i+1)+"@mail.com",
                prefix_phone = "34",
                phone = "64665262"+str(i),
                surname = "contactForm",
                information = "Here will come information of a person who wants to contact us"
            )
            self.stdout.write(self.style.SUCCESS('Successfuly registered ContactForm to  %s' % contact_form.email))
        
    
        # job request
        counter = 10
      
        cities = ["Valencia","Granada","Sevilla"]

        for i in range (counter):
            job = JobApplication()
            job.city = random.choice(cities)
            job.name = "Job" + str(i)
            job.email = "Job"+str(i)+"@gmail.com"
            job.prefix_phone = "34"
            job.phone = "62723324"+str(i)
            job.type_job = 'J'
            job.NIF = "33563635N"
            job.age = "33"
            job.origin = "Moroco"
            job.studies = "English"
            job.curriculum = "C:\\Users\\d4b\\Downloads\\hola.pdf"
            job.information = "Im the best"
            job.save()
                    
            self.stdout.write(self.style.SUCCESS('Successfuly registered user: %s' % job))
      
        print("--- %s  ---" % (time.process_time() - start_time))
        