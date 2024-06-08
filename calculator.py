def calculator(input_arif):

  # Вычленяем нужные нам компоненты из вводимого пользователем выражения
  num_left, operator, num_right = input_arif.split()

  # Перегоняем наши строки в числовой формат. На всякий случай в float
  num_left = float(num_left)
  num_right = float(num_right)

  # Проверяем тип операции и проводим ее
  if operator == '+':
    result = num_left + num_right
  elif operator == '-':
    result = num_left - num_right
  elif operator == '*':
    result = num_left * num_right
  elif operator == '/':
    result = num_left / num_right
  elif operator == '<':
    result = num_left < num_right
  elif operator == '>':
    result = num_left > num_right
  elif operator == '<=':
    result = num_left <= num_right
  elif operator == '>=':
    result = num_left >= num_right
  elif operator == '!=':
    result = num_left != num_right
  elif operator == '==':
    result = num_left == num_right
  else:
    return "Недопустимый оператор"

  # Русифицируем результат
  if result == True:
    result = 'Верно'
  elif result == False:
    result = 'Неверно'
  else:
    result
  return result

# Получаем входные данные от пользователя
input_arif = input("Введите выражение в формате 'X оператор X': ")

# Вызываем функцию калькулятора и выводим результат
result = calculator(input_arif)
print("Результат: ", result)
