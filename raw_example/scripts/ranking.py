import plotly.plotly as py
import plotly
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
import pandas as pd

df = pd.read_csv('../data/ranking.csv')


# Create a trace
trace = go.Scatter(
    x = df['GDP'],
    y = df['Ranking'],
    mode = 'markers',
    text = df['Country'],
    
)


data = [trace]

layout = go.Layout(
        title='Ranking VS GDP',
        xaxis=dict(
            title='GDP',
            
        ),
        yaxis=dict(
            title='Ranking',
            
        )
    )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig,filename='../html/ranking.html',config={'displayModeBar': False})
