# Developed by Dhananjay Singh
def no_of_day(inp):
	if int(inp[2])>=2020 and int(inp[0])>0 and int(inp[0])<=31 and int(inp[1])<=12 and int(inp[1])>=1:
		year=int(inp[2])-2020
		month=int(inp[1])-4
		day=int(inp[0])-1
		return year*365+month*30+day
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
pkjj=open('corona.txt','r').read()
pkjj=pkjj.split("\n")
new=[]
for line in pkjj:
	al=line.split()
	if al:
		al[1]=al[1]+" "+al[2]
		del(al[2])
		new.append(al)
df=pd.DataFrame(new,columns=["Serial","Date","Daily_Confirmed","Total_Confirmed","Daily_Recovered","Total_Recovered","Daily_Deceased","Total_Deceased"])
print ("Choose \n 1: Daily_Confirmed \n 2: Total_Confirmed \n 3: Daily_Recovered \n 4: Total_Recovered \n 5: Daily_Deceased \n 6: Total_Deceased \n")
n=int(input("Choose the option"))
if n==1:
	x=df[["Serial"]]
	y=df[["Daily_Confirmed"]]
	pkjj=LinearRegression().fit(x,y)
	inp=raw_input("Enter Date in the Format of DD-MM-YYYY").split("-")
	print pkjj.predict(no_of_day(inp))
elif n==2:
	x=df[["Serial"]]
        y=df[["Total_Confirmed"]]
        x_train,x_test,y_train,y_test=train_test_split(x,y)
        pkjj=LinearRegression().fit(x,y)
	inp=raw_input("Enter Date in the Format of DD-MM-YYYY").split("-")
        print pkjj.predict(no_of_day(inp))

if n==3:
        x=df[["Serial"]]
        y=df[["Daily_Recovered"]]
        pkjj=LinearRegression().fit(x,y)
	inp=raw_input("Enter Date in the Format of DD-MM-YYYY").split("-")
        print pkjj.predict(no_of_day(inp))

elif n==4:
        x=df[["Serial"]]
        y=df[["Total_Recovered"]]
        x_train,x_test,y_train,y_test=train_test_split(x,y)
        pkjj=LinearRegression().fit(x,y)
	inp=raw_input("Enter Date in the Format of DD-MM-YYYY").split("-")
        print pkjj.predict(no_of_day(inp))

if n==5:
        x=df[["Serial"]]
        y=df[["Daily_Deceased"]]
        pkjj=LinearRegression().fit(x,y)
	inp=raw_input("Enter Date in the Format of DD-MM-YYYY").split("-")
        print pkjj.predict(no_of_day(inp))

elif n==6:
        x=df[["Serial"]]
        y=df[["Total_Deceased"]]
        x_train,x_test,y_train,y_test=train_test_split(x,y)
        pkjj=LinearRegression().fit(x,y)
	inp=raw_input("Enter Date in the Format of DD-MM-YYYY").split("-")
        print pkjj.predict(no_of_day(inp))

