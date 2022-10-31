import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3) # order means the order in the tab on the dashboard

green_text = {'color': 'green'}

def layout():
    return dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Markdown("# Pedro Gallego López", className="mt-3·"), # in className, "mt" means margin top, changing the number change the margin
                    dcc.Markdown("### Mathematician and Computer Scientist"), 
                    dcc.Markdown("### (AI specialist)", className="mb-5"), # "mb" means margin bottom, changing the number change the margin
                    dcc.Markdown("###  Personal info", style={'color':'gray'}),
                    
                    dcc.Markdown("Address", style=green_text),
                    dcc.Markdown("Currently: _Dublin, Ireland_ "),

                    dcc.Markdown("Phone number", style=green_text),
                    dcc.Markdown("+34 635 088 883 "),

                    dcc.Markdown("Email", style=green_text),
                    dcc.Markdown("pedrogallegolop@gmail.com"),

                    dcc.Markdown("Linkedin", style=green_text),
                    dcc.Markdown("[Pedro Gallego López](https://www.linkedin.com/in/pedro-gallego-l%C3%B3pez-414a14173)"),
                    
                    dcc.Markdown("GitHub", style=green_text),
                    dcc.Markdown("[github.com/pedrogallegolpz](https://github.com/pedrogallegolpz)"),
                    
                ],
                width={'size':6, 'offset':2}
            )
        ],
        justify='center',
    )