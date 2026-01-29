i = 0
_counter_up_to_16 = 0
for _ in range(1 , 10 + 1):
    age = int(input("שחקו יקר בן כמה אתה?"))
    if age > 18:
        print("שחקן זה מבוגר מדי לקבוצת נוער!! ")
        break
    if age < 12 :
        print("אתה מתחת לגיל הדרישה לקבוצת נוער!! ")
        continue
    if age > 16:
       _counter_up_to_16 += 1
       i += 1
       continue
    i += 1
print( "שחקנים מעל גיל 16:", _counter_up_to_16)
print ("מספר השחקנים התקינים שהצלחתי לאסוף מבחינת דרישות הגיל הינו:", i)