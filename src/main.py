import os

from HeadHunterParser import HeadHunterParser


def filter_vacancies(vacancies_list, keyword_list):
    ret_vacancies_list = []
    for vacancy_item in vacancies_list:
        if keyword_list in vacancy_item:
            ret_vacancies_list.append(vacancy_item)
    return ret_vacancies_list


def get_vacancies_by_salary(vacancies_list, min_value, max_value):
    ret_vacancies_list = []
    for vacancy_item in vacancies_list:
        if vacancy_item.is_salary_between(min_value, max_value):
            ret_vacancies_list.append(vacancy_item)
    return ret_vacancies_list


def get_sorted_vacancies(vacancies_list, reverse=True):
    vacancies_list.sort(reverse=reverse)
    return vacancies_list


def get_top_vacancies(vacancies_list, amount_of_values):
    if amount_of_values > len(vacancies_list):
        return vacancies_list
    else:
        return vacancies_list[0:amount_of_values]


def get_formatted_vacancies(vacancies_list):
    for vacancy_item in vacancies_list:
        print(vacancy_item)

# Функция для взаимодействия с пользователем


def user_interaction():
    is_online = False

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    filename = os.path.join("..", "data", "hh_python.json")
#    filename = os.path.join("..", "data", "vacancies_example.json")
    hh = HeadHunterParser(filename)
    if is_online:
        # Получение вакансий с hh.ru в формате JSON
        hh.load_vacancies("Python")
        hh.save_to_file()
    else:
        hh.load_from_file()

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = hh.parse_and_verify()

    # search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # keyword_list = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    top_n = 5
    keyword_list = ["танц"]
    keyword_list = ["Python", "Git"]
    salary_min = 1
    salary_max = 1e9

    filtered_vacancies = filter_vacancies(vacancies_list, keyword_list)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_min, salary_max)
    sorted_vacancies = get_sorted_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    get_formatted_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()