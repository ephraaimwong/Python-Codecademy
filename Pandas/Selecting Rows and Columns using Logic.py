import codecademylib
import pandas as pd

shoefly.csv
    id,first_name,last_name,email,shoe_type,shoe_material,shoe_color
    54791,Rebecca,Lindsay,RebeccaLindsay57@hotmail.com,clogs,faux-leather,black
    53450,Emily,Joyce,EmilyJoyce25@gmail.com,ballet flats,faux-leather,navy
    91987,Joyce,Waller,Joyce.Waller@gmail.com,sandals,fabric,black
    14437,Justin,Erickson,Justin.Erickson@outlook.com,clogs,faux-leather,red
    79357,Andrew,Banks,AB4318@gmail.com,boots,leather,brown
    52386,Julie,Marsh,JulieMarsh59@gmail.com,sandals,fabric,black
    20487,Thomas,Jensen,TJ5470@gmail.com,clogs,fabric,navy
    76971,Janice,Hicks,Janice.Hicks@gmail.com,clogs,faux-leather,navy
    21586,Gabriel,Porter,GabrielPorter24@gmail.com,clogs,leather,brown
    62083,Frances,Palmer,FrancesPalmer50@gmail.com,wedges,leather,white
    91629,Jessica,Hale,JessicaHale25@gmail.com,clogs,leather,red
    98602,Lawrence,Parker,LawrenceParker44@gmail.com,wedges,fabric,brown
    45832,Susan,Dennis,SusanDennis58@gmail.com,ballet flats,fabric,white
    33862,Diane,Ochoa,DO2680@gmail.com,sandals,fabric,red
    73431,Rebecca,Charles,Rebecca.Charles@gmail.com,boots,faux-leather,white
    93889,Jacqueline,Crane,JC2072@hotmail.com,wedges,fabric,red
    39888,Vincent,Stephenson,VS4753@outlook.com,boots,leather,black
    35961,Roy,Tillman,RoyTillman20@gmail.com,boots,leather,white
    24560,Thomas,Roberson,Thomas.Roberson@gmail.com,wedges,fabric,red
    28559,Angela,Newton,ANewton1977@outlook.com,wedges,fabric,red

#reads CSV is pandas format(table like excel)
orders = pd.read_csv("shoefly.csv")
#orders.head() will print first 5 rows by default, can specify more
print(orders.head())

#orders.email selects email column
emails = orders.email
print(emails)

#gets the row of which firstname == Francis and lastname == Palmer
frances_palmer = orders[(orders.first_name == "Frances") & (orders.last_name == "Palmer")]
print(frances_palmer)

#orders.columnname.isin(["value"]) will return "value" within the column
comfy_shoes = orders[orders.shoe_type.isin(["clogs", "boots", "ballet flats"])]