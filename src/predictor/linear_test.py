import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from model.seasons import PastSeasons


def linear_regression(new_data=None):

    pd.set_option("display.max_rows", None, "display.max_columns", None)

    files = [x for x in map("{0}.csv".format, PastSeasons)]
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)

    train = df.sample(frac=0.8, random_state=200)
    targetsColumnName = train.columns[len(train.columns)-1]
    print(targetsColumnName)
    targets = train[targetsColumnName].to_list()
    train.drop(targetsColumnName, axis=1, inplace=True)

    test = df.drop(train.index)

    # create LR model
    model = LinearRegression()

    # Fit
    model.fit(train, targets)

    # r-squared
    y_pred = model.predict(train)
    r_squared = r2_score(targets, y_pred)
    print("R-squared: ", r_squared)

    # P-Values
    x_intercept = sm.add_constant(train)
    model_sm = sm.OLS(targets, x_intercept).fit()
    print("P-Values: ", model_sm.pvalues)

    # Coefficients
    print("Coef: ", model.coef_)
    print("Intercept: ", model.intercept_)

    # Predictions
    if new_data is not None:
        predictions = model.predict(new_data)
        print("Predictions based on new data: ", predictions)

linear_regression()