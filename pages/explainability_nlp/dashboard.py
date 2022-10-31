from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import json
import plotly.graph_objects as go


from .utils import explain_evolucion, horizontal_bar_chart, split_text, get_rgb_atribucion, split_patterns

path_json = './assets/textos.json'
def load_json_ejemplos(ejemplo, path):
    if ejemplo<=3:
        ejemplo_str = f'medicine{ejemplo}'
    else:
        ejemplo_str = 'news1'

    with open(path,'r') as f:
        dic = json.load(f)

    idx = np.where(np.array(dic['ejemplos'])==ejemplo_str)[0][0]

    return dic, idx


def update_increments(value, min, max, step, figure, selected_points=[]):
    rango = np.linspace(min, max, int(np.round((max-min)/step))+1)[1:] # El 0 está contenido en el slider y por eso hay que restarlo
    
    value_arr = np.array([value for i in rango])
    
    split_num = np.argmin(abs(rango-value_arr))

    markers = []
    figures = []
    for class_num, data in enumerate(figure['data']):
        if split_num==0:
            reference = 0
        else:
            reference = np.round(data["y"][split_num-1],3)

        
        inicio = class_num/(len(figure['data']))
        fin = (class_num+1)/(len(figure['data']))
        
        figures.append(go.Indicator(
                    mode = "number+delta",
                    value = np.round(data["y"][split_num],3),
                    title = {"text": f"{data['name']}",  "font":{"size":20}},
                    number={"font":{"size":22}},
                    delta = {'reference': reference, 'relative': False, "font":{"size":17}},
                    domain = {'x': [inicio, fin], 'y': [0, 0.5]}))

        markers.append((inicio+fin)/2)


    fig = go.Figure()
    scatter = go.Scatter(
            x=markers, 
            y=[1 for m in markers], 
            mode='markers',
            marker = dict(size=120, 
                          opacity=0.5,
                          color = px.colors.qualitative.Plotly[2:],
                          #colorscale=px.colors.qualitative.Plotly[2:]
                          ),
            selectedpoints=selected_points)
    
    #color=clases, color_discrete_sequence=px.colors.qualitative.Plotly[2:],
    fig.add_trace(scatter)

    fig.update_layout(#shapes = circles+circles_white,
                      margin=dict(l=50, r=50, t=0, b=0),
                      height=100,
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      xaxis =  {                                     
                              'showgrid': False,
                              'showticklabels': False,
                                      },
                      yaxis = {                              
                              'showgrid': False,
                              'showticklabels': False,
                              },
                      xaxis_title="", 
                      showlegend=False,
                      clickmode='event+select')

    fig.update_xaxes(range=[0, 1], fixedrange=True)
    fig.update_yaxes(range=[0, 1], fixedrange=True)



    fig.add_traces(figures)

    return dcc.Graph(figure=fig, id='incrementos_clases_fig', config={'displayModeBar': False})


def update_text_children(value=None, min=None, max=None, step=None, division_texto=None, probs=[], clases = [], texto = ""):
    assert(value is not None and min is not None and  max is not None and step is not None and division_texto is not None)

    rango = np.linspace(min, max, int(np.round((max-min)/step))+1)[1:] # El 0 está contenido en el slider y por eso hay que restarlo
    
    value_arr = np.array([value for i in rango])
    
    split_num = np.argmin(abs(rango-value_arr))

  
    if division_texto=='phrases':
        patron_split = split_patterns.FRASES.value
    elif division_texto=='words':
        patron_split = split_patterns.PALABRAS.value

    text_splitted = split_text(patron_split, texto)

    if probs==[]:
        probs = [0 for i in range(split_num+1)]
    else:
        probs = probs[:split_num+1]


    children=[]

    # Strong
    last_prob = 0
    for i, prob in enumerate(probs):
        r,g,b = get_rgb_atribucion(prob-last_prob)
        final_color = f'rgb({r}, {g}, {b})'

        last_prob = prob

        decoration = "none" if i!=split_num else "underline"
        children.append(html.Strong(text_splitted[i],
                                    style={'background-color':final_color,
                                           "text-decoration":f"{decoration}",
                                           'whiteSpace': 'pre-wrap'})
        
                    )

    
    for i in range(split_num+1, len(text_splitted)):
        children.append(html.Span(text_splitted[i],
                                  style={'background-color':'rgb(255,255,255)','color':'gray','whiteSpace': 'pre-wrap'})
                )  
    

    return children


def update_barchart(value, min, max, step, figure, clases):
    score = [0 for i in clases]
    
    rango = np.linspace(min, max, int(np.round((max-min)/step))+1)[1:] # El 0 está contenido en el slider y por eso hay que restarlo
    
    value_arr = np.array([value for i in rango])
    
    split_num = np.argmin(abs(rango-value_arr))
    

    for i, data in enumerate(figure['data']):
        score[i] =  data['y'][split_num]


    fig = horizontal_bar_chart(score, clases)

    fig.update_layout(
        margin=dict(l=200, r=200, t=0, b=0))

    return fig










def layout():
    
    dic, idx = load_json_ejemplos(1, path_json)
    fig_inicial, _ = explain_evolucion(dic['texto'][idx], np.array(dic['clases'][idx]), splitter=split_patterns.FRASES.value)


    return html.Div([
            
            html.Div(
                [
                    dbc.RadioItems(
                        id="ejemplos",
                        className="btn-group",
                        inputClassName="btn-check",
                        labelClassName="btn btn-outline-primary",
                        labelCheckedClassName="active",
                        options=[
                            {"label": "Medicine 1", "value": 1},
                            {"label": "Medicine 2", "value": 2},
                            {"label": "Medicine 3", "value": 3},
                            {"label": "News", "value": 4},
                        ],
                        value=1,
                    )
                ],
                className="radio-group",
            ),

            dcc.Dropdown(
                        ['words', 'phrases'],
                        'phrases',
                        id='division_texto'
                    ),

            html.Div(html.H3('SEQUENTIAL EVOLUTION OF MODEL DECISION'),
                    style={'textAlign':'center'}),


            dcc.Graph(id="graph", 
                      figure = fig_inicial),



            html.Div(id='processed_text_slider_div', 
                    children=[dcc.Slider(
                        0,
                        100,
                        100/len(split_text(split_patterns.FRASES.value, dic['texto'][idx])),
                        id = 'processed_text_slider',
                        marks=None, 
                        value=0,
                    
                    ),
                    html.H2( children=f'Processed: 0% text', id='processed_text_slider_H2',style={'textAlign':'center'})
                    ],
                    style={'padding': '0px 200px 0px 200px'}),


            html.Div(id="incrementos_clases", 
                    children= dcc.Graph(id='incrementos_clases_fig', config={'displayModeBar': False}),#update_increments(50, 0, 100, 100/len(split_text(split_patterns.FRASES.value, dic['texto'][idx])), fig_inicial),
                    style={'textAlign':'center'}               
            ),

            dcc.Graph(id="barras",
                    figure= horizontal_bar_chart([1], [''])),

            html.Div(id='texto',
                    children="",
                    style={'textAlign': 'center',
                        'padding': '0px 100px 0px 100px',
                        "height": "300px",
                        'font-size':20,
                        "overflowY": "auto"
                        }
                    ),

            


        ],style={'padding': '0px 20px 0px 20px', 'background-color': 'white', 'color': 'black'})


    



@callback(
    Output('graph', 'figure'),
    Output('processed_text_slider_div', 'children'),
    Input('division_texto','value'),
    Input('ejemplos','value'))
def change_text_division(division_texto, ejemplo):
    dic, idx = load_json_ejemplos(ejemplo, path_json)
   
    if division_texto=='phrases':
        patron_split = split_patterns.FRASES.value
    elif division_texto=='words':
        patron_split = split_patterns.PALABRAS.value

     
    fig, _ = explain_evolucion(dic['texto'][idx], np.array(dic['clases'][idx]), splitter=patron_split)

    slider=[dcc.Slider(
                0,
                100,
                100/len(split_text(patron_split, dic['texto'][idx])),
                id = 'processed_text_slider',
                marks=None,
                value=0,
            
            ),
            html.H2( children=f'Processed: 0% text', id='processed_text_slider_H2',style={'textAlign':'center'})
            ]

    return fig, slider



@callback(
    Output('processed_text_slider','value'),
    Input('graph', 'hoverData'),
    Input('division_texto','value'),
    Input('ejemplos','value'))
def update_processed_text_slider(hoverdata, division_texto, ejemplo):
    dic, idx = load_json_ejemplos(ejemplo, path_json)
    
    if division_texto=='phrases':
        patron_split = split_patterns.FRASES.value
    elif division_texto=='words':
        patron_split = split_patterns.PALABRAS.value

    text_splitted = split_text(patron_split, dic['texto'][idx])
    
    if hoverdata is not None:
        split_num = hoverdata["points"][0]["pointNumber"]
    else:
        split_num = 0

    n = len(text_splitted)
    
    return  (split_num+1)*100/(n)



@callback(
    Output('processed_text_slider_H2','children'),
    Output('incrementos_clases','children'),
    Output("texto", "children"),
    Output("barras", "figure"),
    Input('incrementos_clases_fig', 'selectedData'),
    Input('processed_text_slider', 'value'),
    Input('processed_text_slider', 'min'),
    Input('processed_text_slider', 'max'),
    Input('processed_text_slider', 'step'),
    Input("division_texto", "value"),
    #Input('graph', 'hoverData'),
    Input('graph','figure'),
    Input('ejemplos','value'))
def update_processed_tex(selectedData, value, min, max, step, division_texto, figure, ejemplo):
    processed_text_slider_H2_children = f'Processed: {np.round(value,1)}% text'
    
    dic, idx = load_json_ejemplos(ejemplo, path_json)

    if selectedData is not None:
        selected_point = selectedData['points'][0]['pointNumber']

        incrementos_clases_children = update_increments(value, min, max, step, figure, [selected_point])
        updated_text_children = update_text_children(value, min, max, step, division_texto, probs=figure['data'][selected_point]['y'], clases =  np.array(dic['clases'][idx]), texto=dic['texto'][idx])
    else:
        incrementos_clases_children = update_increments(value, min, max, step, figure)
        updated_text_children = update_text_children(value, min, max, step, division_texto, clases =  np.array(dic['clases'][idx]), texto=dic['texto'][idx])

    bar_chart = update_barchart(value, min, max, step, figure, np.array(dic['clases'][idx]))

    return processed_text_slider_H2_children, incrementos_clases_children, updated_text_children, bar_chart
