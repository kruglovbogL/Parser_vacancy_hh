import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1,  # Specify the desired area ID (1 is Moscow)
        "per_page": 50,  # Number of vacancies per page
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

resylt = X['id'].tolist()
print(resylt)
colums = X.columns.tolist()
print(colums)
resuly = X[['name', 'schedule', 'url', 'employer', 'id']]
df = pd.DataFrame(resuly)

df.id.unique()
df.plot()
plt.show()


#
# # Numpy array of all the cluster labels assigned to each data point
# db_default = DBSCAN(eps = 0.0375, min_samples = 3).fit(X_principal)
# labels = db_default.labels_
# #-----------------------------------------------------------------
# # Building the label to colour mapping
# colours = {}
# colours[0] = 'r'
# colours[1] = 'g'
# colours[2] = 'b'
# colours[-1] = 'k'
#
# # Building the colour vector for each data point
# cvec = [colours[label] for label in labels]
#
# # For the construction of the legend of the plot
# r = plt.scatter(X_principal['P1'], X_principal['P2'], color ='r');
# g = plt.scatter(X_principal['P1'], X_principal['P2'], color ='g');
# b = plt.scatter(X_principal['P1'], X_principal['P2'], color ='b');
# k = plt.scatter(X_principal['P1'], X_principal['P2'], color ='k');
#
# # Plotting P1 on the X-Axis and P2 on the Y-Axis
# # according to the colour vector defined
# plt.figure(figsize =(9, 9))
# plt.scatter(X_principal['P1'], X_principal['P2'], c = cvec)
#
# # Building the legend
# plt.legend((r, g, b, k), ('Label 0', 'Label 1', 'Label 2', 'Label -1'))
#
# plt.show()
