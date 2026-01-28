# שאלה שנייה - מלבן של כוכביות

_lines: int = int(input("Enter a number of lines: "))
_columns: int = int(input("Enter a number of columns: "))
if _lines > 0 and _columns > 0:
    for i in range(_lines):
        print("*" * _columns)
else:
    print("invalid input")

