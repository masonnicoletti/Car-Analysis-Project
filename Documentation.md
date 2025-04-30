# Documentation

### Selecting the Data


### EDA
The goal of conducting EDA was to visualize some of the important variables in the data and figure out the best ways to clean up the USA_cars_dataset in order to build predictive models for it. 
- We started by analyzing the distribution of car prices in the dataset. As one would expect, the prices are skewed to the right. The average price is $18.8 k, but the majority of cars have a price lower than this. 
- Looking at mileage, this variable was also significantly skewed to the right. In order to normalize this distribution, we dropped outliers of cars that had some extremely high mileage
- Taking a look at the geography variables, nearly all of the cars are from the USA - although there is an uneven representation across the 50 states. We used a map to identify all the locations of cars throughout the country.
- Nearly 30 different car brands are represented in this data. The majority of these vehicles are Ford by far. There is also a decent representation of Dodge, Nissan, and Chevrolet.
- The distribution of these cars' manufacturing year is heavily skewed to the left. The majority of the vehicles are made in 2016-2020 (2020 is the likely the year the data was collected). There are some strong outliers in the 1970s, 1990s, and 2000s. For a more even distribution, it is best to drop the vehicles before 2010.
- There are alo a variety of colors for vehicles in the data. The most prevalent colors are white, black, gray, silver, blue, and red. It is useful to group all the other colors into a category called 'other'.
- The condition variable is a string indicating the amount of time a car has left - with some of these values being in minutes, hours, and days. It is unclear to what this is referring to.
- Other variables that are not useful include vin, lot, and title-status.
- Looking specifically at Ford entries, 
- We determined it is valuable to focus on Ford cars because this brand has by far the most data out of the other makes. F-150 is the most frequent Ford model in the data. There are also hundreds of entries with a model called 'door' and 'doors'. We are uncertain what this model means, so we will drop these rows from the data.



### Research Question



### Data Cleaning Function


### Decision Tree


### Linear Regression


### Polynomial Regression


### Findings