# comp115_project2

For project 2, I decided to learn some data visualization in an attempt to show patterns in my music streaming throughout a day of driving. 

In order to collect the data used for this project, I went to stat.fm, linked my Spotify account and chose a day to log what songs I listened to. Then, I created a CSV file, compiling the data into the following columns: Time, Artist, Title, Length, Genre, Top Position (see easter_roadtrip_songs.csv file).

Once the data was compiled, I began to read and parse the data in VSCode. Then, I coded two separate plots, using MatPlotLib. In the first graph (see project2_plot1.png), I aimed to show how the selection of music changed throughout the day changed, by showing the number of songs played from separate genres, further separated into the time of day the song was played.

In my second graph (see project2_plot2.png), with the help of https://www.officialcharts.com/ I aimed to see how the length of each song played, compared to its highest ranking on the charts. If a song had never had a position on the charts, I gave it the value 0.

Throughout my code, I have added comments to explain what a particular block of code means.

I hope you enjoy my project! Hopefully in the future, I can tweak this code in order to add more values and make my graphs more meaningful and descriptive.
