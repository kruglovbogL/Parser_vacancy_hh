#!/usr/bin/python
# -*- coding: UTF - 8
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns


def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"  # загрузка с помощью api
    params = {
        "text": keyword,
        "area": 1,  # Если 1 то Москва или поиск пор всем районам
        "per_page": 50,  # Количество страниц для поиска
    }
    headers = {  # голова запроса, без нее запрос не выполниться
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/123.0.0.0 Safari/537.36",  # Заменить на свой браузер

    }

    response = requests.get(url, params=params, headers=headers)

    data_frame = pd.DataFrame()  # создание DataFrame с данными
    if response.status_code == 200:  # если статус код 200 то
        data = response.json()  # получить json
        vacancies = data.get("items", [])  # получить items
        for vacancy in vacancies:
            # Информация о вакансиях id, job, title, url, name
            vacancies_cash = vacancy.get("money")
            vacancy_id = vacancy.get("id")
            vacancy_job = vacancy.get("schedule", {}).get("name")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            print(
                f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\nJob: {vacancy_job}\n")
            data_frame = data_frame._append(vacancy, ignore_index=True)
            data_frame.to_csv('list_vacancies.csv', index=False)  # создание файла с данными
    else:
        print(f"Request failed with status code: {response.status_code}")  # другой статус код НЕ 200.


get_vacancies("python developer junior")  # запрос текста INPUT

X = pd.read_csv('list_vacancies.csv')  # чтение csv файла
X.describe()
print(X.columns)
new_data = X.dropna()

fig = plt.figure
fig, ax = plt.subplots(figsize=(7, 7))
sns.distplot(X.id, color='red', label='bmi', ax=ax)  # seaborn график по id вакансий, запихнуть любые ЧИСЛОВЫЕ данные DATAFRAME
plt.show()