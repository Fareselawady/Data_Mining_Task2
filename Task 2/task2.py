import pandas as pd
import os 

mydt=pd.DataFrame({
'ID':[11, 12, 13, 14, 15],
'first_name': ['David', 'Jamie', 'Steve', 'Stevart', 'John'],
'company': ['Aon', 'TCS', 'Google', 'RBS', '.'],
'salary': [74, 76, 96, 71, 78]})
os.getcwd()
print(mydt)
os.chdir("C:\\Users\\DELL\\Desktop\\Mawlana")
mydt.to_csv("mydata.txt")

print("===============================================")

a=pd.read_csv("mydata.txt")
print(a)

print("===============================================")

b=pd.read_csv("task.txt",header=1)
print(b)

print("===============================================")

c=pd.read_csv("task.txt",usecols=['id','item'],nrows=3)
print(c)

print("===============================================")

x=pd.read_csv("iris.csv")
print(x)

print("===============================================")

x.loc[1]
x.loc[:,'species']
x.iloc[:,4]


print("===============================================")

xx=x.drop([1,4],axis=0)
print(xx)


print("===============================================")

yy=x.drop(['sepal_width','sepal_length'], axis=1)
print(yy)


print("===============================================")
x.describe()



print("===============================================")

x['sepal_length'].describe()


print("===============================================")

x.describe(include=['O'])


print("===============================================")

z=x.query('(species =="versicolor")')
print(z)

print("===============================================")

zz=x.sort_values(by='sepal_width', ascending=True)
print(zz)

print("===============================================")

x["species"].astype('category')


print("===============================================")

x['sepal_length'].hist()


print("===============================================")

x.boxplot(column='sepal_width')

