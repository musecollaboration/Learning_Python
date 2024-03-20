# # https://stepik.org/lesson/296968/step/8?auth=login&unit=278696

# На основании переменной persons, в которой хранится список кортежей, 
# в каждом кортеже хранится имя, зарплата, пол и паспорт человека.
# Ваша задача создать словарь, где ключами будут имена, 
# а значениями словарь из трех ключей: salary, gender и passport

# К примеру, если у вас есть изначально следующий список
[
    ('Bob Moore', 330000, 'M', '1635777202'),
    ('Gina Moore', 12500, 'F', '1639999999'),
]
# то из него должен получится следующий словарь
{
    'Bob Moore': {
        'salary': 330000,
        'gender': 'M',
        'passport': '1635777202'
    },
    'Gina Moore': {
        'salary': 12500,
        'gender': 'F',
        'passport': '1639999999'
    }
}

# РЕШЕНИЕ 1
persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]
data = {}
for i in persons:
    name, salary, gender, passport = i  # тут фишка с присвоением!!!
    i_dict = {
        'salary': salary,
        'gender': gender,
        'passport': passport,

    }
    data[name] = i_dict
print(data)

# Распаковка кортежа
https://github.com/musecollaboration/Learning_Python/blob/main/%D0%9A%D0%BE%D1%80%D1%82%D0%B5%D0%B6%D0%B8/%D0%A0%D0%B0%D1%81%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%BA%D0%BE%D1%80%D1%82%D0%B5%D0%B6%D0%B0.py

# s = ('Allison Hill', 334053, 'M', '1635644202')
# name, salary, gender, passport = s
# d = {
#     'name': name,
#     'salary': salary,
#     'gender': gender,
#     'passport': passport
# }
# print(d)


# РЕШЕНИЕ 2
persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]
data = {}
for i in persons:
    dict = {
        'salary': i[1],
        'gender': i[2],
        'passport': i[3]
    }
    data[i[0]] = dict
print(data)
