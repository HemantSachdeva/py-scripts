#!/usr/bin/env python3

import sys
try:
    import phonenumbers as p
    from phonenumbers import timezone, carrier, geocoder
except ImportError:
    print("Please install phonenumbers module")
    sys.exit(1)

number = input("Enter phone number [with country code]: ")
number = p.parse(number, "US")
print("Timezone: ", timezone.time_zones_for_number(
    number)[0])
print("Carrier Name: ", carrier.name_for_number(number, "en"))
print("Location: ", geocoder.description_for_number(number, "en"))
print("Country Code: ", number.country_code)
print("National Number: ", number.national_number)
print("National Number: ", number.national_number)
print("Number of Leading Zero: ", number.number_of_leading_zeros)
print("Valid Number: ", p.is_valid_number(number))
