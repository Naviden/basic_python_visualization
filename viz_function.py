import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def do_the_magic(df):
    plt.figure(figsize=(20, 13))
    plt.suptitle('Temperature and Humidity Analysis', fontsize=25)


    plt.subplot(221)
    plt.hist(df.hum, bins=50, alpha=0.5, edgecolor='black', linewidth=1.2)
    plt.title('Humidity Distribution', fontsize=20)
    xmin, xmax, ymin, ymax = plt.axis()
    #plt.vlines(np.median(df.hum), 0, ymax, 'r')
    plt.vlines(np.mean(df.hum), 0, ymax, 'r')
    font = {'family': 'serif',
            'color':  'blue',
            'weight': 'normal',
            'size': 13,
            }
    plt.text(0.06, ymax*0.5, 'The blue line shows\nthe Mean of the data.\nAdding a line for the\nmedian we will see\nthat these line overlap\ndue to the distribution\nof data.',
            fontdict=font)
    #plt.text(np.median(df.hum)*1.02, ymax, 'Median value', fontdict=font)
    plt.yticks([])





    plt.subplot(222)
    #plt.figure(figsize=(10, 7))

    for i in range(len(df)):
        if df.holiday[i] == 0:
            # if it's not holiday
            alpha = 0.3
            size = 28

            # checking for the green area
            if df.hum[i] < np.mean(df.hum) and  df.atemp[i] > np.mean(df.atemp):
                c = 'g'
            else:
                c = 'b'
        else:
            # in case of holiday
            c = 'r'
            alpha = 0.8
            size = 40
        plt.scatter(df.hum[i] , df.atemp[i], c=c, alpha=alpha, edgecolors='k', s=size)

    plt.title('Humidity Vs. Temperature\nHolidays are showed in red', fontsize=16)
    plt.xlabel('Humidity', fontsize=14)
    plt.ylabel('Temperature', fontsize=14)
    plt.hlines(np.mean(df.atemp), 0, 1, 'grey',linestyles='--')
    plt.vlines(np.mean(df.hum), 0, 1, 'grey',linestyles='--')
    plt.text(0.08, 0.8, 'Records in this area has a lower\nhumidity and a higher temperature\nrespect to the average values.')
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.show()


    plt.figure(figsize=(20, 13))

    plt.subplot(212)

    for i in range(len(df)):
        if i in list(range(3)) + list(range(len(df), len(df)-3, -1)):
            col = 'b'
            size = 10
            alpha = 0.2
        if df.atemp[i] < np.mean(df.atemp[i-3: i+4]) * 0.65 or df.atemp[i] > np.mean(df.atemp[i-3: i+4]) * 1.4:
            col = 'r'
            size = 23
            alpha = 1
            plt.vlines(df.dteday[i], 0, 0.05, 'r')
        else:
            col = 'b'
            size = 10
            alpha = 0.2
        plt.scatter(df.dteday[i], df.atemp[i], c=col, alpha=alpha, s=size)




    plt.plot(df.dteday, df.atemp, color='k', alpha=0.5, label='Normalized feeling temperature')

    # plotting the moving average
    # creating a moving average for 1 month
    df['roll_avg'] = df.atemp.rolling(window=30).mean()
    plt.plot(df.dteday, df.roll_avg, color='blue', label='Rolling average(30 days) of normalized feeling temperature')





    plt.title('How temperature changes from 2011 to 2013\nRed points show the days which are consider anomalies respect to the selected window',
            fontsize=14)
    plt.xticks(rotation=90)

    plt.ylim(0, 1)
    plt.ylabel('Normalized feeling temperature', fontsize=15)
    plt.legend()
    plt.show()