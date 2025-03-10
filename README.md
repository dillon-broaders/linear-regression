# Simple linear regression program

This Python program reads data from an Excel file, performs linear regression, and generates a plot with the line of best fit. It also calculates the slope, 
intercept, R² value, and their respective errors. It displays this regression information plus any error bars for both x and y values.

## Motivation

During my undergraduate labs, MacOS users couldn't use Origin for data analysis. At the time, this software could only be used on Windows. Hence, I created this 
program to quickly generate regression plots and display results.

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
   - **xerr**: x error values.
   - **yerr**: y error values.

2. Edit script to specify your file and column names.

3. Run script to generate the regression plot.
