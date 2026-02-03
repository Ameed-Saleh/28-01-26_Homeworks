_count = 1
_previous = None
while True:
    _current = int(input("הכנס מספר נוכחי:"))
    if _previous is None:
        _previous = _current
    if _current > _previous:
       _count += 1
    else:
        _count = 1
    _previous = _current
    if _count == 3:
        break
print(" התקבל רצף של 3 מספרים עוקבים עולים,התוכנית הסתיימה!")


