# Вычисление вероятности выпадения заданной суммы S при броске N шестигранных кубиков

## Описание
При запуске скрипта необходимо ввести количество кубиков N и исследуемую сумму S (числа проходят проверку на целочисленный тип). Далее создается пустой массив
размерностью N * 6N. Ячейки массива A[N, S] циклически заполняются количеством вариантов набрать сумму S количеством кубиков N. Затем берется соответствующее
заданной пользователем сумме число вариантов и делится на число всех возможных исходов 6^N.

Принцип заполнения:<br>
Сумму S при использовании N кубиков можно получить при выпадении одного очка на N-м кубике и сумме S-1 на N-1 кубиках. Эту же сумму можно получить при выпадении
двух очков на N-м кубике и сумме S-2 на N-1 кубиках - и т.д. до 6 очков.

### Технологии
- Python 3.9 (библиотека NumPy)

### Запустите проект
```bash
python main.py
```
