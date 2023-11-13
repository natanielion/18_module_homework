count = int(input("Укажите кол-во билетов: \n"))
summ=0
for i in range(count):
    age = int(input("Напишите возраст посетителя " + str(i+1) + ":\n"))
    if 0 < age < 18:
        continue
    elif 18 <= age <=25:
        summ += 900
    elif age > 25:
        summ += 1390
if count>3:
    summ *= 0.9
print("Сумма к оплате - " + str(int(summ)))