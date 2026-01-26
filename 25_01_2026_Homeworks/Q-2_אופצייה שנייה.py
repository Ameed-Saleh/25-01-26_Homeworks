_lines: int = int(input("Enter a number of lines: "))
_columns: int = int(input("Enter a number of columns: "))
while _lines > 0 or _lines != 0:
    if _columns > 0 or _columns != 0:
        a = 0
        while a < _lines:
            print("*" * _columns)
            a += 1
        else:
            _lines: int = int(input("Enter a number of lines: "))
            _columns: int = int(input("Enter a number of columns: "))
else :
   print("invalid input")
