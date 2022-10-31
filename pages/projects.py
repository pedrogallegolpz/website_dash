import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar


dash.register_page(__name__, name='Projects', order=1)


def layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [sidebar()],
                        xs=4, sm=4, md=2, lg=2, xl=2, xxl=2, # set the dimension of the col in function of windows size
                        # xs=extra small, sm=small, md=middle, lg=large, xl=extra-large, xxl=extra-extra large
                    )
                    ,

                    dbc.Col(
                        [
                            html.Br(),
                            html.H3('Projects - Overview'),
                            html.Br(),
                            
                            dcc.Markdown(
                                """
                                In this section I show you some researchs or tools I have developed. I will introduce you into the problem, then I show you the proposal I worked on for solving it and then we analyse the results.
                                """,
                                style = {'textAlign':'justify','whiteSpace': 'pre-wrap',})

                        ], 
                        xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                    )

                ]
            )
        ]
    )
