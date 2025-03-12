from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 11", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 12", "+79234567890"))
catalog.append(Smartphone("Apple", "iPhone 13", "+79345678901"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79456789012"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79567890123"))

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}.")
    print(f"{smartphone.phone_number}")
