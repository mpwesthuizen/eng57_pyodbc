import pyodbc


server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_string ='DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

# print(db_string)

py_connect2 = pyodbc.connect(db_string)

cursor = py_connect2.cursor()

print(cursor)

query_result = cursor.execute('SELECT * FROM Products')
all_results_list = query_result.fetchall()
row = query_result.fetchone()
#
# print(query_result.fetchone())
# # print(query_result.fetchall())
#


# for data in all_results_list:
#     print(data.ProductName, 'costs', data.UnitPrice)

# Search documentation/or internet to use a for loop to get our all of the data using the .fetchone() method

# while True:
#     if row is None:
#         break
#     print(row)
