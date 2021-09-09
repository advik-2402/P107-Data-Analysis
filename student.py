import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("p107/studentData.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(data_frame = mean, x="student_id", y="level", size="attempt", color="attempt")

fig.show()
