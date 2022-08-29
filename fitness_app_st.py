#region Dependencies
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from datetime import datetime
from plotly.subplots import make_subplots

pd.options.mode.chained_assignment = None
#endregion

#region Read
df = pd.read_excel('fitness_data.xlsx', engine='openpyxl')
#endregion

#region Preprocessing
##Fill nulls with previous value
df.fillna(method='ffill', inplace=True)

##Today's Date
date_now = datetime.now().date()

##Take data from today's date
df = df[df['date'] <= pd.to_datetime(date_now)]

##Calculate self_difference
def self_difference(df):

    columns = df.iloc[:,2:].columns

    for column in columns:
        new_column = column + '_%diff'
        new_column_2 = new_column + '_start'
        df[new_column] = round((df[column] * 100) / df[column].shift() - 100,1)
        df[new_column_2] = round((df[column] * 100) / df[column][0] - 100,1)

    return df

df = self_difference(df)
#endregion 

#region Graphs
##Weight data
x = df['date']

y1 = df['johanna_weight']
y2 = df['adam_weight']
y3 = df['laura_weight']
y4 = df['michael_weight']

Y1 = df['johanna_weight_%diff_start']
Y2 = df['adam_weight_%diff_start']
Y3 = df['laura_weight_%diff_start']
Y4 = df['michael_weight_%diff_start']

y_1 = df['johanna_weight_%diff']
y_2 = df['adam_weight_%diff']
y_3 = df['laura_weight_%diff']
y_4 = df['michael_weight_%diff']

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=['Weight Timeline', 
                    'Weight % Difference from Start',
                    'Weight % Difference from Previous Value'])

##Weight
fig.add_trace(go.Scatter(x=x, y=y1, name='Johanna', line={'color':'orange'}),
            row=1, col=1)

fig.add_trace(go.Scatter(x=x, y=y2, name='Adam', line={'color':'red'}),
            row=1, col=1)

fig.add_trace(go.Scatter(x=x, y=y3, name='Laura', line={'color':'aqua'}),
            row=1, col=1)

fig.add_trace(go.Scatter(x=x, y=y4, name='Michael', line={'color':'green'}),
            row=1, col=1)

##Weight difference from Start
fig.add_trace(go.Scatter(x=x, y=Y1, name='Johanna', line={'color':'orange'}, showlegend=False),
            row=2, col=1)

fig.add_trace(go.Scatter(x=x, y=Y2, name='Adam', line={'color':'red'}, showlegend=False),
            row=2, col=1)

fig.add_trace(go.Scatter(x=x, y=Y3, name='Laura', line={'color':'aqua'}, showlegend=False),
            row=2, col=1)

fig.add_trace(go.Scatter(x=x, y=Y4, name='Michael', line={'color':'green'}, showlegend=False),
            row=2, col=1)

##Weight difference cumulative
fig.add_trace(go.Scatter(x=x, y=y_1, name='Johanna', line={'color':'orange'}, showlegend=False),
            row=3, col=1)

fig.add_trace(go.Scatter(x=x, y=y_2, name='Adam', line={'color':'red'}, showlegend=False),
            row=3, col=1)

fig.add_trace(go.Scatter(x=x, y=y_3, name='Laura', line={'color':'aqua'}, showlegend=False),
            row=3, col=1)

fig.add_trace(go.Scatter(x=x, y=y_4, name='Michael', line={'color':'green'}, showlegend=False),
              row=3, col=1)              

fig.add_shape(type='line', 
            x0=x.iloc[1,], 
            y0=0, 
            x1=x.iloc[-1,], 
            y1=0, 
            line=dict(color='black',),
            xref='x', 
            yref='y', 
            row=3, 
            col=1)

fig.update_layout(height=800, width=800, hovermode='x unified')

##Graph
st.plotly_chart(fig, use_container_width=True)

##Fat data
x = df['date']

y1 = df['johanna_fat']
y2 = df['adam_fat']
y3 = df['laura_fat']
y4 = df['michael_fat']

Y1 = df['johanna_fat_%diff_start']
Y2 = df['adam_fat_%diff_start']
Y3 = df['laura_fat_%diff_start']
Y4 = df['michael_fat_%diff_start']

y_1 = df['johanna_fat_%diff']
y_2 = df['adam_fat_%diff']
y_3 = df['laura_fat_%diff']
y_4 = df['michael_fat_%diff']

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=['Fat % Timeline', 
                    'Fat % Difference from Start',
                    'Fat % Difference from Previous Value'])

##Fat
fig.add_trace(go.Scatter(x=x, y=y1, name='Johanna', line={'color':'orange'}),
            row=1, col=1)

fig.add_trace(go.Scatter(x=x, y=y2, name='Adam', line={'color':'red'}),
            row=1, col=1)

fig.add_trace(go.Scatter(x=x, y=y3, name='Laura', line={'color':'aqua'}),
            row=1, col=1)

fig.add_trace(go.Scatter(x=x, y=y4, name='Michael', line={'color':'green'}),
            row=1, col=1)

##Fat difference from Start
fig.add_trace(go.Scatter(x=x, y=Y1, name='Johanna', line={'color':'orange'}, showlegend=False),
            row=2, col=1)

fig.add_trace(go.Scatter(x=x, y=Y2, name='Adam', line={'color':'red'}, showlegend=False),
            row=2, col=1)

fig.add_trace(go.Scatter(x=x, y=Y3, name='Laura', line={'color':'aqua'}, showlegend=False),
            row=2, col=1)

fig.add_trace(go.Scatter(x=x, y=Y4, name='Michael', line={'color':'green'}, showlegend=False),
            row=2, col=1)

##Fat difference cumulative
fig.add_trace(go.Scatter(x=x, y=y_1, name='Johanna', line={'color':'orange'}, showlegend=False),
            row=3, col=1)

fig.add_trace(go.Scatter(x=x, y=y_2, name='Adam', line={'color':'red'}, showlegend=False),
            row=3, col=1)

fig.add_trace(go.Scatter(x=x, y=y_3, name='Laura', line={'color':'aqua'}, showlegend=False),
            row=3, col=1)

fig.add_trace(go.Scatter(x=x, y=y_4, name='Michael', line={'color':'green'}, showlegend=False),
              row=3, col=1)              

fig.add_shape(type='line', 
            x0=x.iloc[1,], 
            y0=0, 
            x1=x.iloc[-1,], 
            y1=0, 
            line=dict(color='black',),
            xref='x', 
            yref='y', 
            row=3, 
            col=1)

fig.update_layout(height=800, width=800, hovermode='x unified')

##Graph
st.plotly_chart(fig, use_container_width=True)
#endregion
