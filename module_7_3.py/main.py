
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
teme1_team = 1552.512
teme2_team = 2153.31451
tasks_total = 82

time_avg = 45.2
time_avg_true = (teme1_team + teme2_team)/tasks_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:

     result = 'Победа команды Мастера кода!'

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:

     result = 'Победа команды Волшебники Данных!'

else:

    result = 'Ничья!'
challenge_result = result

print('В команде Мастера кода участников:%d' % team1_num)
print("Итого сегодня в командах участников:" '%d'  'и'  '%d'  % (team1_num, team2_num))
print('Команда Волшебники данных решила задач:{0}'.format(score_2))
print('Волшебники данных решили задачи за :{0}'.format(teme1_team))

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы:{challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')
