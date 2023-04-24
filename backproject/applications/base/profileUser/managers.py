# Django imports
from django.db.models import Manager, Q

class ProfileManager(Manager):
    def search_complete_name(self, kword):
        return self.filter(
            Q(first_name__unaccent__trigram_similar=kword) | Q(last_name__unaccent__trigram_similar=kword)
        )
    