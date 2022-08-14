# gus-stats

This is the progam which scraps data from polish statistic office database (gus gui bdl - https://bdl.stat.gov.pl/bdl/start)
and show the results in python table and chart.

To run the program clone the repository and run the command: python project-gus.py

What it does every step:
1. Use gus API to request data with GET method. Save the file in json format. - with reqest method
2. Loads the json, retrives essential data and puts it into pandas data frame. - using json and pandas library
3. Pivots the table and print it in python console.
4. Generates line chart of combine data for all the regions. - with matplotlib pyplot
