import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

file = 'Vehicle_Sales.csv'
df = pd.read_csv(file)

print("""
    Лабораторна номер 1
    Виконав Корець Олександр КМ-92
    Підгрупа 1
""")

print("\ntask1 - відкрити файл із даними")
df = pd.read_csv(file)
print(df.describe())
input("\nenter something to continue")

print("\ntask2 - визначити та вивисти кількість записів та полів в кожному записі")
df.info()
input("\nenter something to continue")

print("\ntask3 - вивести К+7 перших та 5К-3 останіх записів")
k = int(input("введіть k - натуральне число:"))
print(df.head(k+7))
print(df.tail(5*k-3))
input("\nenter something to continue")

print("\ntask4 - визначити та вивести тип полів та кожного запису")
df.info()
input("\nenter something to continue")

print("\ntask5 - привести поля що відповідають обсягам продаж до числового значення")
df["Total Sales New"] = df["Total Sales New"].apply(lambda x: int(x[1:]))
df["Total Sales Used"] = df["Total Sales Used"].apply(lambda x: int(x[1:]))
print(df)
input("\nenter something to continue")

print("\ntask6 - вести нові поля: [сума продаж нових+б/н, сумарний дохід нових+б/у, Різниця в обсязі продаж нових-б/у]")
df["New+Used"] = df["New"] + df["Used"]
df["Sales New+Used"] = df["Total Sales Used"] + df["Total Sales New"]
df["Sales New-Used"] = df["Total Sales New"] - df["Total Sales Used"]
print(df)
input("\nenter something to continue")

print("\ntask7 - змінити порядок розташування полів")
print(df)
df = df[["Year","Month","Sales New+Used","Total Sales New","Total Sales Used","New+Used","New","Used","Sales New-Used"]]
print(df)
input("\nenter something to continue")

print("\ntask8")
print(df)
print(df[["Year", "Month"]][df["New"] < df["Used"]])
print(df[["Year", "Month"]][df["Sales New+Used"] == df["Sales New+Used"].min()])
print(df[["Year", "Month"]][df["Used"] == df["Used"].max()])
input("\nenter something to continue")

print("\ntask9")
print(df)
print(df[["Year", "Sales New+Used"]].groupby(["Year"]).sum())
# my number in group list = 6
print(df[["Month", "Sales New+Used"]][df["Month"] == "JAN"].groupby(["Month"]).mean())
input("\nenter something to continue")

print("\ntask10")
df2 = df[["Year", "Month", "New"]][df["Year"] == int(f"20{17-6}")]
fig1 = plt.bar(df2["Month"], df2["New"])
plt.show()

print("\ntask11")
df2 = df[["Year", "Sales New+Used"]].groupby(["Year"]).sum()
fig2 = plt.pie(df2["Sales New+Used"])
plt.show()

print("\ntask12")
df2 = df[["Year", "Total Sales Used"]].groupby(["Year"]).sum()
plt.plot(df2.index, df2["Total Sales Used"])
df2 = df[["Year", "Total Sales New"]].groupby(["Year"]).sum()
plt.plot(df2.index, df2["Total Sales New"])
plt.show()



