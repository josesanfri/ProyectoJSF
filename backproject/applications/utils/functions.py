# Python imports
import string
import random
from random import choices
from os import makedirs
from datetime import date, datetime, timedelta

# Django imports
from django.conf import settings
from django.utils.translation import gettext as _

def generate_random_string():
    n = 3
    random_string = ''.join(choices(string.ascii_letters + string.digits, k=n))
    return random_string

def generate_two_random_chars():
    n = 2
    random_string = ''.join(choices(string.ascii_uppercase, k=n))
    return random_string

def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    print(random_date)

# generate_random_date()

def log_creation(app: str, exc, context):
    """Creates a txt file were we register the errors of the website

    Args:
        app (str): Name of the app were the error occurred
        exc (Exception): The exception
        context (Request context): Context of the request, were we can find interesting data
    """
    
    today = date.today()
    path = settings.BASE_DIR / 'logs/{}/{}'.format(today.year, today.month)
    makedirs(path, exist_ok=True)
    
    with open(f"{path}/{today.day}_{app}_errors.txt", "a+",) as f:
    
        context_req = context.get('request')
        
        f.write("ERROR:\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write(f"Exception: {exc}\n")
        f.write(f"User: {context_req.user}\n")    
        f.write(f"View: {context.get('view')}\n")
        f.write(f"Request: {context_req}\n")
        f.write(f"Request data: {context_req.data}\n\n")
        


