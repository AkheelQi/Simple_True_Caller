import phonenumbers
from time import time
from numpy import number
from phonenumbers import geocoder, carrier, timezone
import requests

# Example text containing phone numbers
text = input("Enter your Number: ")

# Function to extract phone numbers from text
def extract_phone_numbers(text):
    phone_numbers = []
    for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
        phone_numbers.append(match.number)
    return phone_numbers

# Extract phone numbers
numbers = extract_phone_numbers(text)

# Print details of each phone number
for number in numbers:
    print(f"Phone Number: {phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
    print(f"Country: {geocoder.description_for_number(number, 'en')}")
    print(f"Carrier: {carrier.name_for_number(number, 'en')}")
    print(f"Valid: {phonenumbers.is_valid_number(number)}")
    print()


# Example phone number