import os
import sys
import django

# Add project directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the environment variable for Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')  # Ensure this matches your project name

# Initialize Django
django.setup()

# Import your models after Django is set up
from restaurant.models import MenuItem

# Your fake data generation logic goes here
from faker import Faker

fake = Faker()

def create_fake_menu_items():
    for _ in range(30):
        title = fake.word(ext_word_list=['Burger', 'Pizza', 'Pasta', 'Salad', 'Sushi', 'Tacos'])
        price = round(fake.random_number(digits=4) / 100, 2)
        inventory = fake.random_int(min=1, max=100)

        MenuItem.objects.create(
            title=title,
            price=price,
            inventory=inventory
        )

if __name__ == "__main__":
    create_fake_menu_items()
    print("Fake data generated.")
