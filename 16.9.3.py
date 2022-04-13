class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def display_user(self):
        return str(f'Клиент: {self.name}\nБаланс: {self.balance} руб.')

user_1=User('Иван Петров',50)
print(user_1.display_user())
