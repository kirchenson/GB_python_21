"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами."""

from sys import argv
from pyles4 import mod
script_name, hours, rate, bonus = argv
mod.sum(int(hours),int(rate),int(bonus))