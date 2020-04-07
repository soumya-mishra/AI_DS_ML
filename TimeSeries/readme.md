Time Series
----------------------------------------------
Time series is a sequence of observation in equi-spaced  time intervals
Order and continuity should be mintained.
Time series Modelling technique:-
----------------------------------
1.	Auto Regression(AR)
2.	Moving Average(MA)
3.	Auto regressive moving average(ARMA)
4.	Auto regressive integrated  moving average(ARIMA)
5.	Seasonal Autoregressive Integrated Moving-Average (SARIMA)
6.	Seasonal Autoregressive Integrated Moving-Average with Exogenous              Regressors (SARIMAX)
7.	Vector Auto regressor(VAR)
8.	Vector Auto regressor moving average(VAM)
9.	Vector Auto regressor moving average with exogenous Regressor(VARMAX
10.	Simple exponetial smoothing(SES)
11.	Holt winter's exponenetial smoothing(HWES)
 
AR:-
For AR(1) model
  
MA:-
Linear function of residula error.
Useful for univariate time seriese.
  
Above - q order is 1 , p order is 0. ARMA converted to MA.
 
ARMA:-
The Autoregressive Moving Average (ARMA) method models the next step in the sequence as a linear function of the observations and resiudal errors at prior time steps.
  
combines both Autoregression (AR) and Moving Average (MA)
 
model involves specifying the order for the AR(p) and MA(q) models as parameters to an ARMA function, e.g. ARMA(p, q). An ARIMA model can be used to develop AR or MA models.
 
ARIMA:-
 
model involves specifying the order for the AR(p), I(d), and MA(q) models as parameters to an ARIMA function, e.g. ARIMA(p, d, q). An ARIMA model can also be used to develop AR, MA, and ARMA models.
suitable for univariate time series with trend and without seasonal components
 
 
SARIMA :-
 
Sarima models the next step in the sequence as a linear function of 
-different observation
-errors 
-Different seaosonal observation
-Seasonal errors
SARIMA(p, d, q)(P, D, Q)m where 'm' is the number of time steps in each season (the seasonal period)
 
suitable for univariate time series with trend and/or seasonal components.
 
 
SARIMAX:-
Exogeneous variable-  exogenous variable is one whose value is determined outside the model and is imposed on the model.
 
VAR:-
The method is suitable for multivariate time series without trend and seasonal components.
 
 
Vector Autoregression Moving-Average (VARMA)
multivariate time series
 
method is suitable for multivariate time series without trend and seasonal components
 
VARMAX:-
 
The method is suitable for multivariate time series without trend and seasonal components with exogenous variables.
 
 
Simple Exponential Smoothing (SES):-
 
exponentially weighted linear function of observations at prior time steps.
 
 
Holt Winter’s Exponential Smoothing (HWES):-
exponentially weighted linear function of observations at prior time steps
 
Stationary data: - mean, variance remain constant over time
Means the entire distribution of data is same at particular point.
ARIMA, AR, MA etc are depends on stationary data to build model
These models assumes the data you are supplying are stationary data.
Trending data  | seasonal data , they are not stationary.

Check stationary data: - 
1.Plot Rolling statistics

Handle Time data:- 
  
Datetimeindex:
  
When we convert the data into datetime index, it has many benefit.
 
Average passenger on year 2017 . If we do not convert it into datetimeindex it throws error.
 
 
 
 
 
 
Assign Date range in CSV file where there is no date:-
 
 
 
Provide start date, end date, freq = Business days(B), we need stock price, stock exchage is off on weekends.
 
Make the data with date index.
 
 
Also we can use asfreq method to insert date all days. Includign weekend.
 
 
 
hourly
 
 
Weekly  - 'W'
 
If I do not know end date, I can specify the periods.
 
For US holiday calenders,
 
 
 
 
 
 
Date time can be many form
 
 
To_datetime:-
 
 
 
 
 
 
 
Errors = 'ignore'  ignores the error in date conversion
 
 
 
 
 
 
 
 
 
 
 
 
Ffill and bfill to fill the NaN  with last value.


Resampling: down and upsampling :
 
Expanding and rolling window concept
 

Time series decomposition:
Level: The average value in the series.
Trend: The increasing or decreasing value in the series.
Seasonality: The repeating short-term cycle in the series.
Noise: The random variation in the series.

These are the components of a time series
* Trend - Consistent upwards or downwards slope of a time series
* Seasonality - Clear periodic pattern of a time series(like sine funtion)
* Noise - Outliers or missing values
we want to decompose the time series into abobve three to see the trend, seaosnality and Noise.
** Additive and Multiplicative model decomposition
import seasonal_decompose from stats model
apply seasonal decompose to log transformed time series.
plot the trend | seasonality and residual
 
Additive : this additive as the amplitude is not changing much.
 
Multiplicative:
 
 
 
 
 
 
 
