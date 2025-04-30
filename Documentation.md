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
After deciding to focus on Ford vehicles, we crafted our research question:

**Can we build a model that accurately predicts the selling price of used Ford Vehicles?**


### Data Cleaning Function
The clean_car_data function takes a DataFrame of used car listings and performs a series of cleaning and transformation steps to prepare the data for analysis or modeling, based on many of the findings from EDA. It starts by removing unnamed or irrelevant columns and filters the data to include only Ford vehicles sold in the United States (excluding listings from Canada). The function standardizes U.S. state names to lowercase and maps them to their corresponding regions (Northeast, Midwest, South, or West), assigning 'other' to unmapped states. It then filters out records with missing or non-informative model names, restricts the data to vehicles from 2010 onward, and removes entries with mileage above 150,000. The car color values are simplified into a limited set of main colors, with all others grouped as 'other'. An age column is added, calculated as the difference between 2020 and the car's model year. Finally, all object-type columns are converted to categorical variables to improve memory efficiency and support downstream analysis. This function was imported into all the ML model files, and it consistently cleaned the data.

### Regression Trees


### Linear Regression
The next step in this process was to build a linear regression model. Unlike the Decision Tree Regressor, we had to do one-hot coding, creating dummy variables for all the categorical data. After standardizing the numerical data, separating the features and target variable, and partitioning the data into train/test sets, we instantiated a Linear Regression model. The intercept of this model is $36k, far greater than the average car price. As a result, the majority of the coefficients were negative, and they were pretty large values. The only positive coefficients were for the variables: `is-f150` (binary), `color_off-white`, and `region-Northeast`. After predicting on the test data, the R2 score was calculated to be 0.156, a slight improvement from the Decision Tree. The RMSE was 10,000 - a very large value considering the prices of the cars in the dataset. The plot of the predicted values vs the true values revealed a nonlinear distribution, possibly one that could be modeled better using polynomial regression.


### Polynomial Regression
The polynomial regression model process was similar to building a regression model. However, instead of regressing over the data once, we created a list of degrees, and looping through the list, fit many polynomial regression models over a range of degrees. The findings here were unfortunately not very useful again. The model worked best with two degrees, scoring a similar R2 score and RMSE as the linear regression model. However, as the number of degrees increased, the R2 score decreased exponentially (even going into large negative values), and the RMSE increased exponentially. These findings signal the the model is overfitting as the number of degrees is increased. This step unfortunately did not result in a model that improve the predictive power over Ford cars.


### Findings
Out of the three types of models implemented on the car data, all of them had very poor results. The greatest correlation was achieved with the linear regression model, although this R2 score of 0.16 is not indicative of any useful predictive power. We reason that the USA_cars_dataset offered too few useful features to effectively predict prices of cars. In the end, the majority of features in this data had to be collapsed or dropped altogether, giving little room for an effective model to be made.