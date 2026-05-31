import time
import random as rd
conveyor_belt = ["biryani", "tea", "chicken", "pullao", "tea", "water", "biryani", "tea", "pullao", "water"]
menu = {"biryani":6.50, "tea": 1.75, "water": 1.00, "pullao" : 5.25, "chicken": 3.50}
menu_list = ['biryani',"tea","water","pullao","chicken"]
station_1 = 1
station_2 = 4
station_3 = 7
replenish = 0
station_1_list = []
station_2_list = []
station_3_list = []


def Take(a, b, c):
    if int(a) and conveyor_belt[station_1] != " EMPTY " :
        station_1_list.append(conveyor_belt[station_1])
        conveyor_belt[station_1] = " EMPTY "
    if int(b) and conveyor_belt[station_2] != " EMPTY " :
        station_2_list.append(conveyor_belt[station_2])
        conveyor_belt[station_2] = " EMPTY "
    if int(c) and conveyor_belt[station_3] != " EMPTY " :
        station_3_list.append(conveyor_belt[station_3])
        conveyor_belt[station_3] = " EMPTY "

def Replenish():
    if conveyor_belt[replenish] == " EMPTY " :
        p = rd.choice(menu_list)
        conveyor_belt[replenish] = p
def bill():
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    for i in station_1_list:
        sum_1 += menu[i]
    for i in station_2_list:
        sum_2 += menu[i]
    for i in station_3_list:
        sum_3 += menu[i]
    return (sum_1,sum_2,sum_3)
def receipt(d,f,g):
    print(f"Receipt - Station 1 : ${d} , Station 2 : ${f} , Station 3 : ${g}")
while True:
    pivot = conveyor_belt[-1]
    conveyor_belt.pop()
    conveyor_belt = [pivot] + conveyor_belt
    time.sleep(2)
    a, b, c = tuple(input('Detector 0/1 ? '))
    if int(input("Calculate Bill 0/1 ? :")):
        d,f,g = bill()
        receipt(d,f,g)
        break
    print(conveyor_belt)