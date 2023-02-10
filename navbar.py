from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.BOOTSTRAP, 'seg-style.css']
text_color = {"dark": "#95969A", "light": "#595959"}
card_color = {"dark": "#2D3038", "light": "#FFFFFF"}


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "30px",
    "left": 0,
    "bottom": 0,
    "width": "400px",
    "padding": "2rem 1rem",
    "background-color": "#769290",
    'color' : '#000000',
}


# Header
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H4('Prevendo Status do Cliente', style = {'margin-left' : 45}),
                                ],
                                id = 'app-title',
                                style = {
                                    'color' : 'white',
                                }
                            )
                        ],
                        width = 6,
                        md = True,
                        style = {'width' : '1000px', 'text-align' : 'left'},
                    ),

                    dbc.Col(
                        [
                            html.Div(
                                [
                                    dbc.Button('GitHub', color = 'success', className = 'me-1',
                                    href = 'https://github.com/tharikf?tab=repositories', target = '_blank'),
                                    dbc.Button('Jupyter Notebook', color = 'success', className = 'me-1',
                                    href = 'https://nbviewer.org/github/tharikf/Prevendo_Clientes_Inativos/blob/main/Notebook_Prevendo_Clientes_Inativos.ipynb',
                                    target = '_blank'),
                                    dbc.Button('Base de Dados', color = 'success', className = 'me-1',
                                    href = 'https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers', target = '_blank'),
                                ],
                                id = 'app-descricao',
                                style = {
                                    'color' : 'white',
                                },
                            )
                        ],
                        width = 6,
                        md = True,
                        style = {'width' : '1900px', 'text-align' : 'right', 'margin-top' : -4},
                    ),
                ],
                #className = 'g-0',
                style = {'height' : '30px', 'width' : '1920px', 'left' : 0},
            ),
        ],
        fluid = True, style = {'height' : '30px', 'width' : '1920px'},
    ),
    color = '#769290',
    sticky = 'top',
    style = {'left' : 0, 'width' : '1920px'},
)


# Side-Bar
sidebar = html.Div(
    [
        html.P('Gerar cliente automaticamente!', style = {'textAlign': 'center', 'font-size' : 20, 'color' : '#FFFFFF'}),
        dbc.Row(
            [
                dbc.Col(dbc.Button('Gerar Valores Automaticamente', id = 'id-botao', color = 'danger'), style = {'textAlign': 'center'})
            ]
        ),
        html.Br(),
        html.P('Ou insira as características do cliente!', style = {'textAlign': 'center', 'font-size' : 18, 'color' : '#FFFFFF'}),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Escolaridade", id = 'label-escolaridade'),
                        dcc.Dropdown(
                            id = "id-escolaridade", style = {"width" : "175px", "color" : "#010451", 'textAlign': 'left'},
                            options = [{"label" : "Uneducated", "value" : "Uneducated"}, {"label" : "High School", "value" : "High School"},
                                        {"label" : "College", "value" : "College"}, {"label" : "Graduate", "value" : "Graduate"},
                                        {"label" : "Post-Graduate", "value" : "Post-Graduate"}, {"label" : "Doctorate", "value" : "Doctorate"}],
                        ),
                        dbc.Tooltip('Escolaridade do cliente.', target = 'id-escolaridade'),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Sexo"),
                        dcc.Dropdown(
                            id = "id-sexo", style = {"width" : "175px", "color" : "#010451", 'textAlign' : 'left'},
                            options = [{"label" : "Feminino", "value" : "Feminino"}, {"label" : "Masculino", "value" : "Masculino"}],
                        ),
                        dbc.Tooltip('Sexo do cliente.', target = 'id-sexo'),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Categoria de Renda"),
                        dcc.Dropdown(
                            id = "id-renda", style = {"width" : "175px", "color" : "#010451", 'textAlign': 'left'},
                            options = [{"label" : "Menos que 40K", "value" : "Menos que 40K"},
                                        {"label" : "Entre 40K e 60K", "value" : "Entre 40K e 60K"},
                                        {"label" : "Entre 60K e 80K", "value" : "Entre 60K e 80K"},
                                        {"label" : "Entre 80K e 120K", "value" : "Entre 80K e 120K"},
                                        {"label" : "Mais que 120K", "value" : "Mais que 120K"}],
                        ),
                        dbc.Tooltip('Categoria de renda do cliente.', target = "id-renda"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Dependentes"),
                        dbc.Input(id = "id-dependentes", placeholder = 'Entre 0 e 5', type = "number", min = 0, max = 5, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Número de dependentes do cliente.', target = "id-dependentes"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Idade"),
                        dbc.Input(id = "id-idade", placeholder = 'Entre 18 e 85', type = "number", min = 18, max = 85, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Idade do cliente.', target = "id-idade"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Limite do Cartão"),
                        dbc.Input(id = "id-limite", placeholder = 'Entre 1.5K e 35K', type = "number", min = 1500, max = 35000, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Limite do cartão do cliente.', target = "id-limite"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Crédito Aberto"),
                        dbc.Input(id = "id-credito-aberto", placeholder = 'Entre 0 e 35K', type = "number", min = 0, max = 35000, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Total de crédito aberto ao cliente nos últimos 12 meses.', target = "id-credito-aberto"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Utilização do Cartão"),
                        dbc.Input(id = "id-taxa-utilizacao", placeholder = 'Entre 0 e 0,99', type = "number", min = 0, max = 0.99, step = 0.01,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Taxa de utilização do cartão pelo cliente.', target = "id-taxa-utilizacao"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Produtos do Banco"),
                        dbc.Input(id = "id-contato-banco", placeholder = 'Entre 1 e 6', type = "number", min = 1, max = 6, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Quantidade de produtos do banco que o cliente possui.', target = "id-contato-banco"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Saldo Rotativo"),
                        dbc.Input(id = "id-saldo-rotativo", placeholder = 'Entre 0 e 2500', type = "number", min = 0, max = 2500, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Saldo rotativo do cliente.', target = "id-saldo-rotativo"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Volume de Transações"),
                        dbc.Input(id = "id-transacoes", placeholder = 'Entre 0 e 140', type = "number", min = 0, max = 140, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Total de transações realizadas pelo cliente nos últimos 12 meses', target = "id-transacoes"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Valor Transacionado"),
                        dbc.Input(id = "id-transacionado", placeholder = 'Entre 0 e 20K', type = "number", min = 0, max = 20000, step = 1,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Valor total transacionado pelo cliente nos últimos 12 meses', target = "id-transacionado"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Variação no Volume de Transações"),
                        dbc.Input(id = "id-variacao-volume", placeholder = 'Entre 0 e 3,75', type = "number", min = 0.0, max = 3.75, step = 0.01,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Variação no volume transacionado pelo cliente entre o primeiro e o quarto trimestre',
                                    target = "id-variacao-volume"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),

                dbc.Col(
                    [
                        dbc.Label("Variação no Valor Transacionado"),
                        dbc.Input(id = "id-variacao-valor", placeholder = 'Entre 0 e 3,50', type = "number", min = 0.0, max = 3.50, step = 0.01,
                                    style = {'textAlign': 'center'}),
                        dbc.Tooltip('Variação no valor total transacionado pelo cliente entre o primeiro e o quarto trimestre',
                                    target = "id-variacao-valor"),
                    ], style = {"width" : "175px", 'textAlign': 'center'},
                ),
            ], style = {'height' : '60px', 'color' : '#FFFFFF'},
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button('Clique Após Preencher os Valores', id = 'id-preenchi', color = 'danger'),
                        html.A(dbc.Button('Limpar Valores', color = 'warning', style = {'margin-top' : 4}), href = '/'),
                    ], style = {'textAlign': 'center', 'color' : '#FFFFFF'},
                ),
            ],
        )
    ],
    style = SIDEBAR_STYLE,
)








def Navbar():

    layout = html.Div(
        [
            header,
            sidebar,
        ]
    )

    return layout



