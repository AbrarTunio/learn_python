cash = 2560

if cash >= 1000:
    cash2=cash/1000
    print("give",int(cash2),"one thousand note")
cash=cash%1000
# print("my cash now is:",cash)
if cash >= 500:
    cash2=cash/500
    print("give",int(cash2),"five hundered note")
cash=cash%500


if cash >= 100:
    cash2=cash/100
    print("give",int(cash2),"one hundered note")
cash=cash%100


if cash >= 50:
    cash2=cash/50
    print("give",int(cash2),"fifty rupee note")
cash=cash%50


if cash >= 10:
    cash2=cash/10
    print("give",int(cash2),"ten note")
cash=cash%10
