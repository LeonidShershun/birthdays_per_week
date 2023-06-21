from datetime import datetime, date
from collections import defaultdict


users = {'Андрійович Андрій Андрійович': '29.06.1995', 'Романович Роман Романович': '26.06.1983',
         'Адамович Адам Адамович': '25.06.1987', 'Бенедович Бенеда Бенедович': '27.06.1992',
         'Степанович Степан Степанович': '01.01.1999', 'Іванович Іван Іванович': '15.03.1994',
         'Семенович Семен Семенович': '28.06.1963'}

data_ = datetime.now()
print()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


print('Сьогодні: ', data_.strftime('%A %d %B %Y'))
print(f'За рахунком сьогодні {data_.weekday()+1}-й день тижня') # Сьогоднішній день тижня від 0 до 6 з + 1
print()

def get_birthdays_per_week(users):
    birthday_users = {}  # Словник працівників у кого ДН на цьому тижні.
    for name in users:
        birthday = users[name]
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
        
    
    print()
    print(f'На цьому тижні потрібно привітати таких працівників: ')
    print()
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

    print()
get_birthdays_per_week(users)



