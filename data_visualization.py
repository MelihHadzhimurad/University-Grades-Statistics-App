import pandas
import data_processing
import matplotlib.pyplot as plt
from scipy import stats
import seaborn.objects as graphic_presenter
import seaborn as sbrn

data_frame = data_processing.get_data_in_frame()

# Average grade for each semester -- add styling!!!
"""
print(data_frame.groupby("Semester")["Grade"].mean())

grade_by_years = pandas.DataFrame(data_frame.groupby("Semester")["Grade"].mean())

(
    graphic_presenter.Plot(grade_by_years, x="Semester", y="Grade")
    .add(graphic_presenter.Dots())
    .add(graphic_presenter.Line())
).show()
"""

# Average grade for each year
"""
print(data_frame.groupby("Year")["Grade"].mean())

grade_by_years = pandas.DataFrame(data_frame.groupby("Year")["Grade"].mean())

(
    graphic_presenter.Plot(grade_by_years, x="Year", y="Grade")
    .add(graphic_presenter.Dots())
    .add(graphic_presenter.Line())
).show()
"""

# number of each grade as the student has

grades = []
counts = []

for index in range(1, 7, 1):
    count = data_frame[data_frame["Grade"] == index]["Subject"].count()

    if count != 0:
        grades.append(index)
        counts.append(count)

plt.pie(counts, labels=grades, autopct='%1.1f%%', startangle=140)
plt.legend(counts, title="Grade - count", loc="center right", bbox_to_anchor=(0.8, 0, 0.5, 1))
plt.show()

# the last grade for each subject(if all grades are 2, take last, else, take last grade different from 2)
# half implemented, must be finished!
"""
subjects_frame = pandas.DataFrame({"Subjects": data_frame["Subject"]})

print(data_frame[(data_frame["Subject"].duplicated().equals(False)) or (data_frame["Grade"] != 2)])
"""

# Grade that appears the most
# print(stats.mode(data_frame["Grade"]))

# print(data_frame.describe())
