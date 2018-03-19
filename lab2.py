usd=57
euro=60
forint=4
krona=7
funt=100

money = int (input ("VVedite summu, kotoruiu hotitte obmenyat: "))
currency = int (input("Ukazhite kod valuti (usd - 400, euro - 401, forint - 402, krona - 403, funt - 404): "))

if currency == 400:
    cache = round (money / usd, 2)
    print ("Valuta: доллар США")
elif currency == 401:
    cache = round (money / euro, 2)
    print ("Valuta: евро")
elif currency == 402:
    cache = round(money / forint, 2)
    print("Valuta: венгерский форинт")
elif currency == 403:
    cache = round(money / krona, 2)
    print("Valuta: норвежская крона")
elif currency == 404:
    cache = round(money / funt, 2)
    print("Valuta: фунт стерлинг")
else:
    cache = 0
    print ("NEIZVESTNAYA VALUTA")
print ("K polucheniu:", cache)