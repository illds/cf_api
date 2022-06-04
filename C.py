import requests
import sys

print("Вас приветствует программа для подсчёта количества попыток ученика на Codeforces.")
answer = ''
while answer != '1' and answer != '2':
    answer = str(input("Как вы хотите задать логины? (1 - по одному, 2 - несколько подряд)\n"))

if answer == "1":
    while True:
        nickname = str(input("Введите логин: (/stop - остановить программу)\n"))
        if nickname == "/stop":
            print("Программа завершена.")
            sys.exit()
        try:
            request = requests.post("https://codeforces.com/api/user.status?handle=" + nickname)
            print(f"Количество попыток {nickname}: " + str(len(request.json()['result'])) + '.')
        except:
            print("Error: Неправильный формат ввода или такого логина не существует!")
            continue
else:
    while True:
        nicknames = str(input("Введите логины через пробел: (/stop - остановить программу)\n"))
        if nicknames == "/stop":
            print("Программа завершена.")
            sys.exit()
        nn_array, nn_ans = [], []
        nickname = ''
        for i in range(len(nicknames)):
            if nicknames[i] != ' ':
                nickname += nicknames[i]
            else:
                nn_array.append(nickname)
                nickname = ''
        nn_array.append(nickname)
        for i in range(len(nn_array)):
            nickname = nn_array[i]
            try:
                request = requests.post("https://codeforces.com/api/user.status?handle=" + nickname)
                nn_ans.append(len(request.json()['result']))
            except:
                nn_ans.append(-1)
                continue
        for i in  range(len(nn_array)):
            if nn_ans[i] != -1:
                print(f"Количество попыток {nn_array[i]}: {nn_ans[i]}.")
            else:
                print(f"Error: Логин {nn_array[i]} не существует, либо неверный формат ввода!")
