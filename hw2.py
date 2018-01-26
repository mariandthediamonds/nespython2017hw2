#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:43:33 2018

@author: maria.ilinykh
"""
#%% №1

def func(n):
    f = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            f += i
    return f
print(func(100))
/Users/maria.ilinykh/Desktop/hw2.py
#%% №2
def fib(n, a = {1: 1, 2:2}):
   if n not in a:
        a[n] = fib(n-1, a) + fib(n-2, a)
   return a[n]
print(fib(200))

#%% №4
import pandas
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()
x = 'лекарство'
k = 0
for i in df:
    if set(i) & set(x) == set(i) and len(i) == len(set(i)):
        print(i)
        k += 1
print('кол-во слов:', k)
#%%  №5
import pandas
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()
five_words = []
for i in df:
    if len(i) == 5 and len(i) == len(set(i)):
        five_words.append(i)
import random
y = random.choice(five_words)
n = 1
print("Загаданное слово:", y)         
playing = True
while playing :
    
    user_guess = input("Ваше слово из 5-ти разных букв!\n") 
    if user_guess == 'стоп':
        break
    elif y != user_guess: 
        print(len((set(y) & set(user_guess))))
        n += 1
    elif user_guess == y:
        playing = False  
        print('Вы выиграли')
print('вы угадали с попытки №', n)
#%% №6
import pandas
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()
five_words = []
for i in df:
    if len(i) == 5 and len(i) == len(set(i)):
        five_words.append(i)
import random
n = 1        
playing = True
while playing :
    
    print(random.choice(five_words))
    user_guess = input("Введите число совпадающих букв\n") 
    if user_guess != "!":
        playing=True
        n += 1
    else:
            playing = False   
            print('Вы выиграли')
print('вы угадали с попытки №', n)
#%% №7
    
 """http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/ """

import re
import urllib.request
from bs4 import BeautifulSoup


url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') 

#table = soup.table
table = soup.find("table")
table_rows = table.find_all("tr")

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]

print(row)

       
      
       
          
          
          
    
    
        
        
      
      
    
    

    
    
 