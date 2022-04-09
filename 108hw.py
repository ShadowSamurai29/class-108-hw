import plotly.figure_factory as ff
import random
import pandas as pd

df = pd.read_csv("108 hw.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist = False)
fig.show()