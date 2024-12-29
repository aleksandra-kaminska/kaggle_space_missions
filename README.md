# Linear Regression
Results for space mission data
 
## OLS Regression Results

| Dep. Variable:                  | Mission_Success_percent  | R-squared:                | 0.726 |
|----------------------------------|--------------------------|---------------------------|-------|
| Model:                           | OLS                      | Adj. R-squared:           | 0.718 |
| Method:                          | Least Squares            | F-statistic:              | 91.76 |
| Date:                            | Sun, 29 Dec 2024         | Prob (F-statistic):       | 2.19e-126 |
| Time:                            | 17:17:06                 | Log-Likelihood:           | -1505.3 |
| No. Observations:                | 500                      | AIC:                      | 3041  |
| Df Residuals:                    | 485                      | BIC:                      | 3104  |
| Df Model:                        | 14                       | Covariance Type:          | nonrobust |




### Coefficients

|

| Variable                           | coef     | std err  | t        | P>|t| |  0.025  |  0.975 |
|------------------------------------|----------|----------|----------|-------|---------|--------|
| Intercept                          | 76.5233  | 1.329    | 57.588   | 0.000 | 73.912  | 79.134 |
| Target_Type[T.Exoplanet]           | 0.1657   | 0.738    | 0.224    | 0.823 | -1.285  | 1.616  |
| Target_Type[T.Moon]                | -0.4404  | 0.739    | -0.596   | 0.551 | -1.891  | 1.011  |
| Target_Type[T.Planet]              | -0.3147  | 0.716    | -0.439   | 0.661 | -1.722  | 1.093  |
| Target_Type[T.Star]                | 0.0015   | 0.707    | 0.002    | 0.998 | -1.388  | 1.391  |
| Mission_Type[T.Exploration]        | -0.3811  | 0.634    | -0.601   | 0.548 | -1.626  | 0.864  |
| Mission_Type[T.Mining]             | -0.6535  | 0.658    | -0.994   | 0.321 | -1.946  | 0.639  |
| Mission_Type[T.Research]           | -1.1437  | 0.628    | -1.820   | 0.069 | -2.378  | 0.091  |
| Distance_from_Earth_light_years    | -0.7127  | 0.458    | -1.557   | 0.120 | -1.612  | 0.187  |
| Mission_Duration_years             | 0.1088   | 0.194    | 0.562    | 0.574 | -0.272  | 0.489  |
| Crew_Size                          | 0.0015   | 0.008    | 0.180    | 0.857 | -0.015  | 0.017  |
| Mission_Cost_billion_USD           | 0.0697   | 0.016    | 4.423    | 0.000 | 0.039   | 0.101  |
| Fuel_Consumption_tons              | 0.0066   | 0.004    | 1.473    | 0.142 | -0.002  | 0.015  |
| Payload_Weight_tons                | -0.0666  | 0.079    | -0.845   | 0.399 | -0.222  | 0.088  |
| Scientific_Yield_points            | 0.0068   | 0.008    | 0.801    | 0.424 | -0.010  | 0.023  |


### Diagnostics

| Omnibus                         | 1.696 | Durbin-Watson:   | 1.907 |
|----------------------------------|-------|------------------|-------|
| Prob(Omnibus):                  | 0.428 | Jarque-Bera (JB): | 1.545 |
| Skew:                           | -0.007| Prob(JB):         | 0.462 |
| Kurtosis:                       | 2.728 | Cond. No.         | 2.03e+04 |

**Notes:**
1. Standard Errors assume that the covariance matrix of the errors is correctly specified.
2. The condition number is large, 2.03e+04. This might indicate that there are strong multicollinearity or other numerical problems.

