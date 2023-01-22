# from django.shortcuts import render, HttpResponse

# # Create your views here.

# def index(request):
#     return render(request,'home/welcome.html')

from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv), data manipulation as in SQL
import plotly.express as px
import sys 
from plotly.subplots import make_subplots
import numpy as np # linear algebra

# Create your views here.

def index(request):
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x=x1,
            y = y1
        )
        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis = dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div


    def dataframe():
        
        df = pd.read_excel("C://Users//Rohith Balasubramani//Desktop//TEST.xlsx", sheet_name='UTFLT')
        df = df.drop(labels=range(0, 5), axis=0)
        df.columns = df.iloc[0] 
        #remove first row from the dataframe rows
        df = df[1:]
        df.columns=df.columns.str.replace('&','')
        df.columns = [c.replace('  ', '_') for c in df.columns]
        df.columns = [c.replace(' ', '_') for c in df.columns]
        df.columns = [c.replace('(', '') for c in df.columns]
        df.columns = [c.replace(')', '') for c in df.columns]
        dfday = pd.DatetimeIndex(df['Date']).day_name() # week day name
        df = df.set_index("Date")
        
        df = df.astype(float)
        df[df > 100] = np.nan
        for j in range(0,7): 
                df.iloc[:,j]= round( df.iloc[:,j].fillna(df.iloc[:,j].mean()),0)
        df['Day']=dfday

        return df

    def plotex():

        df =dataframe()
        fig = go.Figure([go.Scatter(x=df.index, y=df['OG1_MWH'], line=dict(color='green', width=2, dash='dashdot'))])
        # fig = px.line(df, x=df.index, y="TF1_MWH", title='Life expectancy in Canada')

        fig.update_layout(xaxis = dict(showline=True, showgrid=False, 
            showticklabels=True, linecolor='rgb(204,204,204)', linewidth=2, ticks='outside', 
            tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)')), 
        yaxis = dict(showline=True, showgrid=True, 
            showticklabels=True, linecolor='rgb(52,52,52)', linewidth=2, ticks='outside', 
            tickfont=dict(family='Arial', size=12, color='rgb(96,96,96)')), autosize= True,
            plot_bgcolor= 'white', title='OG 1', xaxis_title="Date", 
            yaxis_title="Power(in MW)")



        fig1 = plot(fig, output_type='div', include_plotlyjs=False)
      

        return fig1

    def Barex():

        df =dataframe()
        fig = go.Figure([go.Bar(x=df['Day'], y=df['OG1_MWH'])])

        # fig.add_trace(go.Scatter(x=df.index, y=df.TF1_MWH, mode="lines", name="TF1"))


        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                        marker_line_width=1.5, opacity=0.6)
        fig.update_layout(title_text='Day Wise Power Consumption')

	
        # fig = px.line(df, x=df.index, y="TF1_MWH", title='Life expectancy in Canada')
        fig1 = plot(fig, output_type='div', include_plotlyjs=False)
      

        return fig1

        # y=df.columns[1:-6]

    def Multiex():

        df =dataframe()
        

        # fig = make_subplots(
	    # rows=1, cols=1,
	    # column_widths=[0.15,0.15,0.15, 0.55],
	    # row_heights=[0.77, 0.33],
	    # specs=[[{"secondary_y": True, "colspan": 3},None, None, {"secondary_y": True, }],
	    #        [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "table"}]],
	    #         subplot_titles=("Baseline and Forecast", "Cost Analysis", "Time Completed", 
	    #         	"Work Completed", "Cost Distribution", "Quantitative Analysis"))


        # fig.add_trace(go.Scatter(x=df.index, y=df['TF1_MWH'], mode="lines+markers", name="Base-Line"),row=1, col=1,  secondary_y=True)
        # fig.add_trace(go.Scatter(x=df.index, y=df['TF2_MWH'], mode="lines+markers", name="Base-Line"),row=1, col=1,  secondary_y=True)
        # fig.add_trace(go.Scatter(x=df.index, y=df['TF3_MWH'], mode="lines+markers", name="Actual", line=dict(color='firebrick', width=2, dash='dashdot')),row=1, col=1,  secondary_y=True)
        # # fig = px.line(df, x=df.index, y="TF1_MWH", title='Life expectancy in Canada')

        
        fig= go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df.TF1_MWH, mode="lines", name="TF1"))
        fig.add_trace(go.Scatter(x=df.index, y=df.TF2_MWH, mode="lines", name="TF2",
        line=dict(color='firebrick', width=2, dash='dashdot'))) 
        fig.add_trace(go.Scatter(x=df.index, y=df.TF3_MWH, mode="lines", name="TF3",
        line=dict(color='purple', width=2))) 
        
        fig.update_layout(xaxis = dict(showline=True, showgrid=False, 
            showticklabels=True, linecolor='rgb(204,204,204)', linewidth=2, ticks='outside', 
            tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)')), 
        yaxis = dict(showline=True, showgrid=True, 
            showticklabels=True, linecolor='rgb(52,52,52)', linewidth=2, ticks='outside', 
            tickfont=dict(family='Arial', size=12, color='rgb(96,96,96)')), autosize= True,
            plot_bgcolor= 'white', title='Transformers', xaxis_title="Date", 
            yaxis_title="Power(in MW)")
	
       
       
       
        fig1 = plot(fig, output_type='div', include_plotlyjs=False)
      

        return fig1



    context ={
        'plot1': Barex(),
        'plot2': plotex(),
        'plot3':Multiex()
        
    }

    return render(request, 'home/welcome.html', context)