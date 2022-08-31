# sqlalchemy-challenge

# Climate_Starter

# Opening the Project

Please open Climate_Starter.ipynb in jupyter notebook. To run the code you must also have the hawaii.sqlite file downloaded in the Resources folder.

# Reflect Tables into SQLAlchemy ORM

First I import all of the necessary sqlalchemy packages and create an engine to the hawaii.sqlite file. I reflect the database and its tables into a new model. I check to see the classes the automap found and then I create a reference for each table. Lastly I create a session link. 

# Exploratory Precipitation Analysis

For my measurement table I check to see the column name and data type for each column. I use a session query to find the most recent date and convert the list to a string and then to date time format. Using my date I find the date from a year ago, taking care to account for the leap year. I then perform a session query to find all of the precipitation data and the dates up to one year ago. I convert my result into a dataframe and sort by ascending date. I also drop any NaN values in the precipitation column. I plot the dataframe using a bar graph and generate a summary of statistics table. 

# Exploratory Station Analysis

For my station table I check the names and data types for each column. I perform a query to find the total number of stations and another query to find the most active station. From my previous query I extract the station id from the generated list and perform another query to find the min, max and average temperature recorded. I then perform a query to get the temperature data for the most active station within the past year. I convert this result into a dataframe. I plot my dataframe into a histograph that counts the frequency in which each temperature occurs. 

# Findings

The most active station within the last year has perfect weather for a vacation with the low of 55 degrees, a high of 85 degrees and an average of 71.66 degrees. I think it would be interesting to investigate the precipitation recorded at this station, so I can plan for rainy weather. I also think it will be interesting to look at a particular month(s) over the years to find the best time to vacation. 

# App.py

# Opening Project

In the gitbash terminal (or an alternative) set up the path to the sqlalchemy-challenge folder. You can also run your terminal from within the folder. In the terminal type "python app.py" to run the file. This will generate a link for you to copy and paste within your web browser. Please keep the terminal open while using the application. For the start and start/end routes, replace "start"/"end" with a date in the format of "YYYY-MM-DD". To apply a route copy and paste it at the end of the apps url (ex. (url)/api/v1.0/precipitation) I will explain what each route finds in the next session in order.

# First Route, Precipitation 

This route finds all of the precipitation data across all dates. 

# Second Route, Stations

This route finds all of the station ids, name, elevation, latitude, and longitude.

# Third Route, tobs

This route finds all of the temperature observations within the past year from the most active station. 

# Fourth Route, start

This route finds the minimum, maximum and average temperature from the starting date to the most recent date. To use this route you must replace "start" with a date in this format "YYYY-MM-DD". 

# Fifth Route, start/end

This route finds the minimum, maximum and average temperature from the starting date to an ending date. To use this route you must replace "start" and "end" with a date in this format "YYYY-MM-DD". 

# BONUS

# Temperature Analysis Bonus 1

# Opening Project

Please open temp_analysis_bonus_1_starter.ipynb in jupyter notebook. Please make sure to have the hawaii_measurements.csv file downloaded in the resources folder. 

# Setting up data

First I import the hawaii_measurements.csv file into my code. I change the date column's data type from a string to date time. I set the date as my index and drop any rows with NaN values. The starter asks me to drop the date column, but I get an error due to the fact that my date column is an index now. I have commented this out in my code.

# Compare June and December Data

I filter my data frame to get data from June and December across all years. I check to make sure my data was filtered correctly. I find the average temperature for June and December. I create collections of data by creating a variable that only shows the tobs for each month and then use the describe method to look at a statistical over view for both months. 

# Analysis

Lastly I perform a paired t-test because the months are independent. Since I am comparing average temperatures, my null hypothesis is the means are the same, which means my alternate hypothesis is that the means are different. I found that my p-value for this test was near zero and well below a 5% significance level. I am able to reject my null hypothesis which means that the temperatures for June and December are significantly different. 

# Temperature Analysis Bonus 2

# Opening the Project

Please open temp_analysis_bonus_2.ipynb in jupyter notebook. To run the code you must also have the hawaii.sqlite file downloaded in the Resources folder.

# Reflect Tables into SQLAlchemy ORM

First I import all of the necessary sqlalchemy packages and create an engine to the hawaii.sqlite file. I reflect the database and its tables into a new model. I check to see the classes the automap found and then I create a reference for each table. Lastly I create a session link. 

# Bonus Challenge Assignment
Using the provided formula I find the min, avg and max temps for a year within our data set. From my tuple I select the indexes that have the min, avg and max temps for the year. I subtract the min temp from the max temp to get my peak-to-peak value that I will use for the yerr for my bar chart. I plot the average temperature for my trip in a bar chart.

# Daily Rainfall Average
I perform a query that finds the station id, station name, total amount of precipitation, station latitude, longitude and elevation. I filter my query results by dates ranging from 2011-02-28 and 2011-03-05 and when the station id column match for each table. I group by station id column and order by descending precipitation. I put the result into a data frame for ease of reading. 

# Daily Temperature Normals
I first convert the start and end dates of my trip to the date time format. I then create an empty list for the normal temperatures and another for the dates. I create a while loop that loops through my trip dates and I use the provided function to find the min,avg and max temps for a given day. I append my empty lists for each iteration. With my result I convert it into a data frame. Lastly I create an area plot so I can visually process the temperatures for my trip. 

# Findings
In my opinion, I found that the potential weather for my trip will be quite pleasant. By Texas standards, it isn't too hot. There doesn't seem to be too much rain usually, so I can spend my days having fun in the sun! Now the only thing left to do is to buy my ticket!

