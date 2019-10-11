import pandas as pd
import matplotlib.pyplot as plt 

#Read city_data file
city_data = pd.read_csv("city_data.csv")
#Read city_list file
city_list = pd.read_csv("city_list.csv")
#Read global_data file
global_data = pd.read_csv("global_data.csv")

#Extract my nearest city (New York City) into nyc_data
nyc_data = city_data[city_data.city == "New York"]

#Extract data for a very far city (Sydney) into sydney_data
sydney_data = city_data[city_data.city == "Sydney"]
#Elimainate cells with no data
nyc_data_complete = nyc_data.dropna()

#Create new column within each data set and
#calculate the moving average for both NYC and Global data over a 10 year period

#for movingavg, row in nyc_data_complete.iterrows() :
#	nyc_data_complete.loc[movingavg, "nyc_moving_avg"] = nyc_data_complete["avg_temp"].rolling(window=10).mean()
#print(monthly)

nyc_data_complete["nyc_moving_avg"] = nyc_data_complete["avg_temp"].rolling(window=10).mean()
sydney_data["sydney_moving_avg"] = sydney_data["avg_temp"].rolling(window=10).mean()
global_data["global_moving_avg"] = global_data["avg_temp"].rolling(window=10).mean()

#Plot both NYC and Global data on the same plot
ax = nyc_data_complete.plot(x="year", y="nyc_moving_avg", label ="NYC Data")
global_data.plot(x="year", y="global_moving_avg", label ="Global Data", ax=ax)
sydney_data.plot(x="year", y="sydney_moving_avg", label ="Sydney Data", ax=ax)

#y-axis label
ax.set_ylabel("Average Temperature (Degrees Celsius)")
#Plot Title
plt.title("Plot of NYC Ave_Temp vs. Global City Ave_Temp")
#Generate Chart
plt.show()

# Difference in mean between NYC and Gloabl Temps
nyc_temps = sydney_data["sydney_moving_avg"]
global_temps = nyc_data_complete["nyc_moving_avg"]
mean_diff = nyc_temps.mean() - global_temps.mean()
print(nyc_temps.mean())
print(global_temps.mean())
print(mean_diff)