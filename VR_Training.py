# Import all the packages needed for analysis 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

# Load in the data 
df = pd.read_csv("20231215_DG18_training1.csv", header = 0)

# Explore the shape and structure of the data 
print("Shape of the VRbehaviour dataset:", df.shape)
print("First 5 rows of the VRbehaviour dataset", df.head())
print(df.columns)

# Determine whether this is reward training trial: Check if the value in the "reward" column ever equals 1
reward_given = any(df['Reward'] == 1)
if reward_given:
    print("This animal is trained with reward")
else:
    print("This animal is trained without reward")

# Check the position of the mouse in VR looks correct across time and that the reward is delivered reliably 
sns.set(style="whitegrid")

plt.figure(figsize=(20, 6))
sns.lineplot(x='Time', y='Position', data=df, label='Position')

sns.scatterplot(x='Time', y='Position', data=df[df['Reward'] == 1], color='red', label='Reward == 1')

#Time is restricted to 1000-2000 for better visualisation, remove line 30 to view whole experiment
plt.xlim(1000, 2000)
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()

plt.show()

# Calculate parameters to determine this animals level of training and experiment suitablity 

# 1. Calculate the number of laps run by this animal and add a column indicating which lap each data point is from

# Find all the index values when position = min 
position_min = df['Position'].min()

# Setting up variables to identify lap ending, count the number of laps and create a list which will contain the lap number for each position value 
lap_end = 0
lap_counter = 0
lap_list = []

# For loop cycles through position values and is set to 1 once the animal passes the reward (lap complete), then set to 0 when animal is teleported to start position.   
for index, position in enumerate(df["Position"]):
    if position > 870: # lap considered run when reward is given (always before position 870) 
        lap_end = 1        
    if position == position_min and lap_end == 1:
        lap_end = 0
        lap_counter+=1
    lap_list.append(lap_counter) # Add the lap number to the list 

# Add a column to label rows as belonging to a specific lap
df['Lap'] = lap_list

# Print total laps run by the animal and categorises animal by total laps run 
print(f"Total laps run: {lap_counter}")
if lap_counter > 100:
    print("Laps run: High")
elif lap_counter > 50:
    print("Laps run: Moderate")
else:
    print("Laps run: Low")

# 2. Quantify how well the animals licking is correlated with reward delivery, indicating it has learnt the reward location 

# Calculate the percentage of licks per lap that fall within the reward prediction zone (3s pre- and 1s post-reward delivery) 

# Variables and dict
count_lick_inside_range = 0
count_total_licks = 0

percentage_dict = {}

# For loop to create a dataframes for each unique values of lap 
for lap in df['Lap'].unique():
    # Filter data for the current lap
    lap_data = df[df['Lap'] == lap]

    # Initialize counters for each lap
    count_lick_inside_range = 0
    count_total_licks = len(lap_data) 

    # For each row in a single lap dataframe extract the position and lick values
    for index, row in lap_data.iterrows():
        position = row['Position']
        lick = row['Licks']

        # Check the conditions and update counts
        if 765 <= position <= 885 and lick == True:
            count_lick_inside_range += 1

    # Calculate the percentage of licks in the reward prediction zone 
    percentage_inside_range = (count_lick_inside_range / count_total_licks) * 100

    # Store the percentage in the dictionary
    percentage_dict[lap] = percentage_inside_range

# Convert the dictionary to a DataFrame to plot
percentage_df = pd.DataFrame(list(percentage_dict.items()), columns=['Lap', 'Percentage'])

# Plot the percentage of licks inside the range for each lap
plt.figure(figsize=(10, 6))
plt.bar(percentage_df['Lap'], percentage_df['Percentage'], color='blue', alpha=0.7)
plt.xlabel('Lap Number')
plt.ylabel('Percentage of Licks in reward prediction zone')
plt.title('Percentage of Licks in Reward prediction zone for Each Lap')

plt.show()
