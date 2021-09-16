import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
#pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

dataset = pd.read_csv('C:\\Users\ASUS\Downloads\stock_list.csv')

fig = go.Figure(data=go.Ohlc(x=dataset['date'],                    
                open=dataset['open'],
                high=dataset['high'],
                low=dataset['low'],
                close=dataset['close']))

fig.update_layout(
    title='NORTHERN TRUST HACKATHON',
    yaxis_title='Stock on the basis of date',
    shapes = [dict(
        x0='2021-1-04', x1='2021-1-31', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2021-1-04', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left')]
)

fig.show()


