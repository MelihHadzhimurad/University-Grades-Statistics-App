import pandas
import data_processing
import matplotlib.pyplot as plot

data_frame = data_processing.get_data_in_frame()

print(data_frame)
print()

# Average grade for each year
print(data_frame.groupby("Year")["Grade"].mean())
print()

# Average grade for each semester
print(data_frame.groupby("Semester")["Grade"].mean())
print()

# number of each grade as the student has
print()
print("Twos:\t" + str(data_frame[data_frame["Grade"] == 2]["Subject"].count()))
print("Threes:\t" + str(data_frame[data_frame["Grade"] == 3]["Subject"].count()))
print("Fours:\t" + str(data_frame[data_frame["Grade"] == 4]["Subject"].count()))
print("Fives:\t" + str(data_frame[data_frame["Grade"] == 5]["Subject"].count()))
print("Sixes:\t" + str(data_frame[data_frame["Grade"] == 6]["Subject"].count()))

# the last grade for each subject(if all grades are 2, take last, else take last grade different from 2)
# half implemented, must be finished!
"""
subjects_frame = pandas.DataFrame({"Subjects": data_frame["Subject"]})

print(data_frame[(data_frame["Subject"].duplicated().equals(False)) or (data_frame["Grade"] != 2)])
"""

# Grade that appears the most
print()
print("Most appeared grade:\t", data_frame["Grade"].mode())
