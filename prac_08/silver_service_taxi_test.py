from prac_08.silver_service_taxi import SilverServiceTaxi

taxi_1 = SilverServiceTaxi("Prius 1", 100, 2)
taxi_1.start_fare()
taxi_1.drive(18)
print("${:.2f}".format(taxi_1.get_fare()))
print(taxi_1)
# print(taxi_1.price_per_km)