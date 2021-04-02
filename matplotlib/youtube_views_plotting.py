from googleapiclient.discovery import build
from time import sleep
# from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
from matplotlib import dates as mpl_dates

api_key = 'AIzaSyDM_SzQjLhp1e4bXm93kzGN04TlC5d9exw'
yt = build ('youtube', 'v3', developerKey=api_key)

interval_time = 3 # time in seconds between each plot refresh

plt.style.use ('seaborn')
dates = []
views = []

def animate (i) :

    request_dream = yt.channels().list(part='statistics', forUsername='DreamTraps')
    response_dream = request_dream.execute()
    current_views = response_dream['items'][0]['statistics']['viewCount']

    now = datetime.now ()
    dates.append (now)
    views.append (current_views)
    plt.plot_date (dates, views, linestyle = 'solid', color = 'r', label = 'Dream subscribers')
    plt.gcf().autofmt_xdate ()
    date_format = mpl_dates.DateFormatter ('%d/%m/%y, %H:%M:%S')
    plt.gca().xaxis.set_major_formatter(date_format)

ani = FuncAnimation(plt.gcf(), animate, interval=interval_time * 1000)
# plt.legend (loc = 'upper left')
# find how to legend an animated plot
plt.show()

# request_numberphile = yt.channels().list(part='statistics', forUsername = 'numberphile')
# response_numberphile = request_numberphile.execute ()
# print ('Numberphile total views :', response_dream['items'][0]['statistics']['viewCount'])