from app.schemas.item import Vehicle


car1 = Vehicle(
    id=1,
    mark="Toyota",
    model="Camry",
    state_number="А123ВС77",
    year_of_realise="2020",
    status="свободен"
)

# Пример 2: Грузовик в ремонте
truck = Vehicle(
    id=2,
    mark="КАМАЗ",
    model="65201",
    state_number="О765ТТ116",
    year_of_realise="2018",
    status="на ремонте"
)

# Пример 3: Списанный автобус
bus = Vehicle(
    id=3,
    mark="ПАЗ",
    model="32054",
    state_number="У321ХХ54",
    year_of_realise="2010",
    status="занят"
)

# Пример 4: Электромобиль
electric_car = Vehicle(
    id=4,
    mark="Tesla",
    model="Model S",
    state_number="Т999ЕЕ777",
    year_of_realise="2023",
    status="свободен"
)

# Пример 5: Спецтехника (скорая помощь)
ambulance = Vehicle(
    id=5,
    mark="Ford",
    model="Transit",
    state_number="А001МР97",
    year_of_realise="2022",
    status="занят"
)


vehicle_db = [car1, truck, bus, electric_car, ambulance]
# print(vehicle_db[::-1][0].id)
print([item for item in vehicle_db if item.status == 'свободен'])