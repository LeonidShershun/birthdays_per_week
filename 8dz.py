from datetime import datetime, date
from collections import defaultdict


users = {'Андрійович Андрій Андрійович': '29.06.1995', 'Романович Роман Романович': '26.06.1983',
         'Адамович Адам Адамович': '25.06.1987', 'Бенедович Бенеда Бенедович': '27.06.1992',
         'Степанович Степан Степанович': '01.01.1999', 'Іванович Іван Іванович': '15.03.1994',
         'Семенович Семен Семенович': '28.06.1963'}

print()
data_ = datetime.now()
print()


print('Сьогодні: ', data_.strftime('%A %d %B %Y'))
print(f'За рахунком сьогодні {data_.weekday()+1}-й день тижня') # Сьогоднішній день тижня від 0 до 6 з + 1


def get_birthdays_per_week(users):
    birthday_users_list = []  # Словник працівників у кого ДН на цьому тижні.
    for name in users:
        birthday = users[name]
        birthday = datetime.strptime(birthday, '%d.%m.%Y').date() # перетворення дат з str до типу datatime
        birthday_current_year = date(data_.year, birthday.month, birthday.day) # визначення дня народження в поточному році
        diff = birthday_current_year - date.today() # Визначення кількості днів до дня народження працівника
        if 0 <= diff.days < 7: # Якщо до дня народження працівника менше тижня, то заносимо його в новий список birthday_users_list
            years = data_.year - birthday.year # Скільки років
            if years %10 == 0:
                if birthday_current_year.strftime('%A') == 'Sunday': 
                    day_cong = f"{birthday.day+1} {birthday_current_year.strftime('%B')} Monday"
                elif  birthday_current_year.strftime('%A') == 'Saturday':
                    day_cong = f"{birthday.day+2} {birthday_current_year.strftime('%B')} Monday"
                else:
                    day_cong = f"{birthday.day} {birthday_current_year.strftime('%B')} {birthday_current_year.strftime('%A')}"
                congrat = f"{day_cong} у нас ювіляр {name}, що святкуватиме свій ювілейний День народження {birthday.day} {birthday_current_year.strftime('%B')} {birthday_current_year.strftime('%A')}! Щиро вітаємо з ЮВІЛЕЄМ! Виповнилось {years} років!"
                birthday_users_list.append(congrat)
            else:
                if birthday_current_year.strftime('%A') == 'Sunday': 
                    day_cong = f"{birthday.day+1} {birthday_current_year.strftime('%B')} Monday"
                elif  birthday_current_year.strftime('%A') == 'Saturday':
                    day_cong = f"{birthday.day+2} {birthday_current_year.strftime('%B')} Monday"
                else:
                    day_cong = f"{birthday.day} {birthday_current_year.strftime('%B')} {birthday_current_year.strftime('%A')}"
                congrat = f"{day_cong} ми вітатимемо {name}, що святкуватиме свій День народження {birthday.day} {birthday_current_year.strftime('%B')} {birthday_current_year.strftime('%A')} Щиро вітаємо його з {years}-ти річчям!"
                birthday_users_list.append(congrat)
            birthday_users_list.sort()
    print()
    print(f'На цьому тижні ми вітаємо наступних колег: ')
    print()
    for cong in birthday_users_list:
        day = (cong.split()[2])
        print(day, cong)
    print()
get_birthdays_per_week(users)



