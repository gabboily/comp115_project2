from pathlib import Path  
import csv                    # importing the modules I will be using
import numpy as np
import matplotlib.pyplot as plt

path = Path('easter_roadtrip_songs.csv')
lines = path.read_text().splitlines()        # open and parse the csv file 

reader = csv.reader(lines)
header_row = next(reader)
rows = list(reader)

def organize_variables(i):             # organize variables from csv file into lists
    res = []
    for row in rows:
        res.append(row[i])
    return res

time = organize_variables(0)
length = organize_variables(3)
genre = organize_variables(4)
position = organize_variables(5)

def group_counts(genres, times):                # convert lists into a dictionary where all values are linked
    count_dict = {}
    for g, t in zip(genres, times):
        if g not in count_dict:
            count_dict[g] = {}
        if t in count_dict[g]:
            count_dict[g][t] += 1
        else:
            count_dict[g][t] = 1
    return count_dict

counts = group_counts(genre,time)

genres = list(counts.keys())
x = np.arange(len(genres))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

time_options = set(time)

for c in time_options:
    vals = [counts[g].get(c, 0) for g in genres]             # format plot #1
    offset = width * multiplier
    rects = ax.bar(x + offset, vals, width, label=c)
    ax.bar_label(rects, padding=3)
    multiplier += 1

plt.style.use('seaborn-v0_8-bright')
ax.set_ylabel("Number of Songs Played")               # plot a grouped bar chart, showing how many types of songs were played during a 
ax.set_xlabel('Genre of Song')                        # certain time of day
ax.set_xticks(x + width)
ax.set_xticklabels(genres, rotation=45)
ax.set_ylim(0, 9)
ax.legend(loc='upper right', ncols=3)
ax.set_title("Style of Songs Played by Time of Day")

plt.savefig('project2_plot1.png')

length = list(map(int, length))
position = list(map(int, position))

fig1, ax1 = plt.subplots()

plt.style.use('seaborn-v0_8-bright')                            # plot #2: a scatter plot showing songs' highest charting value as a function
ax1.scatter(length, position, s=10, color='blue')               # of song length
ax1.set_xlabel("Length of Song (seconds)")
ax1.set_ylabel("Top Chart Position")
ax1.set_title("Top Chart Position Plotted by Length of Song")
ax1.invert_yaxis()
ax1.set_xlim(min(length) -10, max(length) + 10)
ax1.set_ylim(max(position) + 5, min(position) - 5)

plt.savefig('project2_plot2.png')
plt.show()