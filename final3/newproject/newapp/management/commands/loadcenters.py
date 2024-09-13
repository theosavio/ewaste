from django.core.management.base import BaseCommand
from newapp.models import EwasteCenters
import csv
import os

class Command(BaseCommand):
    help = 'Load centers data from a CSV file'

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join(os.path.dirname(__file__), 'recycling_centers.csv')

        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for index, row in enumerate(reader, start=1):
                try:
                    name, latitude, longitude = row
                    EwasteCenters.objects.create(name=name, latitude=float(latitude), longitude=float(longitude))
                except ValueError:
                    self.stdout.write(self.style.WARNING(f'Error in row {index}: {row}'))
        
        self.stdout.write(self.style.SUCCESS('Centers data loaded successfully'))
