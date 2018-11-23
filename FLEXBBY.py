from  datetime import datetime


# день рождение
birth = 14
birth1 = 20
birth2 = 45
b = 1

day = input("Day: ")
if day in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']:
    month = input("Month: ")
    for month in range(1,12): #['1','2', '3','4', '5','6', '7', '8','9', '10','11', '12']:
        if b in  range(12): #['1','2','3','4','5','6','7','8','9','10','11','12']:
            if month % 12 == 1:
                    year = input("Year: ")
                    c = int(year)
                    y = int(birth)
                    y1 = int(birth1)
                    y2 = int(birth2)
                    r = int(month)
                    pay1 = y + c
                    pay2 = r + b
                    pay3 = y1 + c
                    pay4 = y2 + c
                    print(day,month,pay1)
                    print(day,month,pay3)
                    print(day,month,pay4)
# дата выдачи разницы
extradition = 6
extradition1 = 25








