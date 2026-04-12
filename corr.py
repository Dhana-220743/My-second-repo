import numpy as np

x = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]
y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]

# correlation matrix
data = np.corrcoef(x, y)

print("Correlation Matrix:")
print(data)

x = [43, 21, 25, 42, 57, 59]
y = [99, 65, 79, 75, 87, 81]

correlation = np.corrcoef(x, y)

print("Correlation between Age and Glucose:")
print(correlation)

import pandas as pd

data = {
    'x': [45, 37, 42, 35, 39],
    'y': [38, 31, 26, 28, 33],
    'z': [10, 15, 17, 21, 12]
}

df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nCorrelation Matrix:")
print(df.corr())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset (Boston housing - replace if needed)
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['MEDV'] = data.target

# 1. Dimensions
print("Shape:", df.shape)

# 2. Summary
print(df.describe())

# 3. Independent and dependent variable
X = df[['MedInc']]   # (similar to lstat concept)
y = df['MEDV']

# 4. Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Intercept and slope
print("Intercept:", model.intercept_)
print("Slope:", model.coef_)

# 7. Prediction
y_pred = model.predict(X_test)

# 8. Actual vs predicted
print("\nPredicted values:", y_pred[:5])
print("Actual values:", y_test[:5].values)

# 9. Evaluation
print("\nMAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# 10. Plot
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title("Linear Regression")
plt.show()
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    'year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,
             2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
    'month': [12,11,10,9,8,7,6,5,4,3,2,1,
              12,11,10,9,8,7,6,5,4,3,2,1],
    'interest_rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,
                      2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
    'unemployment_rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,
                           6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
    'stock_index_price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,
                          1047,965,943,958,971,949,884,866,876,822,704,719]
}

df = pd.DataFrame(data)

# Independent variables
X = df[['interest_rate', 'unemployment_rate']]

# Dependent variable
y = df['stock_index_price']

# Model
model = LinearRegression()
model.fit(X, y)

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Equation
print("\nEquation:")
print("stock_index_price =",
      model.intercept_,
      "+", model.coef_[0], "* interest_rate",
      "+", model.coef_[1], "* unemployment_rate")

# Prediction
y_pred = model.predict(X)

print("\nSample predictions:")
print(y_pred[:5])