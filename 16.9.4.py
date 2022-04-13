class Guests:
    def __init__(self,name,surname,city):
        self.name=name
        self.surname = surname
        self.city = city

    def info(self):
        return str(f'{self.name} {self.surname}, г.{self.city}')

class Mentors(Guests):
    def __init__(self, name, surname, city, status):
        super().__init__(name, surname, city)
        self.status=status

    def info_mentor(self):
        return str(f'{self.name} {self.surname} , г.{self.city} , статус: {self.status}')

guests=[
    {'name': 'Иван','surname':'Иванов','city':'Тула','status':'Отсутствует'},
{'name': 'Петр','surname':'Петров','city':'Калуга','status':'Наставник'},
{'name': 'Сидор','surname':'Сидоров','city':'Москва','status':'Отсутствует'},
{'name': 'Захар','surname':'Захаров','city':'Нижний Новгород','status':'Отсутствует'},
{'name': 'Гордей','surname':'Гордеев','city':'Кострома','status':'Наставник'}
]
list_of_guests=[]
list_of_mentors=[]

for i in guests:
    if 'Наставник' in i.values():
        mentor=Mentors(i['name'],i['surname'],i['city'],i['status'])
        list_of_mentors.append(mentor.info_mentor())
    else:
        del i['status']
        guest=Guests(i['name'],i['surname'],i['city'])
        list_of_guests.append(guest.info())
print('Наставники')
for i in list_of_mentors:
    print(i)
print('Прочие гости-волонтеры')
for i in list_of_guests:
    print(i)





