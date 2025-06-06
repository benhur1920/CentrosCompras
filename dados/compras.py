import pandas as pd
import unidecode

def carregando_as_urls(opcao):
    if opcao == 'mercado':
        url = 'http://dados.recife.pe.gov.br/dataset/eeee4ac5-d0e0-490b-aac0-490a6de74e07/resource/40d97dcb-4a14-4365-bced-8555998a498d/download/mercadospublicos.csv'
    elif opcao == 'feira':
        url = 'http://dados.recife.pe.gov.br/dataset/eeee4ac5-d0e0-490b-aac0-490a6de74e07/resource/dc6b3d07-3124-453d-b11e-72364cced7aa/download/feiraslivres.csv'
    else:
        url = 'http://dados.recife.pe.gov.br/dataset/eeee4ac5-d0e0-490b-aac0-490a6de74e07/resource/81f406de-8468-4bb9-b038-0956d6684acd/download/shopping.csv'
    return url


def criando_as_colunas_para_adequar_o_conjunto_de_dados(df, nome_coluna, nome_identificador):
    df[nome_coluna] = nome_identificador
    return df

def ajustando_nome_das_feiras_livres(df):   
    # Criando um dicionário para as substituições
    substituicoes = {'Feira Água Fria': 'Agua Fria',
                 'Feira Dom Vital': 'Sao Jose',
                 'Feira de Beberibe': 'Beberibe',
                 'Feira Arruda':'Arruda',
                 'Feira Encruzilhada': 'Encruzilhada',
                 'Feira Alto do Deodato': 'Agua Fria',
                 'Feira Casa Amarela': 'Casa Amarela',
                 'Feira Nova Descoberta': 'Nova Descoberta',
                 'Feira Bomba Grande':'Cordeiro',
                 'Feira do Cordeiro':'Cordeiro',
                 'Feira da Várzea':'Varzea',
                 'Feira do Engenho do Meio':'Engenho do Meio',
                 'Feira de Areias':'Areias',
                 'Feira da Mustardinha':'Mustardinha',
                 'Feira de Afogados':'Afogados',
                 'Feira do Jordão':'Jordao',
                 'Feira do Ibura UR – 01':'Ibura'}

    # Aplicando as substituições
    df['bairro'] = df['Nome'].replace(substituicoes)
    return df

def concatenando_a_coluna_funcionamento_com_dias_e_horario(df):
    # Concatenando as colunas
    df['funcionamento'] = df['Dias'] + ' das ' + df['Horário']
    return df

def adicionando_o_texto_fixo_e_criando_uma_nova_coluna(df):
    df['funcionamento'] = 'Segunda a sábado das ' + df['funcionamento'] + ' e domingos das ' + df['funcionamentoDomingo']
    return df

def criando_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando(df, opcao):
    if opcao == 'mercado':
        df = df [['nome', 'Localização', 'bairro',  'Horário', 'Opção', 'latitude', 'longitude'
                       ]].rename(columns={'nome': 'Nome','Horário':'Funcionamento', 'latitude':'Latitude', 'longitude':'Longitude',
                                           'bairro':'Bairro'})
    elif opcao == 'feira':
        df  = df [['Nome', 'Localização', 'bairro', 'funcionamento', 'Latitude', 'Longitude','Opção']].rename(columns={
                                           'bairro':'Bairro', 'funcionamento':'Funcionamento'})
    else:
        df = df [['nome', 'logradouro', 'bairro',  'funcionamento', 'Opção', 'latitude', 'longitude'
                       ]].rename(columns={'logradouro': 'Localização', 'latitude':'Latitude', 'longitude':'Longitude',
                                          'nome':'Nome', 'bairro':'Bairro', 'funcionamento':'Funcionamento' })
        
    return df
def redefinir_os_indices_de_cada_DataFrame(df):
    df = df.reset_index(drop=True)
    return df

def concatenar_os_dataframes(compras, feiras, mercados):
    # Concatenar os DataFrames após alinhar as colunas
    df = pd.concat([compras, feiras, mercados], ignore_index=True)
    return df

def salvando_o_DataFrame_no_arquivo_CSV(df):
    df.to_csv('LocaisCompras.csv', sep=';',encoding='utf-8-sig', index=False)

def criar_a_coluna_Regiao(df):
    dicionario = {
        'Centro': [
            'Boa Vista', 'Cabanga', 'Coelhos', 'Ilha Do Leite', 'Ilha Joana Bezerra',
            'Paissandu', 'Recife', 'Santo Amaro', 'Santo Antônio', 'Soledade', 'São José'
        ],
        'Noroeste': [
            'Aflitos', 'Alto Do Mandu', 'Alto José Bonifácio', 'Alto José Do Pinho', 'Apipucos',
            'Brejo Da Guabiraba', 'Brejo De Beberibe', 'Casa Amarela', 'Casa Forte',
            'Córrego Do Jenipapo', 'Derby', 'Dois Irmãos', 'Espinheiro', 'Graças', 'Guabiraba',
            'Jaqueira', 'Macaxeira', 'Mangabeira', 'Monteiro', 'Morro Da Conceição',
            'Nova Descoberta', 'Parnamirim', 'Passarinho', 'Pau Ferro', 'Poço', 'Santana',
            'Sítio Dos Pintos', 'Tamarineira', 'Vasco Da Gama'
        ],
        'Norte': [
            'Alto Santa Terezinha', 'Arruda', 'Beberibe', 'Bomba Do Hemetério', 'Cajueiro',
            'Campina Do Barreto', 'Campo Grande', 'Dois Unidos', 'Encruzilhada', 'Fundão',
            'Hipódromo', 'Linha Do Tiro', 'Peixinhos', 'Ponto De Parada', 'Porto Da Madeira',
            'Rosarinho', 'Torreão', 'Água Fria'
        ],
        'Oeste': [
            'Caxangá', 'Cidade Universitária', 'Cordeiro', 'Engenho Do Meio',
            'Ilha Do Retiro', 'Iputinga', 'Madalena', 'Prado', 'Torre',
            'Torrões', 'Várzea', 'Zumbi'
        ],
        'Sudeste': [
            'Afogados', 'Areias', 'Barro', 'Bongi', 'Caçote', 'Coqueiral', 'Curado',
            'Estância', 'Jardim São Paulo', 'Jiquiá', 'Mangueira', 'Mustardinha',
            'San Martin', 'Sancho', 'Tejipió', 'Totó'
        ],
        'Sul': [
            'Boa Viagem', 'Brasília Teimosa', 'Cohab', 'Ibura',
            'Imbiribeira', 'Ipsep', 'Jordão', 'Pina'
        ]
    }

    # Criar dicionário com bairros sem acento como chave
    bairro_para_regiao = {
        unidecode.unidecode(bairro).strip().title(): regiao
        for regiao, bairros in dicionario.items()
        for bairro in bairros
    }

    # Normalizar a coluna 'Bairro' (sem acento e formatado corretamente)
    df['Bairro_norm'] = df['Bairro'].astype(str).apply(lambda x: unidecode.unidecode(x).strip().title())

    # Criar a coluna Região
    df['Região'] = df['Bairro_norm'].map(bairro_para_regiao)

    # (Opcional) remover a coluna auxiliar
    df.drop(columns='Bairro_norm', inplace=True)

    return df

def main():
    # Carregando os dataframes
    mercados = pd.read_csv(filepath_or_buffer = carregando_as_urls('mercado'), sep=';', encoding='utf-8')
    feiras = pd.read_csv(filepath_or_buffer = carregando_as_urls('feira'), sep=';', encoding='utf-8')
    compras = pd.read_csv(filepath_or_buffer = carregando_as_urls('compra'), sep=';', encoding='utf-8')
    # Criando as colunas para adequar os dataframes
    mercados = criando_as_colunas_para_adequar_o_conjunto_de_dados(mercados, 'Opção', 'Mercado Público')
    mercados = criando_as_colunas_para_adequar_o_conjunto_de_dados(mercados, 'Horário', 'Não informado')
    mercados = criando_as_colunas_para_adequar_o_conjunto_de_dados(mercados, 'Localização', 'Não informado')
    feiras = criando_as_colunas_para_adequar_o_conjunto_de_dados(feiras, 'Opção', 'Feira popular')
    compras = criando_as_colunas_para_adequar_o_conjunto_de_dados(compras, 'Opção', 'Shopping')
    # Ajustando a dataframe  feiras e compras
    feiras = ajustando_nome_das_feiras_livres(feiras)
    feiras = concatenando_a_coluna_funcionamento_com_dias_e_horario(feiras)
    compras = adicionando_o_texto_fixo_e_criando_uma_nova_coluna(compras)
    # Ajustando os dataframes para as mesmas colunas e nomes
    feiras = criando_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando(feiras, 'feira')
    mercados = criando_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando(mercados, 'mercado')
    compras = criando_um_novo_DataFrame_com_as_colunas_desejadas_e_renomeando(compras, 'compra')
    # redefinir os indices de cada dataframe
    compras = redefinir_os_indices_de_cada_DataFrame(compras)
    feiras = redefinir_os_indices_de_cada_DataFrame(feiras)
    mercados = redefinir_os_indices_de_cada_DataFrame(mercados)
    df = concatenar_os_dataframes(compras, feiras, mercados)
    df = criar_a_coluna_Regiao(df)
        
    return df

# criar a variavel df com o dataframe
df = main()

# Definição do programa principal será o main()
if __name__ == '__main__':
    print("Executando compras.py diretamente")


"""
Depois avaliar essa funcao
    for col, val in [('Opção', 'Mercado Público'), ('Horário', 'Não informado'), ('Localização', 'Não informado')]:
        mercados = ajustar_colunas(mercados, col, val)



"""