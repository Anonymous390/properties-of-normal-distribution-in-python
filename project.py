import plotly.express as px
import pandas as pd
from statistics import *

df = pd.read_csv("StudentsPerformance.csv")

data = df["math score"]

pop_mean = sum(data)/len(data)
pop_median = median(data)
pop_mode = mode(data)
standard_deviation = stdev(data)

print(pop_mean)
print(pop_median)
print(pop_mode)
print(standard_deviation)

stdev1_start, stdev1_end = pop_mean-standard_deviation, pop_mean+standard_deviation
stdev2_start, stdev2_end = pop_mean-(2*standard_deviation), pop_mean+(2*standard_deviation)
stdev3_start, stdev3_end = pop_mean-(3*standard_deviation), pop_mean+(3*standard_deviation)

counter = 0
counter2 = 0
counter3 = 0

for i in data:
	if i > stdev1_start and i < stdev1_end:
		counter+=1
		percentage = counter/len(data)*100
	if i > stdev2_start and i < stdev2_end:
		counter2+=1
		percentage2 = counter2/len(data)*100
	if i > stdev3_start and i < stdev3_end:
		counter3+=1
		percentage3 = counter3/len(data)*100

print(percentage, percentage2, percentage3)
