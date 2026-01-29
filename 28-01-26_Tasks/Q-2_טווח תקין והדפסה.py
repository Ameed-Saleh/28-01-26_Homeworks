_lower = int(input("the lower limit: "))
while True:
   _higher = int(input("the higher limit: "))
   if  _higher > _lower:
       print("🔉"," ~~lower~~ = ", _lower)
       print("🔊"," ~~higher~~ = ", _higher)
       break
   if _higher <= _lower:
       _lower = int(input("the lower limit: "))
       continue
for _ in range(_lower, _higher +1 ):
    print( _ , end="  ")

