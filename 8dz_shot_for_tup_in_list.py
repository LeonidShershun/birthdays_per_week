from datetime import datetime, date
from collections import defaultdict


users = [{'name': 'Андрійович Андрій Андрійович', 'birthday': '29.06.1995'},
         {'name': 'Романович Роман Романович', 'birthday': '26.06.1983'},
         {'name': 'Адамович Адам Адамович', 'birthday': '25.06.1987'},
         {'name': 'Бенедович Бенеда Бенедович', 'birthday': '27.06.1992'},
         {'name': 'Степанович Степан Степанович', 'birthday': '01.01.1999'},
         {'name': 'Іванович Іван Іванович', 'birthday': '15.03.1994'},
         {'name': 'Семенович Семен Семенович', 'birthday': '28.06.1963'}]


data_ = datetime.now()
today_day = data_.weekday()+1 # Сьогоднішній день тижня від 0 до 6 з + 1
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


print('\nСьогодні: ', data_.strftime('%A %d %B %Y'))
print(f'За рахунком сьогодні {today_day}-й день тижня') 

def get_birthdays_per_week(users):
    ty_users = {}
    for user_birth in users:
        str_name_bd = (str(user_birth.values()).replace("['", '').replace("'])", '').replace("dict_values(", '').replace("', '", '='))
        key_ = str_name_bd.split('=')[-2]
        value_ = str_name_bd.split('=')[-1]
        tup = ((key_, value_))
        ty_users.update([tup])
    birthday_users = {}  # Словник працівників у кого ДН на цьому тижні.
    for name in ty_users:
        birthday = ty_users[name]
        birthday = datetime.strptime(birthday, '%d.%m.%Y').date() # перетворення дат з str до типу datatime
        birthday_current_year = date(data_.year, birthday.month, birthday.day) # визначення дня народження в поточному році
        diff = birthday_current_year - date.today() # Визначення кількості днів до дня народження працівника
        if 0 <= diff.days < 7: # Якщо до дня народження працівника менше тижня, то заносимо його в новий список birthday_users_list
            if birthday_current_year.strftime('%A') == 'Sunday' or birthday_current_year.strftime('%A') == 'Saturday': 
                day_cong = "Monday"
            else:
                day_cong = birthday_current_year.strftime('%A')
            birthday_users[name] = day_cong
    this_week = defaultdict(list)
    for name, day in birthday_users.items():
        this_week[day].append(name)
    print(f'\nНа цьому тижні потрібно привітати таких працівників: \n')
    a = this_week["Monday"]
    if len(a) >= 1:
        a= str(a).replace("['", '').replace("']", '').replace("'", '')
        print(f'Понеділок : {a}')
    b = this_week["Tuesday"]
    if len(b) >= 1:
        b= str(b).replace("['", '').replace("']", '').replace("'", '')
        print(f'Вівторок  : {b}')
    d = this_week["Wednesday"]
    if len(d) >= 1:
        d= str(d).replace("['", '').replace("']", '').replace("'", '')
        print(f'Середа    : {d}')
    c = this_week["Thursday"]
    if len(c) >= 1:
        c= str(c).replace("['", '').replace("']", '').replace("'", '')
        print(f'Четвер    : {c}')
    q = this_week["Friday"]
    if len(q) >= 1:
        q= str(q).replace("['", '').replace("']", '').replace("'", '')
        print(f'Пятниця   : {q}')
    else:
        print()


if __name__ == "__main__":
    get_birthdays_per_week(users)



