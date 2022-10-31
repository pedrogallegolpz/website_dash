import json
import re

import pandas as pd
import numpy as np


import plotly.express as px

import plotly.graph_objects as go



from enum import Enum


class split_patterns(Enum):
    PALABRAS = '\s+'
    FRASES = '[\.\;\n]+(?!\d)|[\.\;\n]+$'

def split_string_of_len(string, length, pattern='\W+'):
    found = re.finditer(pattern, string)
    count = 1
    s = []
    last_end = 0
    for match in found:
        if match.start()>=count*length:
            s.append(string[last_end:last_try_start])
            last_end = last_try_end
            count+=1
        
        last_try_start = match.start()
        last_try_end = match.end()
        
    s.append(string[last_end:])
    return s



def get_rgb_atribucion(curr_peso):
    aux = int(255 - (abs(curr_peso))*255)
    if curr_peso>0:
        # Color verde
        r, g, b = aux, 255, aux            
    else:
        # color rojo
        r, g, b = 255, aux, aux  

    return r, g, b


            
    
def plot_plotly_scores(scores, text_splitted=None, clases=None, title ="", colores = None):
    if colores == None:
        colores = px.colors.qualitative.Plotly
    
    if clases is None:
        clases = np.array([f'clase {i}' for i in range(scores.shape[0])])
    
    df = pd.DataFrame(scores.T, columns=clases, index=100*np.linspace(0, 1, scores.shape[1]+1)[1:])
    
    if text_splitted is not None:
        text_splitted_processed = [f if len(f)<=63 else split_string_of_len(f,30)[0]+' (...) '+split_string_of_len(f,30)[-1] for f in text_splitted]
        df['text_splitted']=text_splitted_processed
        
        
    fig = px.line(df, 
                  y=clases,
                  custom_data=['text_splitted'],
                  color_discrete_sequence=colores)
        
    fig.update_traces(mode="markers+lines", hovertemplate=None)
    fig.update_layout(hovermode='x unified', 
                      hoverlabel_bgcolor='#FFFFFF',
                      title =title,
                      title_font_family="Arial",
                      title_font_size=30,
                      title_x=0.5,
                      height=350,
                      legend_title="Otras clases"
                    )
    
    fig.update_xaxes(title='% processed text')
    fig.update_yaxes(title='probability')
    
    if text_splitted is not None:
        fig.update_traces(hovertemplate="<br>".join([
                        "%{customdata[0]}",
                        "Prob: %{y:.3f}"
                    ]))
    
    return fig
    

    

    
    
    
def horizontal_bar_chart(x, clases, colors=px.colors.qualitative.Plotly[2:]):

    fig = go.Figure()

        
    for i in range(len(x)):
        fig.add_trace(go.Bar(
            x=[x[i]], y=[0],
            orientation='h',
            name=clases[i],
            width = 1/2,
            marker=dict(
                color=colors[i]
            )
        ))

    
    fig.update_layout(        
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0,1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False
        ),
        barmode='stack',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=100,
        margin=dict(l=200, r=200, t=0, b=0),
        showlegend=False,
    )

    
     
    annotations = []

    percentage_label_umbral = 0.05
    space = 0
    for xd in x:
        # labeling the rest of percentages for each bar (x_axis)
        if xd>percentage_label_umbral:
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd/2), y=0,
                                    text=f'{xd:.3f}',
                                    font=dict(family='Arial', size=14,
                                                color='rgb(248, 248, 255)'),
                                    showarrow=False))
        
        space += xd

    fig.update_layout(annotations=annotations)
    
            
        
    return fig



def split_text(splitter, text):
    found = list(re.finditer(splitter, text))
    last_end = 0
    
    text_splitted=[]
    i=-1
    while last_end<len(text):
        i+=1        
        if i<len(found):
            match = found[i]
            match_end = match.end()
        else:
            match_end = len(text)
            
        # Vemos si el nuevo texto que se va a añadir contiene una frase
        text_added = text[last_end:match_end]
        if re.sub(splitter, '', text_added).strip()=='':
            # saltamos a la siguiente porque no contiene ninguna frase
            if match_end == len(text):
                break
            else:
                continue
        text_splitted.append(text_added)
        
        # Guardamos los nuevos datos
        last_end = match_end

    return text_splitted 


def explain_evolucion(text, clases, splitter='[\.\;\n]+(?!\d)|[\.\;\n]+$', colores = px.colors.qualitative.Plotly[2:]):    
    path_json = './assets/textos.json'
    
    with open(path_json,'r') as f:
        dic = json.load(f)
    
    scores = np.array(dic[splitter][np.where(np.array(dic['texto'])==text)[0][0]])
    
   
    text_splitted = split_text(splitter, text)

        
    fig = plot_plotly_scores(
                            scores.T,
                            text_splitted=text_splitted, 
                            clases=np.array(clases), 
                            colores=colores,
                            title=''   
                            )

        

    return fig, text_splitted
    
