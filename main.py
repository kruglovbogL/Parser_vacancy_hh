import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns


def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"  # �������� � ������� api
    params = {
        "text": keyword,
        "area": 1,  # ���� 1 �� ������ ��� ����� ��� ���� �������
        "per_page": 50,  # ���������� ������� ��� ������
    }
    headers = {  # ������ �������, ��� ��� ������ �� �����������
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/123.0.0.0 Safari/537.36",  # �������� �� ���� �������

    }

    response = requests.get(url, params=params, headers=headers)

    data_frame = pd.DataFrame()  # �������� DataFrame � �������
    if response.status_code == 200:  # ���� ������ ��� 200 ��
        data = response.json()  # �������� json
        vacancies = data.get("items", [])  # �������� items
        for vacancy in vacancies:
            # ���������� � ��������� id, job, title, url, name
            vacancy_id = vacancy.get("id")
            vacancy_job = vacancy.get('schedule', {}).get("name")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            print(
                f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\nJob: {vacancy_job}\n")
            data_frame = data_frame._append(vacancy, ignore_index=True)
            data_frame.to_csv('list_vacancies.csv', index=False)  # �������� ����� � �������
    else:
        print(f"Request failed with status code: {response.status_code}")  # ������ ������ ��� �� 200.


get_vacancies("python developer junior")  # ������ ������ INPUT

X = pd.read_csv('list_vacancies.csv')  # ������ csv �����
X.describe()
print(X.columns)
new_data = X.dropna()

fig = plt.figure
fig, ax = plt.subplots(figsize=(7, 7))
sns.distplot(X.id, color='red', label='bmi', ax=ax)  # seaborn ������ �� id ��������, ��������� ����� �������� ������
plt.show()
