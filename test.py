from universal_date_parser import DateParser

date_string = "06/07/1995"
a = DateParser(date_string, locale="de_DE")
print(a.to_date_str())
# >>> 1995-07-06
print(a.to_str())
# >>> 1995-07-06 00:00:00
print(a.to_date_str(date_format="%d.%m.%Y"))
# >>> 06.07.1995

date_string = "06/07/1995"
a = DateParser(date_string, locale="en_US")
print(a.to_date_str())
# >>> 1995-06-07

date_string = "06/07/1995"
a = DateParser(date_string, date_format="%d/%m/%Y")
print(a.to_date_str())
# >>> 1995-07-06

date_string = "Jun/06/1995"
a = DateParser(date_string)
print(a.to_date_str())
# >>> 1995-06-06

date_string = "06/Juni/1995"
a = DateParser(date_string, locale="de_DE")
print(a.to_date_str())
# >>> 1995-06-06
