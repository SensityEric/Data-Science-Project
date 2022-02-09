My_weight = int(input('Weight:'))

Measure = input('L(bs) or (K)g: ')

if Measure == "L" or "l":
    kilo = My_weight * 2.205
    print(f"{kilo}Kilos")
elif Measure == "K" or "k":
    pounds = My_weight / 2.205
    print(f'{pounds}kg')
else:
    print("Please you have enter  wrong input try again ")
