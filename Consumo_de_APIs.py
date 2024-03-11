
import requests

# API 1
url_api1 = 'https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500'
api1 = requests.get(url_api1)
if api1.status_code == 200:
  data1 = api1.json()
  print("La conexion con la api 1 fue correcta")
else:
  print("Error de conexion con la api ")
print(data1)
print()


# API 2
url_api2 = 'https://fakerapi.it/api/v1/persons?_quantity=1&_gender=male&_birthday_start=2005-01-01'
api2 = requests.get(url_api2)
if api2.status_code == 200:
  data2 = api2.json()
  print("La conexion con la api 2 fue correcta")
else:
  print("Error de conexion con la api ")
print(data2)
print()


# API 3
url_api3 = 'https://fakerapi.it/api/v1/books?_quantity=1'
api3 = requests.get(url_api3)
if api3.status_code == 200:
  data3 = api3.json()
  print("La conexion con la api 3 fue correcta")
else:
  print("Error de conexion con la api ")
print(data3)
