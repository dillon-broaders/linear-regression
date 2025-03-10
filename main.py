import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm  

def read_data(filename, x_col, y_col, x_err_col=None, y_err_col=None):
    """
    reads excel file and returns x, y, x_err, and y_err values
    """
    dataset = pd.read_excel(filename)
    x = dataset[x_col].values
    y = dataset[y_col].values
    x_err = dataset[x_err_col].values if x_err_col else None
    y_err = dataset[y_err_col].values if y_err_col else None
    return x, y, x_err, y_err


def perform_regression(x, y):
    """
    perform linear regression and returns slope, intercept, R^2, error in slope, 
    and error in intercept
    """
    X = sm.add_constant(x)  
    model = sm.OLS(y, X).fit()  

    # get regression info
    slope = model.params[1]  
    intercept = model.params[0]  
    r_squared = model.rsquared  
    std_err_slope = model.bse[1]  
    std_err_intercept = model.bse[0]  

    return slope, intercept, r_squared, std_err_slope, std_err_intercept


def plot_regression(x, y, x_err, y_err, slope, intercept, r_squared, std_err_slope, std_err_intercept, x_label, y_label):
    """
    returns plot with data, line of best fit, and regression information
    """
    # regression line
    x_range = np.linspace(min(x), max(x), 100)
    y_pred = slope * x_range + intercept

    # regression plot with data
    plt.figure(figsize=(8, 6))
    plt.plot(x_range, y_pred, color='red')

    if x_err is not None and y_err is not None:
        plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', color='blue', ecolor='black', capsize=3)
    else:
        plt.scatter(x, y, color='blue')

    # regression information box
    textstr = f"Slope: {slope:.3f} ± {std_err_slope:.3f}\nIntercept: {intercept:.3f} ± {std_err_intercept:.3f}\nR²: {r_squared:.3f}"
    plt.text(0.06, 0.85, textstr, transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle="square", facecolor="white"))

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'Plot of {x_label} vs {y_label}')
    plt.grid()
    plt.savefig("linear_regression_plot.png")
    plt.show()


# enter file info here 
filename = 'my_file.xlsx'  # excel file containing data
x_col_name = 'x'           # x values column
y_col_name = 'y'           # y values column
x_err_col_name = 'xerr'    # x errors column (set None if unavailable)
y_err_col_name = 'yerr'    # y errors column (set None if unavailable)

x, y, x_err, y_err = read_data(filename, x_col_name, y_col_name, x_err_col_name, y_err_col_name)
slope, intercept, r_squared, std_err_slope, std_err_intercept = perform_regression(x, y)
plot_regression(x, y, x_err, y_err, slope, intercept, r_squared, std_err_slope, std_err_intercept, x_col_name, y_col_name)
