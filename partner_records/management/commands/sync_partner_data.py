from configparser import ConfigParser

import psycopg2
from django.core.management.base import BaseCommand

from oplus import settings
from partner_records.utils import bcolors, connect, count_partner_patient_data_records, count_partner_doctor_notes


class Command(BaseCommand):
    help = "Sync Partner Data"

    def add_arguments(self, parser):
        parser.add_argument('partner', nargs='+')



    def handle(self, *args, **options):
        connect()
        count_partner_patient_data_records()
        count_partner_doctor_notes()
        for partner in options['partner']:
            print(bcolors.OKBLUE + f"Syncing {partner} data" + bcolors.ENDC)
            self.stdout.write(( bcolors.OKBLUE + 'Connection String "%s"' + bcolors.ENDC  ) % settings.DATABASES['partner'])
            self.stdout.write( (bcolors.OKGREEN + 'Successfully synced partner "%s"' + bcolors.ENDC  ) % partner)

