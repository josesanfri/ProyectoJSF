# Django imports
from django.db.migrations import Migration
from django.contrib.postgres.operations import UnaccentExtension, TrigramExtension

class Migration(Migration):

    operations = [
        UnaccentExtension(),
        TrigramExtension(),
    ]