_count = 1
_previous = int(input('הכנס מספר?'))
while True:
    _current = int(input('הכנס מספר נוכחי?'))
    if _current > _previous:
        _count += 1
        _previous = _current
    else:
        _count = 1
        continue
    if _count == 3:
        break
print(" התקבל רצף של 3 מספרים עוקבים עולים,התוכנית הסתיימה!")


