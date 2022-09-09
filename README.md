# Brazil 2020 COVID-19 Analysis: Project Overview

- This notebook is part of Alura's courses [Análise de série temporal: COVID-19 (Time series analysis: COVID-19)]((https://cursos.alura.com.br/course/analise-serie-temporal-covid-19)) and [Previsões de série temporal: COVID-19 (Time series predictions: COVID-19)](https://cursos.alura.com.br/course/previsoes-serie-temporal-covid-19) by Sara Malvar.
- Created a time series analysis of COVID-19 in Brazil 2020. 
- Performed features scaling.
- Label encoded target variable.

## Code and resources

Platform: Google Colab

Python version: 3.7.6

Packages: datetime, itertools, os, matplotlib, pandas, numpy, seaborn and sklearn

## Data set

The dataset contains information about COVID-19 numbers from late February until late July. The records were gathered and compiled by a consortium of main Brazilian press vehicles using their methodology due to the lack of trust in numbers delivered by Brazil's Ministry of Health. That's why we have two different columns for the number of cases and mortality.

Its feature are: semana (epidemiological week), data (date), pais (country), estado (state), cidade (city), novosObitos (new deaths), Obitos (deaths), novosCasos (new cases), Casos (cases), obitosMs (death count by Ministry of Health), casosMS (cases count by Ministry of Health), obitos_por_100k (death per 100k), casos_por_100k (cases per 100k), obitos_por_casos (death by the number of cases), recuperados (recovered), suspeitos (suspicious cases), testes (COVID tests made), testes_por_100k (COVID tests made per 100k).

## Data cleaning

I created the following features:
- aceleracao_casos (cases growth rate)
- aceleracao_obitos (mortality growth rate)
- media_movel_mortes_7_dias (7-day moving average)
- media_movel_mortes_14_dias (14-day moving average)

I checked: 
- the data types and needed to convert the Date column into date type.
- null values and there were several of them due to data compilation methodology.
- size and the data set's main statistics.

I looked at the mortality rate in all states and decided to continue the exploration using São Paulo state data only since it has the largest population in the whole country. Plus, it detected new deaths exponential growth rate, and seven-day seasonality. I also used autocorrelation and partial autocorrelation to confirm how long the mortality and number of cases were correlated to each and these analyses were useful in the model.

## Model building

First, I decompose the time series using **seasonal_decompose** with a 7-day frequency. Using ADF (Augmented Dickey-Fuller) test to confirm that the time series was not stationary and then I used differencing to transform the data into a stationary one.

I used ARIMA and SARIMA models to predict the following 30 days of mortality and the number of cases.

## Model performance

The best SARIMA model for the number of cases had an AIC (Akaike Information Criteria) of 2750 for (1,1,1,7) parameters setup.

For the mortality predictions, the model achieved an AIC of 3462 for (0,1,1,7) setup.

The model did well to forecast the following 30 days' number of cases and mortality. After that, the model's performance was decreasing.



