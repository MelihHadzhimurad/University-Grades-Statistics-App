import pandas

import data_processing
import matplotlib.pyplot as plot

data_frame = data_processing.get_data_in_frame()

# Average grade for each year
# print(data_frame.groupby("Year")["Grade"].mean())

# Average grade for each semester
# print(data_frame.groupby("Semester")["Grade"].mean())

# number of each grade as the student has
"""
print("Twos: \n" + str(data_frame[data_frame["Grade"] == 2]["Subject"].count()))
print("Threes: \n" + str(data_frame[data_frame["Grade"] == 3]["Subject"].count()))
print("Fours: \n" + str(data_frame[data_frame["Grade"] == 4]["Subject"].count()))
print("Fives: \n" + str(data_frame[data_frame["Grade"] == 5]["Subject"].count()))
print("Sixes: \n" + str(data_frame[data_frame["Grade"] == 6]["Subject"].count()))
"""

subjects_frame = pandas.DataFrame({"Subjects": data_frame["Subject"]})

print(data_frame[(data_frame["Subject"].duplicated().equals(False)) or (data_frame["Grade"] != 2)])
