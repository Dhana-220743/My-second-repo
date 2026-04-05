import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, recall_score,precision_score
'''data = {
    'Size_sqft':[600,750,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
    'Price':[90000,110000,120000,135000,150000,165000,180000,200000,210000,225000,24000,250000,265000,280000,300000]
}
df = pd.DataFrame(data)

plt.scatter(df['Size_sqft'],df['Price'],color='blue')
plt.title("House size vs Price")
plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.show()

X = df['Size_sqft'].values.reshape(-1,1)
y = df['Price'].values
model = LinearRegression()
model.fit(X,y)
predicted_price = model.predict(np.array([[2100]]))
print(f"Predicted price for 2100 sqft : ${predicted_price[0]:.2f}")

plt.scatter(X,y,color='blue')
plt.plot(X,model.predict(X),color="red")
plt.title("House size vs price with Regression Line")
plt.xlabel("Size(sqft)")
plt.ylabel("Price($)")
plt.show()

print(f"Model coefficient (slope) : {model.coef_[0]:.2f}")
print(f"Model intercept :{model.intercept_:.2f}")

data = {
    'Advertising_budget':[5,7,8,10,12,15,18,20,22,25,27,30],
    'Sales':[25,30,34,40,48,55,60,70,75,82,90,100]
}
df = pd.DataFrame(data)
X = df['Advertising_budget'].values.reshape(-1,1)
y = df['Sales'].values
model = LinearRegression()
model.fit(X,y)

predict_sales = model.predict(np.array([[35]]))
print(f"Predict price when budget = 35 : ${predict_sales[0]:.2f}")

plt.scatter(X,y,color='blue')
plt.plot(X,model.predict(X),color='red')
plt.title("Advertising_budget vs Sales")
plt.xlabel("Advertising_budget")
plt.ylabel("Sales")
plt.show()

print(f"Model coefficient (slope) : {model.coef_[0]:.2f}")
print(f"Model intercept :{model.intercept_:.2f}")

data = {
    'Level':[1,2,3,4,5,6,7,8,9,10],
    'Salary':[30000,35000,40000,50000,65000,80000,100000,130000,170000,220000]
}
df = pd.DataFrame(data)
X = df['Level'].values.reshape(-1,1)
y = df['Salary'].values
model = LinearRegression()
model.fit(X,y)

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly,y)

X_range = np.linspace(1,10,100).reshape(-1,1)
# linear prediction
y_lin = model.predict(X_range)
# polynomial prediction
y_poly = poly_model.predict(poly.transform(X_range))


# Plot
plt.scatter(X, y)
plt.plot(X_range, y_lin)     # Linear line
plt.plot(X_range, y_poly)    # Polynomial curve
plt.title("Level vs Salary")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

linear_predict = model.predict(np.array([[11]]))
poly_predict = poly_model.predict(poly.transform(np.array([[11]])))
print("Linear prediction :",linear_predict[0])
print("Polynomial prediction:",poly_predict[0])

data = {
    'Temperature':[20,22,24,26,28,30,32,34,36,38],
    'Sales':[120,140,160,200,250,300,360,420,480,550]
}
df = pd.DataFrame(data)
X = df['Temperature'].values.reshape(-1,1)
y = df['Sales'].values
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly,y)
#plot
X_range = np.linspace(20,40,100).reshape(-1,1)
y_pred = poly_model.predict(poly.transform(X_range))

plt.scatter(X,y)
plt.plot(X_range,y_pred)
plt.title("Temperature vs Sales (Polynomial Regression)")
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.show()

poly_predict = poly_model.predict(poly.transform(np.array([[40]])))
print("Predicted sales:",poly_predict[0])


data = {
    'Study_hours': [2,3,3,4,5,6,6,7,8,9,10],
    'Sleep_hours': [6,7,6,7,6,7,8,7,7,8,8],
    'Attendance': [70,75,80,85,88,90,92,94,95,97,98],
    'Score': [55,60,62,68,72,78,82,86,90,94,96]
}

df = pd.DataFrame(data)
X = df[['Study_hours', 'Sleep_hours', 'Attendance']]
y = df['Score'].values
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[7, 7, 90]])
print("Predicted Score:", prediction[0])
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

data = {
    'Area':[1000,1200,1400,1600,1800,2000,2200,2400,2600,2800],
    'Bedrooms':[2,2,3,3,3,4,4,4,5,5],
    'Age':[10,8,6,5,4,3,2,2,1,1],
    'Price':[150000,180000,220000,250000,280000,310000,340000,370000,420000,450000]
}
df= pd.DataFrame(data)
X = df[['Area','Bedrooms','Age']]
y = df['Price']
model = LinearRegression()
model.fit(X,y)
predict = model.predict([[2100,4,2]])
print("Prediction : ",predict[0])

data = {
    'Message_length':[120,80,200,60,300,150,90,70,250,100,180,85],
    'Links':[1,0,1,0,1,1,0,0,1,0,1,0],
    'Spam':[1,0,1,0,1,1,0,0,1,0,1,0]
}
df = pd.DataFrame(data)
X = df[['Message_length','Links']]
y = df['Spam']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state =42)
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Actual:", y_test.values)

data = {
    'Income':[30000,40000,50000,25000,45000,32000,60000,70000,20000,52000],
    'Credit_score':[650,700,720,600,680,640,750,780,580,710],
    'Loan_approved':[0,1,1,0,1,0,1,1,0,1]
}
df = pd.DataFrame(data)
X = df[['Income','Credit_score']]
y = df['Loan_approved']

model = LinearRegression()
model.fit(X,y)
predict_model = model.predict([[48000,690]])
print("Predicted value:",predict_model[0])'''

data = {
    'Age':[45,50,30,25,60,55,35,40,65,28],
    'BP':[130,140,120,11,150,145,125,128,155,115],
    'Cholesterol':[200,220,180,170,240,230,190,195,250,175],
    'Disease':[1,1,0,0,1,1,0,0,1,0]
}
df = pd.DataFrame(data)
X = df[['Age','BP','Cholesterol']]
y = df['Disease']
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,stratify =y
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Actual:", y_test.values)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)