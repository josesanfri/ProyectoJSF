import random

# Django imports
from django.core.management.base import BaseCommand

# Local imports
from applications.base.location.models import Zone, Address

class Command(BaseCommand):
    help = 'Inserts various zones and locations'

    def handle(self, *args, **options):
        # ZONES
        Zone(name='Valencia', description = 'La paella es la paella es la paella', assigned_postal_codes = ['46001', '46002', '46003', '46004', '46005', '46006', '46007', '46008', '46009', '46010', '46011', '46012', '46013', '46014', '46015', '46016', '46017', '46018', '46019', '46020', '46021', '46022', '46023', '46024', '46025', '46026', '46035', '46070', '46071', '46080', '46116'] ).save()
        Zone(name='Sevilla', description = 'La giralda es la giralda es la giralda', assigned_postal_codes = ['41001', '41002', '41003', '41004', '41005', '41006', '41007', '41008', '41009', '41010', '41011' , '41012', '41013', '41014', '41015', '41016', '41017', '41018', '41019', '41020', '41070', '41071', '41080', '41092', '41300'] ).save()
        Zone(name='Granada', description = 'La alhambra es la alhambra es la alhambra', assigned_postal_codes = ['18001', '18002', '18003', '18004', '18005', '18006', '18007', '18008', '18009', '18010', '18011', '18012', '18013', '18014', '18015', '18016', '18070', '18071', '18080'] ).save()
               
        # ADDRESS
        zones = Zone.objects.all()

        list_address = [
            ['Avenida', 'Calle', 'Paseo', 'Bulevar'],
            ['Actor', 'Poeta', 'Escritor', 'Pintor'],
            ['Vicente', 'Tomás', 'Javier', 'Piero'],
        ]

        num_address = 10

        for zone in zones:
            
            for n in range(num_address):
                address = Address()
                address.country = 'España'
                address.street = list_address[0][random.randint(0,3)] + ' del ' + list_address[1][random.randint(0,3)] + ' ' + list_address[2][random.randint(0,3)]
                address.number = random.randint(1,99)
                address.floor = n
                address.door = (n+2)

                if str(zone).startswith('Val'):
                    address.region = 'Comunidad Valenciana'
                    address.sub_region = 'Valencia'
                    address.city = 'Valencia'
                    address.postal_code = '46001'
                    address.latitude = float('39.4' + str(n) + '5984')
                    address.longitude = float('-0.3' + str(n) + '6582')
                    address.zone = zone
        
                if str(zone).startswith('Sev'):
                    address.region = 'Andalucia'
                    address.sub_region = 'Sevilla'
                    address.city = 'Sevilla'
                    address.postal_code = '41001'
                    address.latitude = float('37.3' + str(n) + '5984')
                    address.longitude = float('-5.9' + str(n) + '6582')
                    address.zone = zone

                if str(zone).startswith('Gra'):
                    address.region = 'Andalucia'
                    address.sub_region = 'Granada'
                    address.city = 'Granada'
                    address.postal_code = '18001'
                    address.latitude = float('37.1' + str(n) + '5984')
                    address.longitude = float('-3.6' + str(n) + '6582')
                    address.zone = zone

                else:
                    address.zone = zone
                    
                address.save()

                self.stdout.write(self.style.SUCCESS('Successfuly inserted Address: %s' % address))
                