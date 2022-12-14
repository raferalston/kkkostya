from django.core.management.base import BaseCommand
from rating.models import Rating
class Command(BaseCommand):
    help = "deleting some entries to rating model"
    def handle(self, *args, **options):
        print(args, options)
        Rating.objects.filter(text="created from command line").delete()