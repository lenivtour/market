phone = str(input('Введите номер телефона в формате х-х(х-х)х----х:'))
#phone = '+76 (495) 755-08-22'
print('Телефон для проверки', phone)

# Проверки
count_all_symbols = 0
count_numbers = 0
num = str()
#if phone[0] != '+': print('Укажите код страны в формате +7..')
for i in range(len(phone)):
    if phone[i] in '1234567890 ()-+': # Перебираем символы
        count_all_symbols += 1
    if phone[i] in '1234567890':       # Подсчет количества цифр в телефоне
        count_numbers += 1
        num += phone[i]


# Проверка на допустимость всех символов
if count_all_symbols == len(phone): print('Все символы допустимы')
else:
    print('! Cодержит недопустимые символы!')
    exit()

# Проверка количества цифр в номере
if 10 <= count_numbers <= 14: print('Цифр достаточно')
else:
    print('! Неверное количество цифр, должно быть от 10 до 14')
    exit()

# проверка номера

# код страны
country = phone[:(phone.find('('))]
country_code = str()
for i in range(len(country)):
    if country[i] in '1234567890':
        country_code += country[i]   # Подсчет количества цифр в коде страны
if len(country_code) > 4: print('! Неверный код страны', country, '- должен быть от 1 до 4 цифр')
elif country_code == str(): print('! Код страны не указан')
else:
    print('Код страны  -', country)
    if '+' not in country:
        print('! Код страны должени быть в формате +...')


# код города
city = phone[(phone.find('(') + 1):(phone.find(')'))]
if len(city) > 5 or len(city) < 3:
    print('! Неверный код города', city, '- должен быть от 3 до 5 цифр')
else:
    print('Код города  -', city)
#print(phone.split('('))

# телефон
# проверка на колчество цифр
phone_num = phone[(phone.find(')')+1):]
phone_num_code = str()
for i in range(len(phone_num)):
    if phone_num[i] in '1234567890':
        phone_num_code += phone_num[i]   # Выборка цифр в телефоне
# код города + телефон должны составлять в сумме 10 цифр, если код города определен скобками,
# значит телефон должен содержать  цифр: 10 - код города:
if len(phone_num_code) + len(city) != 10:
    print('! Телефон указан неверно:', phone_num, ', должен содержать', (10 - len(city)), 'цифр')
else:
    print('Телефон -', phone_num)