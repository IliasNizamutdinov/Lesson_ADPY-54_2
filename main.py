from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

def main():
    with open("phonebook_raw.csv",'r',encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    #pprint(contacts_list)
    contacts_name = []
    # TODO 1: выполните пункты 1-3 ДЗ
    for contact in contacts_list[1:]:
        #переделываем телефоны
        pattern_phone = r"(\+7|8)\s*\(*(\d\d\d)\)*\s*\-*(\d\d\d)\s*\-*(\d\d)\s*\-*(\d\d)\s*\(*(\д*\о*\б*\.*)\s*(\d*)\)*"
        sub_phone = r"+7(\2)\3-\4-\5 \6\7"
        contact[5] = re.sub(pattern_phone,sub_phone,contact[5]).strip()

        # приводим в порядок фамилии
        delimiter = ' '
        str_join = delimiter.join([contact[0],contact[1],contact[2]])
        str_list = str_join.split(delimiter)
        contact[0] = str_list[0]
        contact[1] = str_list[1]
        contact[2] = str_list[2]
        contacts_name.append([str_list[0],str_list[1],"","","","",""])
    #объединяем записи

    contacts_return = []
    contacts_return.insert(0,contacts_list[0])
    for contact in contacts_name:
        if contact not in contacts_return:
            contacts_return.append(contact)

    for contact_gr in contacts_return:
        for contact_ls in contacts_list:
            if contact_gr[0] == contact_ls[0] and contact_gr[1] == contact_ls[1]:
                if len(contact_gr[2]) == 0:
                    contact_gr[2] = contact_ls[2]
                if len(contact_gr[3]) == 0:
                    contact_gr[3] = contact_ls[3]
                if len(contact_gr[4]) == 0:
                    contact_gr[4] = contact_ls[4]
                if len(contact_gr[5]) == 0:
                    contact_gr[5] = contact_ls[5]
                if len(contact_gr[6]) == 0:
                    contact_gr[6] = contact_ls[6]


    # print(contacts_return)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w",encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_return)
        print("Всё успешно!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
