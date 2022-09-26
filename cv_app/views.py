





from django.shortcuts import render
from django.http import HttpResponse
    
def index_cv(request):

    import json

    chemin = 'cv_app\static\index\json\data.json'

    with open(chemin) as json_data:
        data_dict = json.load(json_data)
    
    name = data_dict["Nom"]
    lastname = data_dict["Prenom"]
    age = data_dict["Age"]
    phone = data_dict["Telephone"]
    street = data_dict["Adresse"]
    mail = data_dict["Mail"]


    return render(request,"index/index.html",  {"name": name, "lastname": lastname, "age": age, "phone": phone, "street": street, "mail": mail})













