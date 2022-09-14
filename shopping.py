msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zepjyrus_m16_price = 1849.79
four = 4

prices = [msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zepjyrus_m16_price]


prices.sort()

print(f"the avrage is {round(sum(prices) / len(prices), 2)}")
print("highest price is:", prices[-1])
print("lowest price is:", prices[1])

msi_rtxa5000_price = round(4199.35)
gigabyte_aero_price = round(4295.54)
razer_blade15_price = round(3696.99)
asus_zepjyrus_m16_price = round(1849.79)


print(f"the rounded price of the asus zepjyrus m16 is ${asus_zepjyrus_m16_price}")
print(f"the rounded price of the gigabyte_aero_price is ${gigabyte_aero_price}")
print(f"the rounded price of the razer_blade15_price is ${razer_blade15_price}")
print(f"the rounded price of the asus_zepjyrus_m16_price is ${asus_zepjyrus_m16_price}")