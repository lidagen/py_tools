import datetime
from zhdate import ZhDate

date_object = datetime.date.today()

gregorian_dic = {
    '刘怡': datetime.date(2000, 3, 9)
}
lunar_dic = {
    '王淞': ZhDate(1988, 1, 29)
}


def day_remind():
    today = datetime.date.today()
    for gregorian in gregorian_dic:
        day = gregorian_dic.get(gregorian)
        if day.month == today.month and day.day == today.day:
            print(f"今天{today},是{gregorian}的生日！")

    for lunar in lunar_dic:
        lunar_birthday_day = (lunar_dic.get(lunar))
        lunar_today = ZhDate.today()
        if lunar_today.lunar_month == lunar_birthday_day.lunar_month \
                and lunar_today.lunar_day == lunar_birthday_day.lunar_day:
            print((f"今天{today},农历日期是{lunar_today},是{lunar}({lunar_birthday_day})的生日,！"))
