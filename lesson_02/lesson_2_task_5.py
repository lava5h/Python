def month_to_season(month):

    if not isinstance(month, int):
      return "Номер месяца должен быть целым числом"
    if month < 1 or month > 12:
        return "Некорректный номер месяца"

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"
    
print(month_to_season(10))
print(month_to_season(15))
print(month_to_season(1.5))