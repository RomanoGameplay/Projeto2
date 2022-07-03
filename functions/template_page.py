def card_title():
    return dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(['Choose the platform:'])
                ]),
            dbc.CardBody([
                dcc.Dropdown(['PS4', 'Xbox One'], 'PS4', id='drop-1'),
                html.H4(id='lucro-total', style=dict(display='inline-block')),
                html.H4(id='n_games', style=dict(display='inline-block'))
            ])
            ], className='w-50')
        ])
    ], style=dict(paddingTop='25px'))

def title():
    return dbc.Row([
        dbc.Col([
            html.H1(children='Sales over the years', id='title')
        ], style=dict(paddingLeft='20px')),
        ], style=dict(paddingTop='25px', paddingBottom='25px'))

def graph_detailed_profit():
    return dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(['Detailed view of sales over the years'])
                ]),
                dbc.CardBody([
                    dcc.Graph(id='linegraph-detailed-profit')
                ])
            ])
        ])

def graph_profit():
    return dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(['Sales over the years'])
                ]),
                dbc.CardBody([
                    dcc.Graph(id='linegraph-total-profit')
                ])
            ])
        ]),
        graph_detailed_profit()
    ])

def graph_bar():
    return dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H2(['Quantity of each genre'], id='title-card')
                ]),
                dbc.CardBody([
                    dcc.Graph(id='bargraph')
                ])
            ])
        ], style=dict(paddingTop='15px'), className='w-100')
    ])

def layout():
    return dbc.Container([
        card_title(),
        title(),
        graph_profit(),
        graph_bar()
    ])
