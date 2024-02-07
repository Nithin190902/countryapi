import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "countryapi.settings")  # Replace 'your_project.settings' with your actual project's settings module

import django
django.setup()

from faker import Faker
from countries.models import Country  # Replace 'your_app.models' with the path to your actual Django model

fake = Faker()

def populate_database(num_records):
    for _ in range(num_records):
        fake_name = fake.name()
        fake_capital = fake.city()
        fake_area = fake.random_int(min=10000, max=1000000)

        # Create an instance of your Django model and save it to the database
        Country.objects.create(name=fake_name, capital=fake_capital, area=fake_area)

if __name__ == "__main__":
    num_records_to_create = 100  # Adjust the number of records you want to create
    populate_database(num_records_to_create)
