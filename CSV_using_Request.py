import requests, json, csv
from requests.auth import HTTPBasicAuth

file = open(r"C:\Users\nisha\Desktop\py4e\Request\Devops\Sonarqube_Projects.csv",'w', newline='')

url = "http://localhost:9000/api/projects/search"

response = requests.get(url,auth = HTTPBasicAuth('admin', 'Kiran@123'))

responsedata = response.json()   #converting to dictionary format using json method

writer = csv.writer(file) #Writer function in CSV
writer.writerow(['Key','Name','Visibility']) #Defining columns for required fields

#for loop to loop through the fields and input all required fields in writerow function
for i in range(len(responsedata['components'])):
    writer.writerow([responsedata['components'][i]['key'], responsedata['components'][i]['name'], responsedata['components'][i]['visibility']])

file.close()


'''
#Read file
file = open("C:/Users/nisha/Desktop/py4e/Request/Devops/Sonarqube_Projects.csv",'r', newline='')

reader = csv.reader(file)  #Reader function in CSV
for line in reader:
    print(line)

file.close()
'''
