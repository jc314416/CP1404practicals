TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = 0
print("Electricity bill estimator 2.0")
while tariff == 0:
    tariff = int(input("Enter tariff: "))
    if tariff == 11:
        price_per_kWh = TARIFF_11
    elif tariff == 31:
        price_per_kWh = TARIFF_31
    else:
        print("Invalid Entry")
        tariff = 0
daily_use_kWh = int(input("Enter daily use in kWh: "))
number_of_days_in_billing_period = int(input("Enter number of billing days: "))
estimated_bill = (price_per_kWh*daily_use_kWh*number_of_days_in_billing_period)
print("Estimated bill: ${:.2f}".format(estimated_bill))
