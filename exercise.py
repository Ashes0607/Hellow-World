# coding=UTF-8
# cars = ['toyota','bmw','audi','subaru']
# for car in cars:
#     if car=='bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# ---
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# ---
# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("Have you registered to vote yet?")
# ---
# age = 19
# if age < 10:
#     print('you just need to spend $0')
# elif 10 <= age < 20:
#     print('you just need to spend 10$')
# else:
#     print('you need to pay 20$')
# ---
# joke = (200, 50)
# print(joke)
# joke = (400, 100)
# print(joke)
# ---
# import pandas as pd
# df = pd.DataFrame()
# print(df)
# ��װpandasʧ��
# ---
# age=23
# if age<4:
#     price=0
# elif age<18:
#     price=5
# else:
#     price=10
# print("You just need to pay $"+str(price)+".")
# ֻ��ִ�в�ͨ�����Ż�������һ������ͨ���ʹ�������ͻ���²���˻�������⣬��һ������Ϸ�����������ĳ�������ѵ�һ�����������
# ---
# alien_color = {'red','green','blue'}
# if 'orange' in alien_color:
#     print("��һ��5�����")
# elif 'gray' in alien_color:
#     print ("��һ��10�����")
# else:
#     print("��һ��15�����")
 # ��������ɫ#3
# ---
# cars = ('audi','bmw','subaru','toyota')
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print (car.title())
# if�����ȷ�������
# car = 'subaru'
# print("is car == 'subaru'?, i predict True")
# print(car == 'subaru')
# print ("\nis car == 'audi'?,i predict False ")
# print (car == 'audi')
# ---
# age =23
# if age < 2:
#     print("he is baby")
# elif age < 4:
#     print("he is learning walk")
# elif age < 13:
#     print("he is boy")
# elif age < 20:
#     print("he is teenager")
# elif age < 65:
#     print ("he is adult")
# else:
#     print ("he is aged")
# �ж�����
# ---
# deep_desires = ['zhuanqian','gf','cloth']
# for deep_desire in deep_desires:
#     if deep_desire == 'gf':
#         print ("sorry,it is not a right time!")
#     else:
#         print ("Adding "+deep_desire+".")
# �������Ԫ��
# ---
# deep_desires = ['bb']
# if deep_desires:
#     for deep_desire in deep_desires:
#         print ("Adding "+''.join(deep_desires)+".")
#     print ("finish making your pizza")
# else:
#     print ("you sure?")
# Tetris = {'color':'green','point':5}
# new_point = Tetris['point']
# print ("you earned "+str(new_point)+" points!")
# Tetris['x_position'] = 0
# Tetris['y_position'] = 25
# print (Tetris)
# �ֵ䣬�Ժ�������Զ���˹����С��Ϸ
# ---
# Tetris = {'color':"green"}
# print ("Tetris is "+Tetris['color']+".")
# Tetris['color'] = "yellow"
# print ("Tetris now is "+Tetris['color']+"!")
# del Tetris['color']
# print (Tetris)
# ---
# Tetris = {'x_position':0,'y_position':25,'speed':'medium'}
# Tetris['speed'] = "fast"
# if Tetris['speed'] == 'slow':
#     x_increment = 1
# elif Tetris['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# Tetris['x_position'] = Tetris['x_position'] + x_increment
# print ("New position is "+str(Tetris['x_position']))
#�ƶ�����
# 6-1 �� �� ��ʹ��һ���ֵ����洢һ�����˵���Ϣ�����������ա�����;�ס�ĳ��С����ֵ�Ӧ������first_name ��last_name ��age ��city �����洢�ڸ��ֵ��� ��ÿ����Ϣ����ӡ������
# human_01 = {
#     'last_name':'tz',
#     'first_name':'m',
#     'age':'23',
#     'city':'Karamy'
#     }
# for key,value in human_01.items():
#     print("Key:"+key)
#     print ("Value:"+''.join(value))
# 6-2 ϲ�������� ϲ�������� ��ʹ��һ���ֵ����洢һЩ��ϲ�������֡������5���˵����֣�������Щ���������ֵ��еļ������ÿ����ϲ����һ�����֣�������Щ������Ϊֵ�� �����ֵ��С�
# ��ӡÿ���˵����ֺ�ϲ�������֡�Ϊ������������Ȥ��ͨ��ѯ������ȷ����������ʵ�ġ�
# favourite_person_number = {
#     'Tz':'8',
#     'Yc':'20',
#     'Xl':'66',
#     'xq':'77',
#     'Ry':'88',
#     }
# for key,value in favourite_person_number.items():
#     print ("name: " + key)
#     print ("number: " + value)
# 6-3 �ʻ�� �ʻ�� ��Python�ֵ������ģ����ʵ�����е��ֵ䣬��Ϊ������������ǽ����߳�Ϊ�ʻ�� �������ǰ��ѧ����5����̴ʻ㣬�����������ʻ���еļ����������ǵĺ�����Ϊֵ�洢�ڴʻ���С�
# ������ķ�ʽ��ӡÿ���ʻ㼰�京�塣Ϊ�ˣ�������ȴ�ӡ�ʻ㣬�����������һ��ð�ţ��ٴ�ӡ�ʻ�ĺ��壻Ҳ����һ�д�ӡ�ʻ㣬��ʹ�û��з���\n ���� ��һ�����У�Ȼ������һ���������ķ�ʽ��ӡ�ʻ�ĺ��塣
# vocabulary = {
#     'inhibition':'����',
#     'vocabulary':'�ʻ�',
#     'Avartar':'����',
#     'excuse':'����',
#     'dict':'�ֵ�'
# }
# for key,value in vocabulary.items():
#     print (key + ":" + value + "\n").title()
# 6-6 ���� ���� ����6.3.1�ڱ�д�ĳ���favorite_languages.py��ִ�����²�����
# ����һ��Ӧ�û���ܵ������Ա������������Щ���Ѱ������ֵ��У���������δ�������ֵ��С�
# ���������Ա�����������Ѳ��������ˣ���ӡһ����Ϣ��ʾ��л�����ڻ�δ���������ˣ���ӡһ����Ϣ������������顣
# favourite_person_number = {
#     'Tz':'8',
#     'Yc':'20',
#     'Xl':'66',
#     'xq':'77',
#     'Ry':'88',
#     }
# for key in favourite_person_number:
#     print ("Thanks for your invited " + key)
# if 'eee' not in favourite_person_number:
#     print ("\nDear eee,****")
# ---
# import random
# Tetris_00 = {'color':'red','point':'5','speed':'slow'}
# Tetris_01 = {'color':'blue','point':'10','speed':'medium'}
# Tetris_02 = {'color':'green','point':'15','speed':'fast'}
# Tetris_03 =[Tetris_00,Tetris_01,Tetris_02]
# for Tetris_number in range(30):
#     new_Tetris = random.sample(Tetris_03.)
#     print (new_Tetris)
# ---
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# ���룬�ظ����ݲ������������
# name = raw_input("Please enter your name: ")
# # print("Hello, " + name + "!")
# # ʹ��input���������Ҫע��python2.7ֻ��ʹ��raw_input
# 7-1 �������� �������� ����дһ������ѯ���û�Ҫ����ʲô��������������ӡһ����Ϣ���硰Let me see if I can find you a Subaru����
# car = raw_input("what kind of car do you want? ")
# print ("Let me see if i can find you a " + car)
# 7-2 �͹ݶ�λ �͹ݶ�λ ����дһ������ѯ���û��ж������ò͡��������8�ˣ��ʹ�ӡһ����Ϣ��ָ��û�п���������ָ���п�����
# seat = raw_input("how many person have dinner? ")
# seat = int(seat)
# if seat >= 8:
#     print ("Sorry,There is no seat for you!")
# else:
#     print ("Please follow me,i will lead you to seat")
# 7-3 10�������� �������� �����û�����һ�����֣���ָ����������Ƿ���10����������
# number = raw_input("Please type your number: ")
# number = int(number)
# if number/10 == 0:
#     print ("This number is an integral multiple of 10")
# else:
#     print ("This number is not an integral multiple of 10")
# ---
# prompt = "\n Tell me your message,i will repeat:"
# message = ""
# while message != 'quit':
#     message = raw_input(prompt)
#     print (message)
# ֻ���û�����quitʱ���˳��ó��򣬷���һֱ�ظ��û��������ݡ�
# prompt = "\n Tell me your message,i will repeat:"
# message = ""
# while message != 'quit':
#     message = raw_input(prompt)
#
#     if message != 'quit':
#         print (message)
# ������������иĽ��������벻Ϊquitʱ�Ŵ�ӡ������quitʱֱ���˳�����ӡ��
# prompt = "\n i do love the style of trap hiphop like: "
# message = ""
# active = True
# while active:
#     message = raw_input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# ��Ǹó�����ʲôʱ����ʲôʱ��ֹͣ���У��Եô������룬��ֹ��һ�кܶ�������³����������֪������һ����������
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number %2 == 0:
#         continue
#     else:
#         print (current_number)
# ��ӡ����10���ڵ�ѭ��
# 7-4 �������� �������� ����дһ��ѭ������ʾ�û�����һϵ�еı������ϣ������û�����'quit' ʱ����ѭ����ÿ���û�����һ�����Ϻ󣬶���ӡһ����Ϣ��˵���ǻ��ڱ��� ������������ϡ�
# message = "/n Please type some material to finish your pizza: "
# pizza_mateiral = ""
# while pizza_mateiral != 'quit':
#     pizza_mateiral = raw_input(message)
#     if pizza_mateiral != 'quit':
#         print("Here are the materials available:" + pizza_mateiral)
# 7-5 ��ӰƱ ��ӰƱ ���мҵ�ӰԺ���ݹ��ڵ�������ȡ��ͬ��Ʊ�ۣ�����3��Ĺ�����ѣ�3~12��Ĺ���Ϊ10��Ԫ������12��Ĺ���Ϊ15��Ԫ�����дһ��ѭ����������ѯ���� �������䣬��ָ����Ʊ�ۡ�
# message = "\n i will show price that type you age:"
# Age = ""
# while Age != 'quit':
#     Age = raw_input(message)
#     if Age < 3:
#         print ("Free!")
#     elif 3 < Age < 12:
#         print ("$10")
#     elif Age >12:
#         print ("$15")

# 7-6 �������� �������� ������һ�ַ�ʽ�����ϰ7-4����ϰ7-5���ڳ����в�ȡ�������������� ��while ѭ����ʹ����������������ѭ���� ʹ�ñ���active ������ѭ��������ʱ���� ʹ��break ������û�����'quit' ʱ�˳�ѭ����
# talk = "\n Tell me something and i will repeat it to you !"
# active = True
# while active:
#     message = raw_input(talk)
#     if message == 'quit':
#         active = False
#     else:
#         print (message)

# 7-7 ����ѭ�� ����ѭ�� ����дһ��û��û�˵�ѭ��������������Ҫ������ѭ�����ɰ�Ctrl +C��Ҳ�ɹر���ʾ����Ĵ��ڣ���

# ʹ���û�������ֵ䣨����˼·���ȶ���һ�����ֵ����ڴ洢��Ȼ����һ��active��������жϳ����Ƿ����ִ�к���whileѭ������������
# emptys = {}
# sigh_active = True
# while sigh_active:
#     name = raw_input("what is your name: ")
#     empty = raw_input("which mountain would you like to climb: ")
#     emptys[name] = empty
#     repeat = raw_input("would you like to let another person respond: ")
#     if repeat == 'no':
#         sigh_active = False
#         for name, empty in emptys.items():
#             print (name + " would like to climb " + empty + ".")
#���庯��
# def great_users(username):
#     """��ʾ�򵥵��ʺ���"""
#     print("Hello,"+ username.title() + "!")
# great_users(raw_input())

# 8-1 ��Ϣ ����дһ����Ϊdisplay_message() �ĺ���������ӡһ�����ӣ�ָ�����ڱ���ѧ����ʲô���������������ȷ����ʾ����Ϣ��ȷ����
# def display_message(sentence):
#     """��ӡһ������"""
#     print(sentence.title())
# display_message(raw_input())
# 8-2 ϲ����ͼ�� ����дһ����Ϊfavorite_book() �ĺ��������а���һ����Ϊtitle ���βΡ����������ӡһ����Ϣ����One of my favorite books is
# Alice in Wonderland �������������������һ��ͼ���������Ϊʵ�δ��ݸ�����
# def favourite_book(title):
#     """��ӡһ����Ϣ"""
#     print ("One of my favourite books is " + title.title())
# favourite_book('alice in wonderland')

# λ��ʵ�Σ�����һ���������붯��������Լ����֣��Լ����ú������
# def describe_pet(animal_type,pet_name):
#     """��ʾ������Ϣ"""
#     print ("my favourite animal is " + animal_type.title() + ".")
#     print ("His name is " + pet_name.title() + ".")
# describe_pet('hamster','harry')
# describe_pet('dog','jerry')

# �ؼ���ʵ��(������'animal_type=',��ȷ���ĸ�ʵ��Ҫ�����ĸ��β�)
# def describe_pet(animal_type,pet_name):
#     """��ʾ������Ϣ"""
#     print ("my favourite animal is " + animal_type.title() + ".")
#     print ("His name is " + pet_name.title() + ".")
# describe_pet(animal_type='hamster',pet_name='harry')

# �βο��Ը���Ĭ��ֵ�������ڵ���ʱ����ʡ�Բ���ʵ�εĴ��루��������ʱҲ��ֱ�Ӹ�������ʵ�Σ�
# def describe_pet(animal_type,pet_name='harry'):
#     """��ʾ������Ϣ"""
#     print ("my favourite animal is " + animal_type.title() + ".")
#     print ("His name is " + pet_name.title() + ".")
# describe_pet('hamster')

# 8-3 T�� ����дһ����Ϊmake_shirt() �ĺ�����������һ�������Լ�Ҫӡ��T���ϵ��������������Ӧ��ӡһ�����ӣ���Ҫ��˵��T���ĳ����������
# ʹ��λ��ʵ�ε����������������һ��T������ʹ�ùؼ���ʵ�����������������
# def make_shirt(shirt_size,shirt_word):
#     """��Ҫ˵�����������"""
#     print ("size :" + shirt_size)
#     print ("The words you want to print:" + shirt_word)
# make_shirt(shirt_size=raw_input(),shirt_word=raw_input())

# 8-4 ���T�� ���޸ĺ���make_shirt() ��ʹ����Ĭ�����������һ��ӡ��������I love Python���Ĵ��T�������������������������T����һ��ӡ��Ĭ�������Ĵ��T
# ����һ��ӡ��Ĭ���������к�T����һ��ӡ������������T���������޹ؽ�Ҫ����
# def make_shirt(shirt_size,shirt_word='i love python'):
#     """��Ҫ˵�����������"""
#     print ("size :" + shirt_size)
#     print ("The words you want to print:" + shirt_word)
# make_shirt('big')
# make_shirt('middle')
# make_shirt('middle',shirt_word='others')

# 8-5 ���� ����дһ����Ϊdescribe_city() �ĺ�����������һ�����е������Լ��ó��������Ĺ��ҡ��������Ӧ��ӡһ���򵥵ľ��ӣ���Reykjavik is in
# Iceland �������ڴ洢���ҵ��β�ָ��Ĭ��ֵ��Ϊ������ͬ�ĳ��е������������������������һ�����в�����Ĭ�Ϲ��ҡ�
# def describe_city(country_name,country_belones='China'):
#     """Ĭ��ֵ�βι���"""
#     print (country_name + " is in " + country_belones)
# describe_city('henan')

# ���������ղ��������������
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' +last_name
#     return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print (musician)

# ����һ��get_formatted_name������ȥ���û�����firstname�Լ�lastname�����������������Ϊqʱ��break��
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print ("Please tell me your name: ")
#     print ("(enter 'q' at any time to quit!)")
#     f_name = raw_input("First name:")
#     if f_name == 'q':
#         break
#     l_name = raw_input("Last name:")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name,l_name)
#     print ("Hello, " + formatted_name)

# ��дһ������ȥ������ֵ��д洢���ݵĵ��ʳ��ִ����Լ������ֵĴ����Ӵ�С���У�����Ϊkey������Ϊvalue��
# str1 = """The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested.Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"""
# List1=""" """
# list1 = str1.split(""" """ )
# dict1 ={}
# for element in list1:
#     if element not in dict1:
#         dict1[element] = 1
#     else:
#         dict1[element] += 1
# print(dict1)

# �� 10 ����Ϸ�ĳ�ʼ�˺ţ���Ҫ���� 10 ���˺����� 10 ����������룬����Ҫ�� 8 λ��ֻ
# �ܰ������� 0-9��Сд��ĸ a-z �Լ���д��ĸ A-Z��ÿ��������û���ظ����ַ���***��ʹ�ô����б�ÿ����Ҫ�˺Ž�ȥһһ��Ӧ
# import random,string
# def random_passwords():
#     src = string.ascii_letters + string.digits
#     list_passwords = []
#     kk1 = ['mtz1', 'mtz2', 'mtz3', 'mtz4', 'mtz5', 'mtz6', 'mtz7', 'mtz8']
#     for i in range(len(kk1)):
#         list_password_all = random.sample(src,5) #����ĸ�����������ѡȡ5λ
#         list_password_all.extend(random.sample(string.digits,1)) #��������һ����������
#         list_password_all.extend(random.sample(string.ascii_lowercase,1)) #��������һ������Сд
#         list_password_all.extend(random.sample(string.ascii_uppercase,1)) #��������һ��������д
#         random.shuffle(list_password_all) #�����б�˳��
#         str_password = ''.join(list_password_all) #���б�ת��Ϊ�ַ���
#         if str_password not in list_passwords: #�ж��Ƿ������ظ�����
#             list_passwords.append(str_password)
#             print (list_passwords)
# random_passwords()

# def get_formatted_name(first_name,last_name):
#     full_name = first_name + " " +last_name + "."
#     return full_name.title()
# musician = get_formatted_name('jim','hendirx')
# print (musician)

# def get_person(first_name,last_name,age=''):
#     person = {"first":first_name.title(),"last":last_name.title()}
#     if age:
#         person['age'] = age
#     return person
# musician = get_person('jim','hendirx',24)
# print (musician)

# def get_person(first_name,last_name,age=''):
#     person = {"first":first_name.title(),"last":last_name.title()}
#     if age:
#         person['age'] = age
#     return person
# while True:
#     print ("Please tell me your name")
#     f_name = raw_input("Firstname:")
#     if f_name == 'q':
#         break
#     l_name = raw_input("Lastname:")
#     if l_name == 'q':
#         break
#     a_age = raw_input("age:")
#     if a_age == 'q':
#         break
#     musician = get_person(f_name,l_name,a_age)
#     print (musician)

# �����б�
# def person(names):
#     for name in names:
#         message = "hello " + name + "."
#         print (message)
# username = ['haha','gaga','xixi']
# person(username)

# δ���
# list1 = ['abc','cde','efg']
# list2 = []
# if list1:
#     current_list = list1.pop[1:]
#     print ("Printing model: " + current_list)
#     list2.append(current_list)
# print("\nThe following models have been printed:")
# for a in list2:
#     print(list2)

# # py�Զ����ʼ�����   done
# # ��Ȩ�룺OXRSJBXXVPMZRBRQ
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# # ������ SMTP ����
# mail_host = "smtp.163.com"  # ���÷�����
# mail_user = "m15277337022@163.com"  # �û���
# mail_pass = "OXRSJBXXVPMZRBRQ"  # ����
# sender = 'm15277337022@163.com'
# receivers = ['yyc_yycong@163.com']  # �����ʼ���������Ϊ���QQ���������������
# message = MIMEText('ӱ讱�b', 'plain', 'utf-8')
# message['From'] = Header("˧��", 'utf-8')
# message['To'] = Header("ӱ�", 'utf-8')
# subject = 'Python SMTP �ʼ�����'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 Ϊ SMTP �˿ں�
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "�ʼ����ͳɹ�"
# except smtplib.SMTPException:
#     print "Error: �޷������ʼ�"

# ��
# -*-coding:utf-8-*-
# import os
# for root,dirs,files in os.walk("f:\\"):
#  for dir in dirs:
#   print os.path.join(root,dir).decode('gbk').encode('utf-8');
#  for file in files:
#   print os.path.join(root,file).decode('gbk').encode('utf-8');

# file_path = r'C:\Users\wb.miaotianze\Desktop\1.txt'
# with open(file_path) as file_object:
#     for line in file_object:
#         print (line)
# ָ���ļ���Ŀ¼�µ��ļ�ɨ����������
# ע���������б�ܣ�����·����ǰ��һ��r��Ҳ���Բ���rȫ�����ɷ�б��
# car��

# class Car(object):
#     """һ��ģ�������ĳ���"""
#     def __init__(self,make,model,year):
#         """��ʼ����������������"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descritive_name(self):
#         """���ؼ�����������Ϣ"""
#         long_name = str(self.year) + ' ' + self.make + ' ' +self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """���һ��ָ��������̵���Ϣ"""
#         print("This car has: " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self,mileage):
#         """����̱��������Ϊ���ֵ"""
#         """����̱��������Ϊ�ƶ�ֵ����ֹ����̱�������ص�"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("you can't roll back an odometer! ")
#
#     def increment_odometer(self,miles):
#         """����̱��������ָ����"""
#         self.odometer_reading += miles
#
#
# class Battery():
#     def __init__(self,battery_size = 70):
#         """��ʼ����ƿ���ԣ����class�ǽ�ʵ����������"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """��ӡһ�������ƿ��������Ϣ"""
#         print ("This car has a " + str(self.battery_size) + "-kWh battery. ")
#
#     def get_range(self):
#         range = 300
#         if self.battery_size <= 70:
#             range = 250
#         elif self.battery_size > 70:
#             range = 280
#         message = "This car can go approximately " + str(range)
#         message += "miles on a full charge!"
#         print(message)
#
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         """��ʼ���������ԣ��ٳ�ʼ���綯����������"""
#         super(ElectricCar,self).__init__(make,model,year)
#         self.battery = Battery()

    # def fill_gas_tank(self):
    #     """��д���෽����������ຬ��fill gas tank��ִ�����´���"""
    #     print ("This car doesn't need gas tank!")
# my_new_car = Car('audi','a6',2021)
# print(my_new_car.get_descritive_name())


# my_telsa = ElectricCar('telsa',"model s",2020)
# print(my_telsa.get_descritive_name())
# my_telsa.battery.describe_battery()
# my_telsa.battery.get_range()
# my_new_car.update_odometer(200)
# my_new_car.increment_odometer(22)
# my_new_car.read_odometer()


# a = 123
# b = "abc"
# print("hi,i am{}. i am from {}.".format(a,b))
# С����


# def twoSum(nums, target):
#     lens = len(nums)
#     j = 0
#     for i in range(lens):
#         if (target - nums[i]) in nums:
#             if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
#                 # ���num2=num1,��nums��ֻ������һ�Σ�˵���ҵ���num1����
#                 continue
#             else:
#                 j = nums.index(target - nums[i], i+1)
#                 # index(x,i+1)�Ǵ�num1������к���num2
#                 break
#     if j > 0:
#         return [i, j]
#     else:
#         return []
#
#
# sum_1 = twoSum((1, 2, 3, 4), 7)
# print(sum_1)


# def reverse_force(self, x: int):
#     if -10 < x < 10:
#         return x
#     str_x = str(x)
#     if str_x[0] != "-":
#         str_x = str_x[::-1]
#         x = int(str_x)
#     else:
#         str_x = str_x[:0:-1]
#         x = int(str_x)
#         x = -x
#     return x if -2147483648 < x < 2147483647 else 0

# # ɾ�����������е��ظ���
# class Solution(object):
#     def containsDuplicate(self, nums):
#         d = {}
#         for num in nums:
#             if num not in d:
#                 d[num] = 0
#             else:
#                 return True
#         return False



# def worker(a, b, c):
#     x = a + b
#     y = x * c
#     return y
#
#
# result = worker(1, 2, 3)

# 复习列表操作
# 打印列表，但是这种print出来是带括号的
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# print(str.split( ))       # 以空格为分隔符，包含 \n
# print(str.split(' ', 1))  # 以空格为分隔符，分隔成两个

# str = "Chris_iven+Chris_jack+Chris_lusy"
# print(str.split("+"))
# print(str.split("_"))
# 从selenium中导入webdriver
########################################################
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# # 指定chrom的驱动
# # 执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
# driver = webdriver.Chrome('C:\Python38\selencode\chromedriver.exe')
# # get 方法 打开指定网址
# driver.get('http://www.baidu.com')
# # 选择网页元素
# element_keyword = driver.find_element(By.ID, 'kw')
# # 输入字符
# element_keyword.send_keys('宋曲')
# # 找到搜索按钮
# element_search_button = driver.find_element(By.ID, 'su')
# # driver.quit()
#########################################################
# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()
##########################################################
# import matplotlib.pyplot as plt
#
# input_values = [1, 2, 3, 4, 5]
# # 给定x轴第一个坐标为1
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
# # 设置图标标题，并给坐标轴上加上标签
# plt.title("Squares Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Squares of Value", fontsize=14)
# # 设置刻度标记大小
# plt.tick_params(axis='both', labelsize=14)
# plt.show()
########################################################
# 使用scatter（）绘制散点图并设置其样式

# import matplotlib.pyplot as plt
# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
# plt.scatter(x_value, y_value, s=10)
# # 设置图标题并给坐标轴上加上标签
# plt.title("squares numbers", fontsize=24)
# plt.xlabel("value", fontsize=14)
# plt.ylabel("squares of value", fontsize=14)
# # 设置刻度标记大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()
#######################################################
# 自动计算数据
# import matplotlib.pyplot as plt
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# # c为设置的颜色
# plt.scatter(x_values, y_values, c=(0, 0.6, 0.8), edgecolors='none', s=4)
# # 设置图标题并给坐标轴上加上标签
# plt.title("squares numbers", fontsize=24)
# plt.xlabel("value", fontsize=14)
# plt.ylabel("squares of value", fontsize=14)
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 11000])
# plt.show()
###################################################
# 随机漫步
# 创建RandomWalk类
# from random import choice


# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#     def __init__(self, num_points=5000):
#         """初始化随机漫步的属性"""
#         self.num_points = num_points
#         # 所有随机漫步都始于(0, 0)
#         self.x_values = [0]
#         self.y_values = [0]
#     def fill_walk(self):
#         """计算随机漫步包含的所有点"""
#         while len(self.x_values) < self.num_points:
#             # 决定前进方向以及延这个方向前进的距离
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # 计算下一个点的x和y的值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)

import csv

with open(r'C:\Users\wb.miaotianze\Desktop\特技表.csv') as f:
    reader = csv.DictReader(f)
    head_row = next(reader)
    print(head_row)
    for index,column_header in enumerate(head_row):
        print(index, column_header)
        # enumerate是python的内置函数，意为枚举
