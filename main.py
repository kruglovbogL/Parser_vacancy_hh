import pandas as pd
import requests


def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1,  # Specify the desired area ID (1 is Moscow)
        "per_page": 30,  # Number of vacancies per page
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",  # Replace with your User-Agent header
    }

    response = requests.get(url, params=params, headers=headers)

    # Creating a DataFrame
    df = pd.DataFrame()
    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            # Extract relevant information from the vacancy object
            vacancy_id = vacancy.get("id")
            vacancy_job = vacancy.get('schedule', {}).get("name")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            print(f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\nJob: {vacancy_job}\n")
            df = df._append(vacancy, ignore_index=True)
            df.to_csv('movie_example1.csv', index=False)
    else:
        print(f"Request failed with status code: {response.status_code}")
# Example usage
get_vacancies("python developer junior")

X = pd.read_csv('movie_example1.csv')

result = X['id'].tolist()
print(result)
colums = X.columns.tolist()
print(colums)
resultat = X[['name', 'response_url', 'schedule', 'employment']]
print(resultat)
