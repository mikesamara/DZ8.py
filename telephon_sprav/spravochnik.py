# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt 
# ФИО, номер телефона -данные, которые должны находиться в файле.
# 1. программа должна выводить данные
# 2. программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи 
# (например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os
import shutil

FILE_PATH = r'c:/Users/Alexey/Desktop/Учеба Миша/python/seminar8/telephon_sprav\spravocnik.txt'

def delete_spravochnik():
    with open (FILE_PATH, 'w') as f:
        f.write('Справочник пуст')
    
def add_usser():   
    with open (FILE_PATH, 'a') as f:
        f.write('\n')
        f.write(input("Введите Фамилию, Имя, Номер телефон абонента: "))
        
def read_usser():   
    with open (FILE_PATH, 'r') as f:
        for line in f:
            print(line.strip())

def search_usser():   
    with open (FILE_PATH, 'r') as f:
        esers = input ('Кого ищем? ')
        for line in f:
            if esers in line:
                print(line)

                

def inter():
    print("Если хотите увидеть телефонный справочник, нажмите 1")
    print("Если хотите добавить абонента в телефонный справочник, нажмите 2")
    print("Если хотите найти абонента в телефонном справочнике, нажмите 3")
    print("Если хотите завершить работу нажмите 4")
    print("Если хотите справочник, нажмите 5") 
     
                
print("Если хотите увидеть телефонный справочник, нажмите 1")
print("Если хотите добавить абонента в телефонный справочник, нажмите 2")
print("Если хотите найти абонента в телефонном справочнике, нажмите 3")
print("Если хотите завершить работу нажмите 4")
print("Если хотите удалить справочник, нажмите 5")


while (n := int(input("Выберите значение: "))) != 4:
    match n:
        case 1:
            read_usser()
            inter()
        case 2:
            add_usser()
            inter()
        case 3:
            search_usser()
            inter()
        case 5:
            delete_spravochnik()
        case 4:
            print ("Досвидание")
        
    