import pandas
import data_processing
import matplotlib.pyplot as plt
from scipy import stats
import seaborn.objects as graphic_presenter

data_frame = data_processing.get_data_in_frame()

# Average grade for each semester
print(data_frame.groupby("Semester")["Grade"].mean())

grade_by_years = pandas.DataFrame(data_frame.groupby("Semester")["Grade"].mean())

(
    graphic_presenter.Plot(grade_by_years, x="Semester", y="Grade")
    .add(graphic_presenter.Dots())
    .add(graphic_presenter.Line())
).show()

# Average grade for each year
# print(data_frame.groupby("Year")["Grade"].mean())

# number of each grade as the student has
"""
print("Twos: \n" + str(data_frame[data_frame["Grade"] == 2]["Subject"].count()))
print("Threes: \n" + str(data_frame[data_frame["Grade"] == 3]["Subject"].count()))
print("Fours: \n" + str(data_frame[data_frame["Grade"] == 4]["Subject"].count()))
print("Fives: \n" + str(data_frame[data_frame["Grade"] == 5]["Subject"].count()))
print("Sixes: \n" + str(data_frame[data_frame["Grade"] == 6]["Subject"].count()))
"""

# the last grade for each subject(if all grades are 2, take last, else take last grade different from 2)
# half implemented, must be finished!
"""
subjects_frame = pandas.DataFrame({"Subjects": data_frame["Subject"]})

print(data_frame[(data_frame["Subject"].duplicated().equals(False)) or (data_frame["Grade"] != 2)])
"""

# Grade that appears the most
# print(stats.mode(data_frame["Grade"]))

# print(data_frame.describe())
