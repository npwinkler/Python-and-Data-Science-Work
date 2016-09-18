Given a train set and a test set from the UCI Housing Data Set, my task was to train a predictive model on the train set  for "MEDV: Median value of owner-occupied homes in $1000's" so as to minimize the root mean square error on the test set. 

After 3 hours of my work,

What I tried, in short: linear regression on most important variables (room, distance, lower status %) and decision tree regression with the same variables plus ones which split the data into categories (crime, blacks, radius, tax).

How models perform, in short: The latter model seemed to work very well (perhaps too well). The first model was not that great, despite seeming like these were really the three variables that mattered the most.

My impression is that the number of rooms is the most predictive, with the lower status % and distance variables also being important.

My process:

The data was very clean, so I did not have to do any replacements. After looking at the data for a while (mostly scatterplots of MEDV vs. another variable), I found that RM and DIS seemed to be in linear relationships with MEDV while LSTAT was in more of a logistic relationship with it. As such, I wanted to see how well a simple linear regression of those last 3 variables predicting MEDV would perform, which I did after standardizing the data; I got a high RMSE based off of this. So, I decided I would account for how there seemed to be some amount of different categories of houses based on thresholds for crime, blacks, tax values, and radius. For example, it seemed like there was a split between houses with low-medium amounts of crime comprising one sample and houses in high crime areas (>25 per capital crime rate) comprising another. Thus, I decided that a decision tree would be good because it could split up the data based on these thresholds. This performed a lot better.

 I would have liked to also account for the logistic nature of the MEDV and LSTAT relationship more, but did not have time. Similarly, if I had more time and was more proficient in these libraries as opposed to R, I would like to have split the test data into test and validation and been able to run some actual model evaluation. Hopefully, I will pick up the proficiency to work with these libraries a lot faster and more confidently as time goes on :)

