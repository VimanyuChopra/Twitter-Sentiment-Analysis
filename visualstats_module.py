import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_visuals(rdf):
    
    sdf = rdf['Sentiment'].value_counts()
    s = sum(sdf.tolist())

  
    labels = sdf.index.tolist()
    fracs = [x / s for x in sdf.tolist()]
    explode=(0.1, 0.1, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=30)
    ax1.axis('equal')  
    plt.title('Sentiments', bbox={'facecolor':'0.8', 'pad':5})
    plt.show()
