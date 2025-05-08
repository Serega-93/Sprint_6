from datetime import datetime, timedelta
from faker import Faker


def tomorrow_date():
    current_date = datetime.now()
    tomorrow_date = current_date + timedelta(days=1)
    date = tomorrow_date.strftime('%d-%m-%Y')
    return date

def generate_registration_data():
    faker = Faker('ru_RU')
    name = faker.first_name()
    while len(name) < 2 or len(name) > 15:
        name = faker.first_name()
    last_name = faker.last_name()
    address = faker.address()
    while len(address) < 5 or len(address) > 50:
        address = faker.street_address()
    address = (address.replace("(", "").replace(")", "").replace("/", ''))
    phone = faker.phone_number()
    phone = (phone.replace("-", "").replace(" ", "").replace("(", "")
             .replace(")", ""))
    phone = "8" + phone[1:]
    commit = faker.sentence()
    return name, last_name, address, phone, commit

