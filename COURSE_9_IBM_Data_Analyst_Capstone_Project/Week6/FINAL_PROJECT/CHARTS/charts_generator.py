import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Build first bar chart with Job Postings per City

df = pd.read_excel("../../../Week1/LAB2/job-postings.xlsx").set_index("Location")
df = df.sort_values("Number of Jobs", ascending=False).reset_index()

#df.plot(kind="bar")
my_plot = sns.barplot(df, x="Location", y="Number of Jobs")
my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=-30)
plt.title("Job postings per city")
plt.show()
#plt.savefig("fig1.png")

# Build second bar chart with Programming Languages by salary

df = pd.read_csv("../../../Week1/LAB4/popular-languages.csv").set_index("Language")
df
df = df.sort_values("Average Annual Salary", ascending=False).reset_index()

print(df)