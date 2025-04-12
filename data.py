#Задача 1:

# import json
# import requests

# response = requests.get("https://dummyjson.com/products")

# if response.status_code == 200:
#     data = response.json()
#     print(f'Title: {data["products"][0]["title"]}')  
#     print(f'Category: {data["products"][0]["category"]}')  
#     print(f'Rating: {data["products"][0]["rating"]}/5')  
#     print(f'Price: {data["products"][0]["price"]}$') 
#     total_price = 0
#     total_products = len(data["products"])
#     for product in data["products"]:
#         total_price += product["price"]
#         if product["rating"] == 5:
#             print(f"Rating is 5 for product: {product['title']}")
#             print(f'Title: {product["title"]}')  
#         if not product["rating"] == 5:
#             print(f"Product with rating 5 not found")
#             break
#     print(f'Avg price: {total_price / total_products}$') 
# else:
#     print(f"Error: {response.status_code}")
#     print("Failed to retrieve data.")


# response = requests.get("https://google.com/")

# if response.status_code == 200:
#     print("Google is up and running!")
#     print(f"Response time: {response.elapsed.total_seconds()} seconds")
#     print(f"Response content: {response.content[:100]}...")  # Print the first 100 characters of the response


# #Задача 2:

# from bs4 import BeautifulSoup

# response = requests.get("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")

# if response.status_code == 200:
    
#     root = BeautifulSoup(response.text, "xml")

#     usd = root.find("Cube").find("Cube", {"currency": "USD"})
#     if usd:
#         print("USD Rate:", usd["rate"])
#     else:
#         print("USD rate not found in the XML data.")

#     foot = root.find("Cube").find("Cube", {"currency": "GBP"})
#     if foot:
#         print("GBP Rate:", foot["rate"])
#     else:
#         print("GBP rate not found in the XML data.")
# else:
#     print(f"Error: {response.status_code}")
#     print("Failed to retrieve data.") 

#Задача 3:

# import pandas as pd

# df = pd.read_csv("./assets/products.csv", delimiter=",", quotechar='"')
# print("CSV Data:")
# print(df.head()) 

# passengers_33_yo = df[df["Age"] <= 33]  

# print("Passengers aged 33 or younger:")
# print(passengers_33_yo["Name"])

# current_year = 1912
# passengers_33_yo["birth_year"] = current_year - passengers_33_yo["Age"]

# print(passengers_33_yo[["Name","Age","birth_year"]])

