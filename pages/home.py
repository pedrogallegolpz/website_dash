import dash
from dash import html, dcc 
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", order=0)

layout = html.Div([
    dcc.Markdown('# Pedro Gallego López', style={'textAlign':'center', 'color': 'rgba(255,255,255)'}),
    dcc.Markdown('_Dublin, Ireland_', style={'textAlign':'center', 'color': 'rgba(255,255,255)'}),
    
    html.Div(html.Hr(style = {'width':'300px', 'textAlign':'center', 'margin':'auto', 'color': 'rgba(255,255,255)'}),),

    html.Br(), 

    dcc.Markdown("""
                Ambitious, team worker, leader, creative, mate and friend passionate about how maths model the world and how the 
                AI will shape human future:
                _Data is power._
                
                Looking for mentally challenging opportunities that allow me to use my knowledge, to learn new things and to grow 
                in new scenarios. One quote
                _`Obvious, is the most dangerous word´_ - E.T.Bell
                """, style={'textAlign':'center','whiteSpace': 'pre-wrap'}),

    html.Br(),
    dcc.Markdown('### Professional Summary', style={'textAlign':'center', 'color': 'rgba(255,255,255)'}),
    html.Hr(),
    
    dcc.Markdown("""
                Mathematician and Computer Scientist focused on Data Science. With a great machine learning background in few years which envolve Computer Vision and Natural Language Processing projects, both personal and professional ones. 

                Passionate about research and how to translate advances in technology into tools with value for people.
                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap', 'padding': '0px 100px 0px 100px'}),

    html.Br(),
    
    dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Markdown("02/2022 ➝ current", style={'textAlign':'center', 'color': 'rgba(255,255,255)'})
                ],
                width=2,
            ),

            dbc.Col(
                [
                    dcc.Markdown("##### AyGLOO - Data Scientist. Full remote", style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("""
                    Descripción AyGLOO . 
                    """),
                    
                    dcc.Markdown('###### LEGISLATION RADAR (main customer PriceWaterhouseCoopers)',  style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("""
                    I managed the LEGISLATION RADAR. It consists in predicting changes in the current Spanish Legislation
                    that can affect to a specific sector and notify the customer in real time. I automatize the work that
                    a complete PwC team had to do before, achieving best results. I did this,""",
                    style={'textAlign':'justify', 'padding':'0px 0px 0px 20px'}),

                    html.Ol([
                        html.Li("Designing a large dataset built of laws projects, government webs, tweets and more websites with relevant information that are being extracted (scraping) with a Google Cloud Scheduler."),
                        html.Li("Applying Unsupervised Learning to create links between data and Natural Language Processing technics to get semantic information in order to calculate the relevance of each new document."),
                        html.Li("Creating a Dashboard (python Dash tool) on Google Cloud Run."),
                    ], style={'textAlign':'justify', 'padding':'0px 0px 0px 70px'}),
                  

                    dcc.Markdown('######  FAKE NEWS DETECTOR (with EuropaPRESS)', style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("""
                    Natural Language Processing (NLP) I+D project in order to become in a product for EuropaPRESS. 
                    The fake news can be seen in different ways: as anomalies or as a supervised problem are some 
                    of these ways. It was necessary to use technics like Named Entity Recognition (NER), Topic Modeling
                    and Clustering; to compare traditional methods (like TF-IDF) to state of the art (Transformers). 
                    
                    To create a trusted tool, it has to have the ability to explain his decisions. I studied the state 
                    of the art in NLP  explainability and created, with my team, a new method more interpretable than
                    the current literature.
                    """, style={'textAlign':'justify', 'padding':'0px 0px 0px 20px'}),


                    html.Ul([
                        html.Li([
                            "I use scraping to generate databases. Libraries:",
                            html.Ul([
                                html.Li("Selenium: web scraping."),
                                html.Li("Fitz: pdf scraping."),
                                html.Li("Snscrape: social networks scraping (twitter)."),
                            ]),

                        ]),
                        html.Li("NLP"),
                    ]),
                ]
            )
        ]
    ),

    html.Br(),
    dcc.Markdown('### Studies', style={'textAlign':'center', 'color': 'rgba(255,255,255)'}),
    html.Hr(),

    dbc.Row(
        [
            dbc.Col([dcc.Markdown("09/2016 ➝ 06/2022",
                     style={'textAlign':'center', 'color': 'rgba(255,255,255)'})],
                     width=2),

            dbc.Col([html.H5("Dual bachelor degree in Mathematics and Computer Science.",
                     style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("University of Granada (UGR)."),
                    html.Ul([
                        html.Li("Artificial Intelligence specialty certificate", 
                                style={'color': 'rgba(255,255,255)'}),
                        html.Ul([
                            html.Li([html.Strong("Machine Learning and Metaheuristics Honor Student.")])
                        ]),
                    ])
                ]),
        ]
    ),

    dbc.Row(
        [
            dbc.Col([dcc.Markdown("09/2016 ➝ 06/2022",
                     style={'textAlign':'center', 'color': 'rgba(255,255,255)'})],
                     width=2),

            dbc.Col([html.H5("Dual bachelor degree in Mathematics and Computer Science.",
                     style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("University of Granada (UGR)."),
                    html.Ul([
                        html.Li("Artificial Intelligence specialty certificate", 
                                style={'color': 'rgba(255,255,255)'}),
                        html.Ul([
                            html.Li([html.Strong("Machine Learning and Metaheuristics Honor Student.")])
                        ]),
                    ])
                ]),
        ]
    ),



    dbc.Row(
        [        
            dbc.Col([dcc.Markdown("11/2022 ➝ 02/2022",
                     style={'textAlign':'center', 'color': 'rgba(255,255,255)'})],
                     width=2),

            dbc.Col([html.H5("English Studies.",
                     style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("Centre of English Studies. Dublin (Ireland) on-site.")
                ])
        ]
    ),


    dbc.Row(
        [        
            dbc.Col([dcc.Markdown("05/2020 ➝ 07/2020",
                     style={'textAlign':'center', 'color': 'rgba(255,255,255)'})],
                     width=2),

            dbc.Col([html.H5("Financial Market Technician.",
                     style={'color': 'rgba(255,255,255)'}),
                    dcc.Markdown("Instituto de Estudios Bursátiles (IEB). On-remote.")
                ])
        ]
    ),



    
    

    html.Br(),
    dcc.Markdown('### Skills', style={'textAlign':'center', 'color': 'rgba(255,255,255)'}),
    html.Hr(),

    html.Div([
        dcc.Markdown("I can say I am an expert with **Python**, It is my main programming language for years. It's the language where I studied all I know about Data Science and Maths methods. I have experience in python doing:"),
        html.Ul([
            html.Li("Data wrangling: I usually work with data so I have to manipulate it everyday. I know about data preprocessing, data analysis, data visualization, etc."),
            html.Ul([
                html.Li("Data preprocessing and Data analysis: I usually use Pandas and Numpy to clean data, explore it and extract statistics."),
                html.Li("Data visualization: There are so many libraries to visualize data. For extracting static and simple information I usually use Matplotlib or Seaborn. On the other hand we have plots more complex where Dash and Bokeh are my favourite tools."),
            ]),

            html.Li("Machine Learning: Machine Learning is the main tool for data scientists in order to solve their problems. Libraries:"), 
            html.Ul([
                html.Li("Scikit-Learn: I started learning ML with this library. I have experience using most of his models and methods for handling data. I did a good study about dimensional reduction with autoencoders, PCA, tSNE and UMAP for a specific problem, concluding that autoencoders are able to reduct dimension more efectivily."),
                html.Li("PyTorch: I started using this library in 2021 with my bachelor thesis (you can see it in projects section). Now, I have a great control about how to handle Computer Vision problems with PyTorch. I also hace experience with NLP problems with Pytorch."),
                html.Li("Keras and TensorFlow: I started learning Deep Learning in Computer Vision with keras and TF. I made some projects with these libraries, like face detection (building a YOLOv3 net). I also use keras models for NLP problems."),
                html.Li("HuggingFace and transformers: I have experience using NLP models from these libraries: text classification and I did a little study about text summarization (extractive and abstractive) using their models."),
                html.Li("SPACY, FLAIR and NLTK: I did a research of the state of the art in Named Entity Recognition (NER), so I deeply use these libraries a couple of months.")
            ]),

            html.Li("Scraping: in order to generate databases for my problems. Libraries:"), 
            html.Ul([
                html.Li("Selenium: web scraping."),
                html.Li("Fitz: pdf scraping."),
                html.Li("Snscrape: social networks scraping (twitter)."),
            ]),
        ]),
        dcc.Markdown("I know about other programming languages like C++, Java, C. Databases like mongoDB and SQL."),

        dcc.Markdown("**Statistics**: I am a Mathematician so... I LOVE STATISTICS. So, I really like working with data to apply my knowledge."),
        dcc.Markdown("**Google Cloud Platform**: I worked in Google Platform in my stage at AyGLOO."),
        ], 
        style={'textAlign':'justify', 'padding': '0px 100px 0px 100px'}
    ),



    html.Br(),
    html.Br(),
    html.Br(),

    


],

style={'color': 'rgba(200,200,200)'})