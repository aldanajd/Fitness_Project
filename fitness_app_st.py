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
df = pd.read_csv('fitness_data.csv')
#endregion

#region Preprocessing
##Fill nulls with previous value
df.fillna(method='ffill', inplace=True)

##Convert Date
df['date'] = pd.to_datetime(df['date'])

##Today's Date
date_now = datetime.now().date()
year_now = date_now.year
month_now = date_now.month

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

#region Sidebar (Filters)
month_map = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

month_map1 = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}

unique_years = ['All']
months = ['All']

unique_years.extend(list(set(df['date'].dt.year)))
unique_months = list(set(df['date'].dt.month))

months.extend([month_map1.get(n) for n in unique_months])

year = st.sidebar.selectbox('Select Year', options=unique_years, index=unique_years.index(year_now))
month = st.sidebar.selectbox('Select Month', options=months, index=unique_months.index(month_now)+1)

if year == 'All':
    df1 = df
else:
    df1 = df[df['date'].dt.year == year]

if month == 'All':
    pass
else:
    df1 = df1[df1['date'].dt.month == month_map.get(month)]
#endregion

#region Tabs
tab1, tab2, tab3 = st.tabs(["Timeline", "Progress since the Beginning", "Progress since Previous Day"])

with tab1:
    x = df1['date']

    y1 = df1['johanna_weight']
    y2 = df1['adam_weight']
    y3 = df1['laura_weight']
    y4 = df1['michael_weight']

    y_1 = df1['johanna_fat']
    y_2 = df1['adam_fat']
    y_3 = df1['laura_fat']
    y_4 = df1['michael_fat']

    fig = make_subplots(rows=2, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.07,
                        subplot_titles=['Weight(Kg) - Timeline', 
                        'Fat(%) - Timeline'])

    ##Weight
    fig.add_trace(go.Scatter(x=x, y=y1, name='Johanna', line={'color':'orange'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y2, name='Adam', line={'color':'red'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y3, name='Laura', line={'color':'aqua'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y4, name='Michael', line={'color':'green'}),
                row=1, col=1)

    ##Fat
    fig.add_trace(go.Scatter(x=x, y=y_1, name='Johanna', line={'color':'orange'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_2, name='Adam', line={'color':'red'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_3, name='Laura', line={'color':'aqua'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_4, name='Michael', line={'color':'green'}, showlegend=False),
                row=2, col=1)

    fig.update_layout(height=500, width=800, hovermode='x unified')

    ##Graph
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    x = df1['date']

    y1 = df1['johanna_weight_%diff_start']
    y2 = df1['adam_weight_%diff_start']
    y3 = df1['laura_weight_%diff_start']
    y4 = df1['michael_weight_%diff_start']

    y_1 = df1['johanna_fat_%diff_start']
    y_2 = df1['adam_fat_%diff_start']
    y_3 = df1['laura_fat_%diff_start']
    y_4 = df1['michael_fat_%diff_start']

    fig = make_subplots(rows=2, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.07,
                        subplot_titles=['Weight(%) - Progress since the Beginning', 
                        'Fat(%) - Progress since the Beginning'])

    ##Weight
    fig.add_trace(go.Scatter(x=x, y=y1, name='Johanna', line={'color':'orange'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y2, name='Adam', line={'color':'red'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y3, name='Laura', line={'color':'aqua'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y4, name='Michael', line={'color':'green'}),
                row=1, col=1)

    ##Fat
    fig.add_trace(go.Scatter(x=x, y=y_1, name='Johanna', line={'color':'orange'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_2, name='Adam', line={'color':'red'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_3, name='Laura', line={'color':'aqua'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_4, name='Michael', line={'color':'green'}, showlegend=False),
                row=2, col=1)

    fig.update_layout(height=500, width=800, hovermode='x unified')

    ##Graph
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    x = df1['date']

    y1 = df1['johanna_weight_%diff']
    y2 = df1['adam_weight_%diff']
    y3 = df1['laura_weight_%diff']
    y4 = df1['michael_weight_%diff']

    y_1 = df1['johanna_fat_%diff']
    y_2 = df1['adam_fat_%diff']
    y_3 = df1['laura_fat_%diff']
    y_4 = df1['michael_fat_%diff']

    fig = make_subplots(rows=2, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.07,
                        subplot_titles=['Weight(%) - Progress since Previous Day', 
                        'Fat(%) - Progress since Previous Day'])

    ##Weight
    fig.add_trace(go.Scatter(x=x, y=y1, name='Johanna', line={'color':'orange'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y2, name='Adam', line={'color':'red'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y3, name='Laura', line={'color':'aqua'}),
                row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y4, name='Michael', line={'color':'green'}),
                row=1, col=1)

    ##Fat
    fig.add_trace(go.Scatter(x=x, y=y_1, name='Johanna', line={'color':'orange'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_2, name='Adam', line={'color':'red'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_3, name='Laura', line={'color':'aqua'}, showlegend=False),
                row=2, col=1)

    fig.add_trace(go.Scatter(x=x, y=y_4, name='Michael', line={'color':'green'}, showlegend=False),
                row=2, col=1)

    fig.update_layout(height=500, width=800, hovermode='x unified')

    ##Graph
    st.plotly_chart(fig, use_container_width=True)
#endregion

#region Graphs
##Weight data
x = df1['date']

y1 = df1['johanna_weight']
y2 = df1['adam_weight']
y3 = df1['laura_weight']
y4 = df1['michael_weight']

Y1 = df1['johanna_weight_%diff_start']
Y2 = df1['adam_weight_%diff_start']
Y3 = df1['laura_weight_%diff_start']
Y4 = df1['michael_weight_%diff_start']

y_1 = df1['johanna_weight_%diff']
y_2 = df1['adam_weight_%diff']
y_3 = df1['laura_weight_%diff']
y_4 = df1['michael_weight_%diff']

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=['Weight(Kg) - Timeline', 
                    'Weight(%) - Progress since the Beginning',
                    'Weight(%) - Progress since Previous Day'])

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

fig.update_layout(height=800, width=800, hovermode='x unified')

##Graph
st.plotly_chart(fig, use_container_width=True)

##Fat data
x = df1['date']

y1 = df1['johanna_fat']
y2 = df1['adam_fat']
y3 = df1['laura_fat']
y4 = df1['michael_fat']

Y1 = df1['johanna_fat_%diff_start']
Y2 = df1['adam_fat_%diff_start']
Y3 = df1['laura_fat_%diff_start']
Y4 = df1['michael_fat_%diff_start']

y_1 = df1['johanna_fat_%diff']
y_2 = df1['adam_fat_%diff']
y_3 = df1['laura_fat_%diff']
y_4 = df1['michael_fat_%diff']

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=['Fat(%) - Timeline', 
                    'Fat(%) - Progress since the Beginning',
                    'Fat(%) - Progress since Previous Day'])

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

fig.update_layout(height=800, width=800, hovermode='x unified')

##Graph
st.plotly_chart(fig, use_container_width=True)
#endregion
