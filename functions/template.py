def layout(df1, df2):
    from functions.graphs import concat_df, line
    from dash import html, dcc
    import dash_bootstrap_components as dbc

    df = concat_df(df1, df2)
    fig = line(df.groupby(['Year', 'Platform'], as_index=False)[['Global']].sum(), title='Profit per Year', color='Platform', x='Year', y='Global', markers=True, text='Global')
    return dbc.Container([
        dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(['Choose the platform:'])
                ]),
            dbc.CardBody([
                dcc.Dropdown(['PS4', 'Xbox One'], 'PS4', id='drop-1'),
                html.H4(id='lucro-total', style=dict(display='inline-block', marginRight='15px')),
                html.H4(id='n_games', style=dict(display='inline-block', marginLeft='15px'))
            ])
            ])
        ])
    ], style=dict(paddingTop='25px', paddingBottom='25px'), justify='center'),
        dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(['Sales over the years'])
                ]),
                dbc.CardBody([
                    dcc.Graph(figure=fig)
                ])
            ])
        ], width=6),
            dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(id='subtitle')
                ]),
                dbc.CardBody([
                    dcc.Graph(id='detailed_profit')
                ])
            ])
        ], width=6)
        ], justify='between'),
        dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(id='title-card')
                ]),
                dbc.CardBody([
                    dcc.Graph(id='bargraph')
                ])
            ])
        ], style=dict(paddingTop='15px'), className='w-100')
    ])
    ])
