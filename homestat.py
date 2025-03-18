#!/usr/bin/env python3
import re


class Year_stat:
    def __init__(self, age_of_studying):
        self.names_dict = dict()
        self.age_of_studying = age_of_studying

    def add(self, name):
        if not(name in self.names_dict):
            self.names_dict[name] = 1
        else:
            self.names_dict[name] += 1


def get_all_year_stat(stat):
    all_students_dict = dict()
    for element in stat:
        for i in element.names_dict:
            if not (i in all_students_dict):
                all_students_dict[i] = element.names_dict[i]
            else:
                all_students_dict[i] += element.names_dict[i]
    return all_students_dict

cqcwas = 1

def make_stat(filename):
    file_text = open(filename, "r", encoding="cp1251").read()
    need_to_find = r'(?<=>)[а-яА-Я0-9ёЁйЙ ]+(?=<)'
    text_list = re.findall(need_to_find, file_text)
    stat_lsit = []
    stat_now = Year_stat(int(text_list[0]))

    for i in range(1, len(text_list)):
        if '0' <= text_list[i][0] <= '9':
            stat_lsit.append(stat_now)
            stat_now = Year_stat(int(text_list[i]))
        else:
            stat_now.add(text_list[i].split()[1])

    stat_lsit.append(stat_now)
    return stat_lsit


def extract_years(stat):
    years = []
    for element in stat:
        years.append(element.age_of_studying)
    years.sort()
    for i in range(len(years)):
        years[i] = str(years[i])
    return years


def extract_general(stat):
    list = []
    all_students_dict = get_all_year_stat(stat)
    for i in all_students_dict:
        list.append([all_students_dict[i], i])
    list.sort(reverse=True)
    for i in list:
        i[0], i[1] = i[1], i[0]
    for i in range(len(list)):
        list[i] = tuple(list[i])
    return list


def extract_general_male(stat):
    all_studets_dict = get_all_year_stat(stat)
    list = []
    mans_names = ["Илья", "Игорь", "Никита", "Лёва"]
    for i in all_studets_dict:
        if i[-1] not in ['а', 'я', 'ь'] or i in mans_names:
            list.append([all_studets_dict[i], i])
    list.sort(reverse=True)
    for i in list:
        i[0], i[1] = i[1], i[0]
    for i in range(len(list)):
        list[i] = tuple(list[i])
    return list


def extract_general_female(stat):
    all_studets_dict = get_all_year_stat(stat)
    list = []
    mans_names = ["Илья", "Игорь", "Никита", "Лёва"]
    for i in all_studets_dict:
        if i[-1] in ['а', 'я', 'ь'] and i not in mans_names:
            list.append([all_studets_dict[i], i])
    list.sort(reverse=True)
    for i in list:
        i[0], i[1] = i[1], i[0]
    for i in range(len(list)):
        list[i] = tuple(list[i])
    return list


def extract_year(stat, year):
    this_year_list = []
    for i in stat:
        if i.age_of_studying == int(year):
            this_year_list.append(i)
    return tuple(extract_general(this_year_list))


def extract_year_male(stat, year):
    this_year_list = []
    for i in stat:
        if i.age_of_studying == int(year):
            this_year_list.append(i)
    return extract_general_male(this_year_list)


def extract_year_female(stat, year):
    this_year_list = []
    for i in stat:
        if i.age_of_studying == int(year):
            this_year_list.append(i)
    return extract_general_female(this_year_list)


if __name__ == '__main__':
    pass
