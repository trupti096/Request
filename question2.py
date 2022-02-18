import json
import requests
res = requests.get("http://saral.navgurukul.org/api/courses")
data_text=res.json()
#print(data_text)
# data1=(data_text["availablecourses"])
with open ("request.json","w") as file:
    a=json.dump(data_text,file,indent=4)
b=json.dumps(a)
print(type(b))
def course():
    index=1
    for i in data_text["availablecourses"]:
        print(index,i["name"],i["id"])
        index=index+1
    for c in data_text["availablecourses"]:
        course=int(input("select your course  ")) 
        select=data_text["availablecourses"][course-1]["id"] 
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises") 
        data2=var.json()
        print(data2) 
    for course in data_text["availablecourses"]:
        course=int(input("select your course  ")) 
        select=data_text["availablecourses"][course-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses"+str(select)+"/exercise/get")
        data2=var.json()
        print(data2)
        
course()