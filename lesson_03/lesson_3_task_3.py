from address import Address
from mailing import Mailing

address_from = Address(
    postal_code = "123456",
    city = "Москва",
    street = "Тверская",
    building = "10",
    apartment = "25"
)

address_to = Address(
    postal_code="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    building="20",
    apartment="50"
)

mailing = Mailing(
    to_address = address_to,
    from_address = address_from,
    cost = 500.00,
    track = "AS123456789RU"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.building} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.building} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)