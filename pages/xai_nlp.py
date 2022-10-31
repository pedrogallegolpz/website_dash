import dash
from dash import html, dcc 
import dash_bootstrap_components as dbc
from .side_bar import sidebar
from  .explainability_nlp import dashboard

dash.register_page(__name__, path="/project_explainabilityNLP", name='XAI tool for NLP')

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
                            html.H3('XAI tool for NLP', style={'color': 'rgba(255,255,255)'}),
                            html.Br(),

                            dcc.Markdown(
                                """
                                I developed this tool for the XAI service provide by [AyGLOO](https://www.aygloo.com/). The problem is to find a usefull, intuitive and compact tool to explain models in NLP problems.

                                In the dashboard preview you can see here, you can see the particular case of classification problem in NLP. I provide two problems: diagnosis on medical patient descriptions ("normal" and "abnormal") and new sections classification ("autonomía", "Cultura y Sociedad", "Economía", "Política" y "Sanidad"). The first has three examples and the other has only one example.
                                
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap'}),

                            dcc.Markdown(
                                """
                                * HELP you can click one of the semi-circle to show the item attribution to the class over the text. Green means positive attribution and red means negative attribution.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap'}),


                            html.Br(),
                            dashboard.layout(),
                            html.Br(),

                            dcc.Markdown(
                                """
                                This tool is so powerful. It can explain the model decision as an human would: reading the text sequentially, giving us the information intuitively and compactly. Let's explain the examples:
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap'}
                            ),

                            dcc.Markdown(
                                """
                                We can swap between examples on the tab located on the top. Then we can choose between item splits: we can split the text in phrases or words. When we fixed this options, we can study the figure below them. This figure show the probabilities of each class across the text, accumulating the splits until the last, where the model will have been processed completely the text. The indicators show the increase in probability compared to the previous step. These indicators can be clicked to show more information. Finally, on the bottom we find the text.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap'}
                            ),
                            dcc.Markdown(
                                """
                                If we clicked in any class indicator above the text, we can show the attributions. Swapping between 'phrases' and 'words' in the option located above the figure, we can understand how the model is working.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap'}
                            ),
                            html.Br(),

                            dcc.Markdown("""##### Medicine 1""", style={'color': 'rgba(255,255,255)'}),
                            dcc.Markdown(
                                """
                                The actual class of this example is NORMAL.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),
                            dcc.Markdown(
                                """
                                At the end, the model has doubts about the final class: 0.6 for normal and 0.4 for abnormal (disease). The reason is the word 'defibrillator', which is a bias learnt by the model. 
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),



                            dcc.Markdown("""##### Medicine 2""", style={'color': 'rgba(255,255,255)'}),
                            dcc.Markdown(
                                """
                                The actual class of this example is ABNORMAL.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),
                            dcc.Markdown(
                                """
                                The model is wrong in this case.  If we read the text we know that the patient has a disease: scoliosis, but the model ignores it. Probably, the model doesn't learnt 'scoliosis' as a item of his vocabulary, so the model ignores it.  
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),



                            dcc.Markdown("""##### Medicine 3""", style={'color': 'rgba(255,255,255)'}),
                            dcc.Markdown(
                                """
                                The actual class of this example is NORMAL.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),
                            dcc.Markdown(
                                """
                                The model is wrong in this case. The text analyse the patient concluding that the patient is healthy. Although, in the process explaining the patient health features, the model use some words like "involving" or "compatible", which seem very used to make a abnormal patient description. It means that the model has learnt words to make a diagnosis which actually don't have any relevance: other example of bias.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),




                            dcc.Markdown("""##### News""", style={'color': 'rgba(255,255,255)'}),
                            dcc.Markdown(
                                """
                                "COVID", "CASOS POSITIVOS" are some of the parts that make a positive attribution to SAN class (as we can hope). On the other hand, "Govern" has a positive attribution to POL class. These attributions are logical. The model seems to work well in this example. 
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding':'0px 0px 0px 20px'}
                            ),

                            html.Br(),
                            html.Br(),
                            html.Br(),




                        ], 
                        xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                    )

                ]
            )
        ]
    )

