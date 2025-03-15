# Linear regression 

This Python program reads data from an Excel file, performs linear regression, and generates a plot with the line of best fit. It also calculates the slope, 
intercept, R² value, and their respective errors. It displays this regression information plus any error bars for both x and y values.

## Motivation

During my undergraduate labs, MacOS users couldn't use a data analsis software called Origin for data analysis. I created this program to generate linear regression plots for an excel spreadsheet input. 

## Features

- Reads data from Excel.
- Performs linear regression.
- Generates plot with line of best fit.
- Displays regression details (slope, intercept, R², errors).
- Saves the plot as a png.

## Requirements

- numpy
- pandas
- matplotlib
- statsmodels

## Usage

1. Prepare Excel file with the following columns:
   - **x**: x axis values.
   - **y**: y axis values.
   - **xerr**: x error values (optional).
   - **yerr**: y error values (optional).

2. Edit script to specify your file and column names.

3. Run script to generate the regression plot.

## MIT License
