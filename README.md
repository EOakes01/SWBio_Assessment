# Spatial navigation in VR: training session analysis 
This is a pipeline written in python to process the raw behavioural readouts from a mouse linear track virtual reality training session in order to assertain the level of training and whether the animal is suitable for experiments (completing enough laps). The experimental set up is displayed below: 

![image](https://github.com/EOakes01/SWBio_Assessment/assets/146095262/cde57654-442c-4a7a-805d-6d177c9d40a3)

## The code:
The pipeline outputs the shape and structure of the data and identifies whether the animal was trained with or without reward. It also analyses the suitability of the animal for further experiments by assessing the number of laps run, and gives an indication of the level of training by quantifying whether the animal is anticipating the reward- an idication that the animal has internally mapped the virtual environment. 

This script could be modified for different virtual reality or freely moving tracks provided position remains a continuous variable.

## To run: 
1. Download the python script in this repository into the same directory as the data csv file (provided for assessment via Blackboard) 
2. Ensure the seaborn (https://seaborn.pydata.org/installing.html), numpy (https://numpy.org/install/), matplotlib (https://matplotlib.org/stable/) and pandas (https://pandas.pydata.org/) libraries are all installed
3. Column headers in the code are 'Time', 'Licks', 'Reward', 'Velocity' and 'Position'. Please alter these to fit your dataset if needed
4. Be aware that the position threshold for end of lap is defined as position 870, this can be altered in the code to suit different VR or freely moving tracks. All other positions are defined using max and min.
5. The thresholds to define lap rate can also be altered, the definitions of 'high', 'moderate' and 'low' lap rate were defined using previous training cohort data.

## Results and conclusions 
The analysis of the sample dataset revealed that this mouse has a high lap rate and is therefore likely to be suitable for future experiments. A high lap rate is neccessary to perform the spatial navigation tasks in our experimental paradigm. 
This mouse also indicated a relatively low level of training with the percentage of licks in the reward prediction zone (3s before and 1s after reward) for all laps  <12% of the total licks. The interpretation of this output is currently limited as we have not monitored this on previous cohorts. We intend to monitor this metric accross the full training and experiment schedule in order to didentify a threshold where we can define training as complete. 
