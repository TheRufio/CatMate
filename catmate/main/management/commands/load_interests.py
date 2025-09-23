from django.core.management.base import BaseCommand
from main.models import Interes
import csv

class Command(BaseCommand):
    help = "Load interests from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name = row[0].strip()
                if name:
                    Interes.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS("Interests loaded successfully!"))
