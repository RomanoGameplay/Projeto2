from dash import Input, Output
from graphics import *

def display_linegraph_detailed_profit():
    @app.callback(
        Output('detailed_profit', 'figure'),
        Input('drop-1', 'value')
    )
    def update_graph_line(value):
        if value == 'Xbox One':
            fig = line(df_xbox.groupby('Year', as_index=False)[df_xbox.describe(include=float).columns].sum(), hovermode='x unified', hover=True, x='Year', y=df_xbox.describe(include=float).columns)
        else:
            fig = line(df_ps4.groupby('Year', as_index=False)[df_ps4.describe(include=float).columns].sum(), hovermode='x unified', hover=True, x='Year', y=df_ps4.describe(include=float).columns)

        fig.update_layout(legend=dict(x=0 , y=1.1, xanchor='left',yanchor='top'))

        for region in df.describe(include=float).columns:
            fig.update_traces(
                selector=dict(name=region),
                hovertemplate='<b>' + region + '</b><br>Profit = %{y}<extra></extra>'
            )

        fig.update_traces(
            selector={'name':'Global'}, 
            showlegend=False, 
            visible='legendonly', 
        )
        return fig

def update_subtitle_detailed_profit():
    @app.callback(
        Output('subtitle','children'),
        Input('drop-1','value')
    )
    def update(value):
        return 'Detailed view of sales over the years: {}'.format(value)

def update_bar_subtitle():
    @app.callback(
        Output('title-card', 'children'),
        Input('drop-1', 'value')
    )
    def update_subtitle(value):
        return 'Quantity of each genre: {}'.format(value)

def update_graphbar():
    @app.callback(
        Output('bargraph', 'figure'),
        Input('drop-1', 'value')
    )
    def bar(value):
        if value == 'Xbox One':
            return histogram(df_xbox, y='Genre', visibley=True, visiblex=False) 
        else:
            return histogram(df_ps4, y='Genre', visibley=True, visiblex=False) 

def show_total():
    @app.callback(
        Output('lucro-total','children'),
        Input('drop-1','value')
    )
    def total(value):
        if value == 'PS4':
            return 'Total income: ${}'.format(round(total_income(df_ps4), 2))
        else:
            return 'Total income: ${}'.format(round(total_income(df_xbox), 2))

def show_n_games():
    @app.callback(
        Output('n_games','children'),
        Input('drop-1','value')
    )
    def show_games(value):
        if value == 'PS4':
            return 'Num. of games: {}'.format(count_games(df_ps4))
        else:
            return 'Num. of games: {}'.format(count_games(df_xbox))