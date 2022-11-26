from dash import Dash, dcc, html, ctx
from dash.dependencies import Input, Output, State
import dash
import dash_bootstrap_components as dbc
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import pickle
import time
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

ESTRUTURA_STYLE = {
    "position": "fixed",
    "top": "45px",
    "left": "412px",
    "bottom": 0,
    "width": "1508px",
    "height" : "885px",
    "background-color": '#FFFFFF',
    #"background-color": '#E2F5F4',
}

pil_image = Image.open("components/random_forest_diagram.png")


app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags = [{'name': 'viewport', "content" : "width=device-width, initial-scale=0.19, maximum-scale=5, minimum-scale=0.1, device-height=50"}],
                suppress_callback_exceptions=True)

           
server = app.server

import navbar
from navbar import *
nav = navbar.Navbar()


# Estrutura
estrutura = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H2('Descrição da Aplicação', style = {'text-align' : 'center'}),
                                html.P('''
                                Essa aplicação pretende realizar a classificação dos clientes de um banco entre ativos e inativos. 
                                A base de dados de treinamento foi extraída do site Kaggle e pode ser consultada no botão no canto 
                                superior direito. Foi realizada uma análise exploratória do conjunto de dados e foram testados diversos 
                                algoritmos de aprendizado de máquina supervisionado com a tarefa de classificação. Dentre os algoritmos 
                                que obtiveram os melhores resultados, optou-se por utilizar o Random Forest na aplicação. Além disso, 
                                foi realizada uma seleção de variáveis mais relevantes, também com Random Forest, para simplificar a aplicação. 
                                É possível observar todo o trabalho do projeto, desde a extração e manipulação dos dados até a etapa de modelagem, 
                                clicando no botão no canto superior direito que indica o Jupyter Notebook. É possível realizar previsões 
                                indicando cada um dos valores para as variáveis na barra à esquerda ou simplesmente clicando no botão 
                                para gerar valores para todas as variáveis aleatoriamente.
                                        ''', style = {'text-align' : 'justify'})
                            ]
                        )
                    ], style = {'width' : '1508px', 'height' : '180px', 'background-color' : '#FFFFFF'},
                ),
            ], style = {'width' : '1508px', 'height' : '180px', 'background-color' : '#FFFFFF'},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                    html.Hr(),
                    ]       
                )
            ], style = {'width' : '1508px', 'background-color' : '#FFFFFF'},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.Row(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                            html.H3('Características geradas', style = {'margin-left' : 150}),
                                                            ], width = 10,
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Button('Reset', color = 'warning',
                                                                            id = 'id-reset', style = {'textAlign' : 'right'}),
                                                            ], width = 2,
                                                        )
                                                    ], style = {'margin-top' : -10},
                                                ),
                                                
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Escolaridade',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-escolaridade'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Sexo',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-sexo'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Idade',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-idade'),
                                                            ]
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Nº de Dependentes',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-dependentes'),
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Categoria de Renda',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-renda'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Limite do Cartão',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-limite'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Crédito Aberto',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-credito-aberto'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Utilização do Cartão',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-util-cartao'),
                                                            ],
                                                        ),
                                                    ]
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Produtos do Banco',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-produtos'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Saldo Rotativo',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-rotativo'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Volume de Transações',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-volume-transacoes'),
                                                            ],
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Valor Transacionado',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-valor-transacionado'),
                                                            ],
                                                        ),
                                                    ]
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Variação no Volume de Transações',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-variacao-volume'),
                                                            ]
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card('Variação no Valor Transacionado',
                                                                            style = {'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-variacao-valor'),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ], style = {'width' : '754px', 'height' : '360px', 'textAlign' : 'center'},
                                        )
                                    ],
                                ),
                                dbc.Row(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                dbc.Card('Previsão de Classe',
                                                                style = {'height' : '40px', 'font-size' : '24px',
                                                                        'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-classe', style = {'font-size' : '24px'}),
                                                            ],
                                                        ),
                                                    ], style = {'height' : '100px'},
                                                ),
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                dbc.Card('Probabilidade das Classes',
                                                                style = {'height' : '40px', 'font-size' : '24px',
                                                                        'background-color' : '#515252', 'color' : '#FFFFFF'}),
                                                                dbc.CardBody(id = 'output-ativo', style = {'font-size' : '18px'}),
                                                                dbc.CardBody(id = 'output-inativo', style = {'font-size' : '18px'}),
                                                            ]
                                                        ),
                                                    ], style = {'height' : '210px'},
                                                ),
                                            ],  style = {'width' : '754px', 'height' : '310px', 'text-align' : 'center'},
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ], style = {'width' : '754px', 'height' : '640px', 'background-color' : '#FFFFFF'},
                ),

                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H2('Explicação do Algoritmo', style = {'text-align' : 'center'}),
                                html.Hr(),
                                html.P('''
                                Random Forest é um algoritmo de aprendizado de máquina supervisionado para problemas 
                                de classificação e regressão. Ele utiliza o conceito de árvore de decisão mas expandindo 
                                para um número arbitrário de árvores de decisão, em contrapartida ao algoritmo Decision 
                                Trees que utiliza apenas uma árvore para realizar as previsões. Cada árvore de decisão 
                                realizará uma previsão e o resultado de todas as árvores é levando em consideração para 
                                fazer a previsão final, que pode ser obtida por uma regra, como por exemplo, a regra da maioria 
                                em que o resultado com maior número de votos determina o resultado do modelo.
                                              ''', style = {'text-align' : 'justify'}),
                                html.Img(src = pil_image, style = {'height' : '410px', 'width' : '730px'}),
                            ]
                        ),
                    ], style = {'width' : '754px', 'height' : '640px', 'background-color' : '#FFFFFF'},
                ),
            ], style = {'width' : '1508px', 'height' : '675px', 'background-color' : '#FFFFFF'},
        ),
    ], style = ESTRUTURA_STYLE,
)

# Importando modelo treinado e o scaler
with open('modelo_treinado.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('scaler_treinado.pkl', 'rb') as f:
    scaler = pickle.load(f)



# Define the index page layout
app.layout = html.Div(
    [
        nav,
        estrutura,
    ]
)

selecao_colunas = ['total_trans_ct', 'total_trans_amt', 'total_revolving_bal', 'total_ct_change_Q4_Q1',
                    'total_amt_change_Q4_Q1', 'avg_utilization_ratio', 'total_relationship_count', 'avg_open_to_buy',
                    'age', 'credit_limit', 'gender', 'dependent_count', 'education_level', 'income_category']
### Callbacks
@app.callback(
    Output('output-classe', 'children'),
    Output('output-ativo', 'children'),
    Output('output-inativo', 'children'),
    Output('output-volume-transacoes', 'children'),
    Output('output-valor-transacionado', 'children'),
    Output('output-rotativo', 'children'),
    Output('output-variacao-volume', 'children'),
    Output('output-variacao-valor', 'children'),
    Output('output-util-cartao', 'children'),
    Output('output-produtos', 'children'),
    Output('output-credito-aberto', 'children'),
    Output('output-idade', 'children'),
    Output('output-limite', 'children'),
    Output('output-sexo', 'children'),
    Output('output-dependentes', 'children'),
    Output('output-escolaridade', 'children'),
    Output('output-renda', 'children'),
    inputs = {
        "all_inputs" : {
            "btn1" : Input('id-botao', 'n_clicks'),
            "btn2" : Input('id-reset', 'n_clicks'),
            "btn3" : Input('id-preenchi', 'n_clicks'),
            "input0" : Input("id-transacoes", "value"),
            "input1" : Input("id-transacionado", "value"),
            "input2" : Input("id-saldo-rotativo", "value"),
            "input3" : Input("id-variacao-volume", "value"),
            "input4" : Input("id-variacao-valor", "value"),
            "input5" : Input("id-taxa-utilizacao", "value"),
            "input6" : Input("id-contato-banco", "value"),
            "input7" : Input("id-credito-aberto", "value"),
            "input8" : Input("id-idade", "value"),
            "input9" : Input("id-limite", "value"),
            "input10" : Input("id-sexo", "value"),
            "input11" : Input("id-dependentes", "value"),
            "input12" : Input("id-escolaridade", "value"),
            "input13" : Input("id-renda", "value"),
        }
    },
)

def update_layout(all_inputs):
    c = ctx.args_grouping.all_inputs
    global vetor
    vetor = None
    if c.btn2.triggered:
        return '','','','', '', '', '', '', '', '', '', '', '', '', '', '', ''
    elif c.btn1.triggered:
        vetor = [np.random.randint(0, 140), np.random.uniform(0, 20000), np.random.uniform(0, 2500),
                np.random.uniform(0, 3.75), np.random.uniform(0, 3.50), np.random.uniform(0, 1),
                np.random.randint(1, 7), np.random.uniform(0, 35000), np.random.randint(18, 85),
                np.random.uniform(1500, 35000), np.random.randint(0, 2), np.random.randint(0, 6), 
                np.random.randint(0, 6), np.random.randint(0, 5)]
        
        df = [round(item, 2) for item in vetor]
    
        # Condicao Sexo
        if df[10] == 1:
            df[10] = 'Masculino'
        else:
            df[10] = 'Feminino'

        # Condicao Escolaridade
        if df[12] == 0:
            df[12] = 'College',
        elif df[12] == 1:
            df[12] = 'Doctorate',
        elif df[12] == 2:
            df[12] = 'Graduate',
        elif df[12] == 3:
            df[12] = 'High School',
        elif df[12] == 4:
            df[12] = 'Post-Graduate',
        else:
            df[12] = 'Uneducated'

        # Faixa de Renda
        if df[13] == 0:
            df[13] = 'Mais que 120K'
        elif df[13] == 1:
            df[13] = 'Entre 40K e 60K'
        elif df[13] == 2:
            df[13] = 'Entre 60K e 80K'
        elif df[13] == 3:
            df[13] = 'Entre 80K e 120K'
        elif df[13] == 4:
            df[13] = 'Menos que 40K'
        else:
            pass
        
        
        vetora = vetor
        vetora = np.array(vetora)
        vetora = vetora.reshape(1, -1)
        dfa = pd.DataFrame(vetora, columns = selecao_colunas)

        colunas_norm = ['age', 'credit_limit', 'total_revolving_bal', 'avg_open_to_buy',
                        'total_amt_change_Q4_Q1', 'total_trans_amt', 'total_trans_ct', 'total_ct_change_Q4_Q1',
                        'avg_utilization_ratio']

        dfa[colunas_norm] = scaler.transform(dfa[colunas_norm])

        vetora = np.array(dfa)
        vetora = vetora.reshape(1, -1)
        modelo.predict(vetora)
        classe = modelo.predict(vetora)
        classe_str = ''
        if (classe == 0):
            classe_str = 'Cliente Ativo'
        else:
            classe_str = 'Cliente Inativo'

        proba_ativo = modelo.predict_proba(vetora)[0][0]
        proba_inativo = modelo.predict_proba(vetora)[0][1]
        
        return classe_str, 'A probabilidade do cliente ser ativo é de: {:.2%}'.format(proba_ativo), 'A probabilidade do cliente ser inativo é de: {:.2%}'.format(proba_inativo), df[0], 'R${:,.2f}'.format(df[1]), 'R${:,.2f}'.format(df[2]), df[3], df[4], df[5], df[6], 'R${:,.2f}'.format(df[7]), df[8], 'R${:,.2f}'.format(df[9]), df[10], df[11], df[12], df[13]
    
    elif c.btn3.triggered:
        #input_10 (sexo), input_12 (escolaridade), input_13 (renda)
        input_10 = 0
        input_12 = 0
        input_13 = 0

        # Condicao sexo
        if (c.input10.value == 'Masculino'):
            input_10 = 1
        else:
            input_10 = 0
        
        # Condicao Escolaridade
        if (c.input12.value == 'College'):
            input_11 = 0
        elif (c.input12.value == 'Doctorate'):
            input_11 = 1
        elif (c.input12.value == 'Graduate'):
            input_11 = 2
        elif (c.input12.value == 'High School'):
            input_11 = 3
        elif (c.input12.value == 'Post-Graduate'):
            input_11 = 4
        else:
            input_11 = 5

        # Faixa de Renda
        if (c.input13.value == 'Mais que 120K'):
            input_13 = 0
        elif (c.input13.value == 'Entre 40K e 60K'):
            input_13 = 1
        elif (c.input13.value == 'Entre 60K e 80K'):
            input_13 = 2
        elif (c.input13.value == 'Entre 80K e 120K'):
            input_13 = 3
        else:
            input_13 = 4
        
        vetor_final = [c.input0.value, c.input1.value, c.input2.value, c.input3.value, c.input4.value, c.input5.value,
                       c.input6.value, c.input7.value, c.input8.value, c.input9.value, input_10, c.input11.value,
                       input_12, input_13]
        vetor_final = np.array(vetor_final)
        vetor_final = vetor_final.reshape(1, -1)
        dfb = pd.DataFrame(vetor_final, columns = selecao_colunas)

        colunas_norm = ['age', 'credit_limit', 'total_revolving_bal', 'avg_open_to_buy',
                        'total_amt_change_Q4_Q1', 'total_trans_amt', 'total_trans_ct', 'total_ct_change_Q4_Q1',
                        'avg_utilization_ratio']
        
        dfb[colunas_norm] = scaler.transform(dfb[colunas_norm])
        vetor_final = np.array(dfb)
        vetor_final = vetor_final.reshape(1, -1)
        modelo.predict(vetor_final)
        classe = modelo.predict(vetor_final)
        classe_str = ''
        if (classe == 0):
            classe_str = 'Cliente Ativo'
        else:
            classe_str = 'Cliente Inativo'
        
        proba_ativo = modelo.predict_proba(vetor_final)[0][0]
        proba_inativo = modelo.predict_proba(vetor_final)[0][1]
        return classe_str, 'A probabilidade do cliente ser ativo é de: {:.2%}'.format(proba_ativo), 'A probabilidade do cliente ser inativo é de: {:.2%}'.format(proba_inativo), c.input0.value, 'R${:,.2f}'.format(c.input1.value), 'R${:,.2f}'.format(c.input2.value), c.input3.value, c.input4.value, c.input5.value,  c.input6.value, 'R${:,.2f}'.format(c.input7.value), c.input8.value, 'R${:,.2f}'.format(c.input9.value), c.input10.value, c.input11.value, c.input12.value, c.input13.value




# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug = False, port=8000, host='0.0.0.0')
