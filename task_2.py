import datetime

import dateparser

date_str = "01 июля 2025 года"

dt = dateparser.parse(date_str)
print(dt.strftime('%Y-%m-%d'))

a = datetime.datetime.strftime(date_str, '%Y %m %d')

'''
Самый простой вариант это dateparse 


Если без него, тогда можно поробовать распарсить строку.
Убрать "год", "года".
И пробовтаь определять номер месяца, как вариант
написать словаь типа ("января": "01", "февраля": "02") и использовать его.

'''