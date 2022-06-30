import pandas as pd
import plotly.express as px


def histogram(df, x=None, y=None, category=None, histfunc='count', visiblex=True, visibley=False, barnorm=None, histnorm=None, color=None, orientation=None, text_auto=True, nbins=None, title='', width=850, height=1000):

    fig = px.histogram(
        df, 
        x, 
        y,
        nbins=nbins,
        template='seaborn',
        text_auto=text_auto,
        histfunc=histfunc,
        width=width,
        height=height,
        title=title,
        color=color,
        histnorm=histnorm,
        barnorm=barnorm,
        category_orders=category,
        orientation=orientation
    )
    if histnorm == 'percent' or barnorm == 'percent':
        fig.update_traces(
            textfont_size=16,
            texttemplate='%{x:.2f}%',
            hoverinfo='skip',
            hovertemplate=None
        )
    else:
        fig.update_traces(
            textfont_size=16,
            hoverinfo='skip',
            hovertemplate=None
        )
        
    
    fig.update_layout(
        bargap=0.2,
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(size=16),
        margin=dict(l=20, r=20, pad=20),
        title=dict(xanchor='left', yanchor='top', x=0.01, y=0.95)
        
    )
    
    fig.update_xaxes(
        zeroline=False, 
        showgrid=False,
        title='',
        visible=visiblex
    )
    fig.update_yaxes(
        zeroline=False, 
        showgrid=False,
        categoryorder='total ascending',
        automargin=True,
        title='',
        visible=visibley
        
    )
    
    return fig

def line(df, x=None, y=None, title='', color=None, text=None, markers=False, hover=False, hovermode='closest'):
    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        template='seaborn',
        markers=markers,
        title=title,
        text=text,
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(size=16),
        legend=dict(title=None, yanchor='top', xanchor='left', x=0, y=1, font=dict(size=16)),
        title=dict(yanchor='top', xanchor='left', x=0.12, y=0.95),
        hovermode=hovermode
    )
    if not hover:
        fig.update_traces(
            textposition='top center',
            texttemplate='<b>%{text:$,.3s}</b>',
            line=dict(width=5),
            hovertemplate=None,
            hoverinfo='skip',
            hoverlabel=dict(font_size=16),
            marker=dict(size=15)
        )
    else:
        fig.update_traces(
            textposition='top center',
            texttemplate='<b>%{text:$,.3s}</b>',
            line=dict(width=5),
            hoverlabel=dict(font_size=16),
            marker=dict(size=15)
        )
    
    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        title='',
        rangemode='tozero',
        visible=False
    )
    
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
    )
    
    return fig

def total_games(df):
    return df['Game'].sum()

def concat_df(df1, df2):
    df = pd.concat([df1, df2])
    df.drop('Unnamed: 0', axis=1, inplace=True)
    return df

def total_income(df):
    return df['Global'].sum()

def num_games_launched_per_year(df):
    return df.groupby(['Year'], as_index=False)['Game'].count() 

def profit_per_year(df):
    return df.groupby(['Year'], as_index=False)['Global'].sum()

def count_genres(df):
    return df.Genre.nunique()

def count_games(df):
    return df.Game.nunique()
