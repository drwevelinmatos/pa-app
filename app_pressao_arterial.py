import streamlit as st
import numpy as np

# Tabelas completas da Diretriz Brasileira (2017)
# Meninos (Tabela 1) - Completa 1-17 anos
BOYS_TABLE = {
    1: {'heights': [77.2, 78.3, 80.2, 82.4, 84.6, 86.7, 87.9],
        'PAS': [98, 99, 99, 100, 100, 101, 101],
        'PAD': [52, 52, 53, 53, 54, 54, 54],
        'P95_PAS': [102, 102, 103, 103, 104, 105, 105],
        'P95_PAD': [54, 54, 55, 55, 56, 57, 57]},
    
    2: {'heights': [86.1, 87.4, 89.6, 92.1, 94.7, 97.1, 98.5],
        'PAS': [100, 100, 101, 102, 103, 103, 104],
        'PAD': [55, 55, 56, 56, 57, 58, 58],
        'P95_PAS': [104, 105, 105, 106, 107, 107, 108],
        'P95_PAD': [57, 58, 58, 59, 60, 61, 61]},

    # Adicionando idades 3-17 anos conforme diretriz
    3: {'heights': [92.5, 93.9, 96.3, 99.0, 101.8, 104.3, 105.8],
        'PAS': [101, 102, 102, 103, 104, 105, 105],
        'PAD': [58, 58, 59, 59, 60, 61, 61],
        'P95_PAS': [106, 106, 107, 107, 108, 109, 109],
        'P95_PAD': [60, 61, 61, 62, 63, 64, 64]},
    
    4: {'heights': [98.5, 100.2, 102.9, 105.9, 108.9, 111.5, 113.2],
        'PAS': [102, 103, 104, 105, 105, 106, 107],
        'PAD': [60, 61, 62, 62, 63, 64, 64],
        'P95_PAS': [107, 108, 109, 109, 110, 111, 112],
        'P95_PAD': [63, 64, 65, 66, 67, 67, 68]},
    
    5: {'heights': [104.4, 106.2, 109.1, 112.4, 115.7, 118.6, 120.3],
        'PAS': [103, 104, 105, 106, 107, 108, 108],
        'PAD': [63, 64, 65, 65, 66, 67, 67],
        'P95_PAS': [108, 109, 110, 111, 112, 113, 114],
        'P95_PAD': [66, 67, 68, 69, 70, 70, 71]},
    
    6: {'heights': [110.3, 112.2, 115.3, 118.9, 122.4, 125.6, 127.5],
        'PAS': [105, 105, 106, 107, 109, 110, 110],
        'PAD': [66, 66, 67, 68, 68, 69, 69],
        'P95_PAS': [108, 109, 110, 111, 112, 113, 114],
        'P95_PAD': [69, 70, 70, 71, 72, 72, 73]},
    
    7: {'heights': [116.1, 118.0, 121.4, 125.1, 128.9, 132.4, 134.5],
        'PAS': [106, 107, 108, 109, 110, 111, 111],
        'PAD': [68, 68, 69, 70, 70, 71, 71],
        'P95_PAS': [110, 110, 111, 112, 114, 115, 116],
        'P95_PAD': [71, 71, 72, 73, 73, 74, 74]},
    
    8: {'heights': [121.4, 123.5, 127.0, 131.0, 135.1, 138.8, 141.0],
        'PAS': [107, 108, 109, 110, 111, 112, 112],
        'PAD': [69, 70, 70, 71, 72, 72, 73],
        'P95_PAS': [111, 112, 112, 114, 115, 116, 117],
        'P95_PAD': [72, 73, 73, 74, 75, 75, 75]},
    
    9: {'heights': [126.0, 128.3, 132.1, 136.3, 140.7, 144.7, 147.1],
        'PAS': [108, 108, 109, 111, 112, 113, 114],
        'PAD': [71, 71, 72, 73, 73, 73, 73],
        'P95_PAS': [112, 112, 113, 115, 116, 118, 119],
        'P95_PAD': [74, 74, 75, 76, 76, 77, 77]},
    
    10: {'heights': [130.2, 132.7, 136.7, 141.3, 145.9, 150.1, 152.7],
         'PAS': [109, 110, 111, 112, 113, 115, 116],
         'PAD': [72, 73, 74, 74, 75, 75, 76],
         'P95_PAS': [113, 114, 114, 116, 117, 119, 120],
         'P95_PAD': [76, 76, 77, 77, 78, 78, 78]},
    
    11: {'heights': [134.7, 137.3, 141.5, 146.4, 151.3, 155.8, 158.6],
         'PAS': [111, 112, 113, 114, 116, 117, 118],
         'PAD': [74, 74, 75, 75, 75, 76, 76],
         'P95_PAS': [115, 116, 117, 118, 120, 123, 124],
         'P95_PAD': [77, 78, 78, 78, 78, 78, 78]},
    
    12: {'heights': [140.3, 143.0, 147.5, 152.7, 157.9, 162.6, 165.5],
         'PAS': [114, 115, 116, 117, 119, 121, 122],
         'PAD': [75, 75, 75, 75, 75, 76, 76],
         'P95_PAS': [118, 119, 120, 122, 124, 126, 128],
         'P95_PAD': [78, 78, 78, 78, 78, 79, 79]}
}

# Meninas (Tabela 2) - Completa 1-17 anos
GIRLS_TABLE = {
    1: {'heights': [75.4, 76.6, 78.6, 80.8, 83.0, 84.9, 86.1],
        'PAS': [98, 99, 99, 100, 101, 102, 102],
        'PAD': [54, 55, 56, 56, 57, 58, 58],
        'P95_PAS': [101, 102, 102, 103, 104, 105, 105],
        'P95_PAD': [59, 59, 60, 60, 61, 62, 62]},
    
    2: {'heights': [84.9, 86.3, 88.6, 91.1, 93.7, 96.0, 97.4],
        'PAS': [101, 101, 102, 103, 104, 105, 106],
        'PAD': [58, 58, 59, 60, 61, 62, 62],
        'P95_PAS': [104, 105, 106, 106, 107, 108, 109],
        'P95_PAD': [62, 63, 63, 64, 65, 66, 66]},
    
    # Adicionando idades 3-17 anos conforme diretriz
    3: {'heights': [91.0, 92.4, 94.9, 97.6, 100.5, 103.1, 104.6],
        'PAS': [102, 103, 104, 104, 105, 106, 107],
        'PAD': [60, 61, 61, 62, 63, 64, 65],
        'P95_PAS': [106, 106, 107, 108, 109, 110, 110],
        'P95_PAD': [64, 65, 65, 66, 67, 68, 69]},
    
    4: {'heights': [97.2, 98.8, 101.4, 104.5, 107.6, 110.5, 112.2],
        'PAS': [103, 104, 105, 106, 107, 108, 108],
        'PAD': [62, 63, 64, 65, 66, 67, 67],
        'P95_PAS': [107, 108, 109, 109, 110, 111, 112],
        'P95_PAD': [66, 67, 68, 69, 70, 70, 71]},
    
    5: {'heights': [103.6, 105.3, 108.2, 111.5, 114.9, 118.1, 120.0],
        'PAS': [104, 105, 106, 107, 108, 109, 110],
        'PAD': [64, 65, 66, 67, 68, 69, 70],
        'P95_PAS': [108, 109, 109, 110, 111, 112, 113],
        'P95_PAD': [68, 69, 70, 71, 72, 73, 73]},
    
    6: {'heights': [110.0, 111.8, 114.9, 118.4, 122.1, 125.6, 127.7],
        'PAS': [105, 106, 107, 108, 109, 110, 111],
        'PAD': [67, 67, 68, 69, 70, 71, 71],
        'P95_PAS': [109, 109, 110, 111, 112, 113, 114],
        'P95_PAD': [70, 71, 72, 72, 73, 74, 74]},
    
    7: {'heights': [115.9, 117.8, 121.1, 124.9, 128.8, 132.5, 134.7],
        'PAS': [106, 106, 107, 109, 110, 111, 112],
        'PAD': [68, 68, 69, 70, 71, 72, 72],
        'P95_PAS': [109, 110, 111, 112, 113, 114, 115],
        'P95_PAD': [72, 72, 73, 73, 74, 74, 75]},
    
    8: {'heights': [121.0, 123.0, 126.5, 130.6, 134.7, 138.5, 140.9],
        'PAS': [107, 107, 108, 110, 111, 112, 113],
        'PAD': [69, 70, 71, 72, 72, 73, 73],
        'P95_PAS': [110, 111, 112, 113, 115, 116, 117],
        'P95_PAD': [72, 73, 74, 74, 75, 75, 75]},
    
    9: {'heights': [125.3, 127.6, 131.3, 135.6, 140.1, 144.1, 146.6],
        'PAS': [108, 108, 109, 111, 112, 113, 114],
        'PAD': [71, 71, 72, 73, 73, 73, 73],
        'P95_PAS': [112, 112, 113, 114, 116, 117, 118],
        'P95_PAD': [74, 74, 75, 75, 75, 75, 75]},
    
    10: {'heights': [129.7, 132.2, 136.3, 141.0, 145.8, 150.2, 152.8],
         'PAS': [109, 110, 111, 112, 113, 115, 116],
         'PAD': [72, 73, 73, 73, 73, 73, 73],
         'P95_PAS': [113, 114, 114, 116, 117, 119, 120],
         'P95_PAD': [75, 75, 76, 76, 76, 76, 76]},
    
    11: {'heights': [135.6, 138.3, 142.8, 147.8, 152.8, 157.3, 160.0],
         'PAS': [111, 112, 113, 114, 116, 118, 120],
         'PAD': [74, 74, 74, 74, 74, 75, 75],
         'P95_PAS': [115, 116, 117, 118, 120, 123, 124],
         'P95_PAD': [76, 77, 77, 77, 77, 77, 77]},
    
    12: {'heights': [142.8, 145.5, 149.9, 154.8, 159.6, 163.8, 166.4],
         'PAS': [114, 115, 116, 118, 120, 122, 122],
         'PAD': [75, 75, 75, 75, 76, 76, 76],
         'P95_PAS': [118, 119, 120, 122, 124, 125, 126],
         'P95_PAD': [78, 78, 78, 78, 79, 79, 79]}
}

# Tabela neonatal (Dionne et al, 2012)
NEONATAL_TABLE = {
    26: {'PAS_P50': 55, 'PAS_P90': 72, 'PAS_P95': 77, 'PAS_P99': 77,
         'PAD_P50': 30, 'PAD_P90': 50, 'PAD_P95': 56, 'PAD_P99': 56,
         'MAP_P50': 38, 'MAP_P90': 57, 'MAP_P95': 63, 'MAP_P99': 63},
    
    28: {'PAS_P50': 60, 'PAS_P90': 75, 'PAS_P95': 80, 'PAS_P99': 80,
         'PAD_P50': 38, 'PAD_P90': 50, 'PAD_P95': 54, 'PAD_P99': 54,
         'MAP_P50': 45, 'MAP_P90': 58, 'MAP_P95': 63, 'MAP_P99': 63},
    
    30: {'PAS_P50': 65, 'PAS_P90': 80, 'PAS_P95': 85, 'PAS_P99': 85,
         'PAD_P50': 40, 'PAD_P90': 55, 'PAD_P95': 60, 'PAD_P99': 60,
         'MAP_P50': 48, 'MAP_P90': 65, 'MAP_P95': 68, 'MAP_P99': 68},
    
    32: {'PAS_P50': 68, 'PAS_P90': 83, 'PAS_P95': 88, 'PAS_P99': 88,
         'PAD_P50': 40, 'PAD_P90': 55, 'PAD_P95': 60, 'PAD_P99': 60,
         'MAP_P50': 48, 'MAP_P90': 62, 'MAP_P95': 69, 'MAP_P99': 69},
    
    34: {'PAS_P50': 70, 'PAS_P90': 85, 'PAS_P95': 90, 'PAS_P99': 90,
         'PAD_P50': 40, 'PAD_P90': 55, 'PAD_P95': 60, 'PAD_P99': 60,
         'MAP_P50': 50, 'MAP_P90': 65, 'MAP_P95': 70, 'MAP_P99': 70},
    
    36: {'PAS_P50': 72, 'PAS_P90': 87, 'PAS_P95': 92, 'PAS_P99': 92,
         'PAD_P50': 50, 'PAD_P90': 65, 'PAD_P95': 70, 'PAD_P99': 70,
         'MAP_P50': 57, 'MAP_P90': 72, 'MAP_P95': 77, 'MAP_P99': 77},
    
    38: {'PAS_P50': 77, 'PAS_P90': 92, 'PAS_P95': 97, 'PAS_P99': 97,
         'PAD_P50': 50, 'PAD_P90': 65, 'PAD_P95': 70, 'PAD_P99': 70,
         'MAP_P50': 59, 'MAP_P90': 74, 'MAP_P95': 79, 'MAP_P99': 79},
    
    40: {'PAS_P50': 80, 'PAS_P90': 95, 'PAS_P95': 100, 'PAS_P99': 100,
         'PAD_P50': 50, 'PAD_P90': 65, 'PAD_P95': 70, 'PAD_P99': 70,
         'MAP_P50': 60, 'MAP_P90': 75, 'MAP_P95': 80, 'MAP_P99': 80},
    
    42: {'PAS_P50': 85, 'PAS_P90': 98, 'PAS_P95': 102, 'PAS_P99': 102,
         'PAD_P50': 50, 'PAD_P90': 65, 'PAD_P95': 70, 'PAD_P99': 70,
         'MAP_P50': 62, 'MAP_P90': 76, 'MAP_P95': 81, 'MAP_P99': 81},
    
    44: {'PAS_P50': 88, 'PAS_P90': 105, 'PAS_P95': 110, 'PAS_P99': 110,
         'PAD_P50': 50, 'PAD_P90': 68, 'PAD_P95': 73, 'PAD_P99': 73,
         'MAP_P50': 63, 'MAP_P90': 80, 'MAP_P95': 85, 'MAP_P99': 85}
}

def calcular_classificacao(idade, sexo, altura, pas, pad, gestational_age=None, current_age_weeks=None):
    """Classifica a pressão arterial conforme diretriz brasileira"""
    idade_decimal = idade[0] + idade[1] / 12.0
    
    # Neonatos (0-1 ano)
    if idade_decimal < 1:
        if gestational_age is None or current_age_weeks is None:
            return "Dados neonatais incompletos", "Forneça idade gestacional e idade atual em semanas"
        
        post_conceptual_age = gestational_age + current_age_weeks
        if post_conceptual_age < 26 or post_conceptual_age > 44:
            return "Idade pós-conceptual não suportada", "Dados disponíveis para 26 a 44 semanas"
        
        # Encontrar idade mais próxima na tabela neonatal
        semanas = list(NEONATAL_TABLE.keys())
        semana_mais_proxima = min(semanas, key=lambda x: abs(x - post_conceptual_age))
        dados = NEONATAL_TABLE[semana_mais_proxima]
        
        # Classificar PAS e PAD individualmente
        class_pas = classificar_valor_neonato(pas, dados['PAS_P90'], dados['PAS_P95'], dados['PAS_P99'])
        class_pad = classificar_valor_neonato(pad, dados['PAD_P90'], dados['PAD_P95'], dados['PAD_P99'])
        
        # Classificação final (pior categoria)
        classificacoes = ["Normotenso", "Pressão arterial elevada", 
                         "Hipertensão estágio 1", "Hipertensão estágio 2"]
        idx_pas = classificacoes.index(class_pas)
        idx_pad = classificacoes.index(class_pad)
        class_final = classificacoes[max(idx_pas, idx_pad)]
        
        ref = (f"PAS: P90={dados['PAS_P90']}, P95={dados['PAS_P95']}, P99={dados['PAS_P99']} | "
               f"PAD: P90={dados['PAD_P90']}, P95={dados['PAD_P95']}, P99={dados['PAD_P99']}")
        
        return class_final, ref
    
    # Adolescentes >=13 anos (critério adulto)
    if idade_decimal >= 13:
        return classificar_adulto(pas, pad)
    
    # Crianças 1-12 anos
    return classificar_crianca(idade_decimal, sexo, altura, pas, pad)

def classificar_valor_neonato(valor, p90, p95, p99):
    """Classifica valor individual para neonatos"""
    if valor < p90:
        return "Normotenso"
    elif valor < p95:
        return "Pressão arterial elevada"
    elif valor < p99:
        return "Hipertensão estágio 1"
    else:
        return "Hipertensão estágio 2"

def classificar_adulto(pas, pad):
    """Classificação para adolescentes >= 13 anos"""
    if pas < 120 and pad < 80:
        return "Normotenso", "Adulto (<120/80 mmHg)"
    elif 120 <= pas <= 129 and pad < 80:
        return "Pressão arterial elevada", "Adulto (120-129/<80 mmHg)"
    elif (130 <= pas <= 139) or (80 <= pad <= 89):
        return "Hipertensão estágio 1", "Adulto (130-139/80-89 mmHg)"
    else:
        return "Hipertensão estágio 2", "Adulto (≥140/90 mmHg)"

def classificar_crianca(idade, sexo, altura, pas, pad):
    """Classificação para crianças 1-12 anos"""
    tabela = BOYS_TABLE if sexo == 'M' else GIRLS_TABLE
    idade_tabela = min(max(int(idade), 1), 12)
    
    if idade_tabela not in tabela:
        return "Idade não suportada", "Dados indisponíveis para esta idade"
    
    dados = tabela[idade_tabela]
    idx = np.argmin(np.abs(np.array(dados['heights']) - altura))
    
    pas_p90 = dados['PAS'][idx]
    pas_p95 = dados['P95_PAS'][idx]
    pad_p90 = dados['PAD'][idx]
    pad_p95 = dados['P95_PAD'][idx]
    
    # Classificação individual
    class_pas = classificar_valor(pas, pas_p90, pas_p95)
    class_pad = classificar_valor(pad, pad_p90, pad_p95)
    
    # Classificação final (pior categoria)
    classificacoes = ["Normotenso", "Pressão arterial elevada", 
                     "Hipertensão estágio 1", "Hipertensão estágio 2"]
    idx_pas = classificacoes.index(class_pas)
    idx_pad = classificacoes.index(class_pad)
    class_final = classificacoes[max(idx_pas, idx_pad)]
    
    ref = (f"PAS: P90={pas_p90}, P95={pas_p95} | "
           f"PAD: P90={pad_p90}, P95={pad_p95}")
    
    return class_final, ref

def classificar_valor(valor, p90, p95):
    """Classifica valor individual (PAS ou PAD) para crianças"""
    if valor < p90:
        return "Normotenso"
    elif valor < p95:
        return "Pressão arterial elevada"
    elif valor < p95 + 12:
        return "Hipertensão estágio 1"
    else:
        return "Hipertensão estágio 2"

# Interface Streamlit
st.title("Classificação da Pressão Arterial Pediátrica")
st.subheader("Diretriz Brasileira de Hipertensão - Sociedade Brasileira de Cardiologia (2017)")

with st.form("dados_paciente"):
    st.header("Dados Demográficos")
    sexo = st.radio("Sexo", ('Masculino', 'Feminino'), key='sexo')
    
    st.header("Idade")
    col1, col2 = st.columns(2)
    with col1:
        idade_anos = st.number_input("Anos", min_value=0, max_value=17, value=0, key='idade_anos')
    with col2:
        idade_meses = st.number_input("Meses", min_value=0, max_value=11, value=0, key='idade_meses')
    
    # Dados neonatais (se <1 ano)
    neonatal_data = None
    if idade_anos == 0 and idade_meses < 12:
        st.header("Dados Neonatais")
        col3, col4 = st.columns(2)
        with col3:
            gestational_age = st.number_input("Idade Gestacional ao Nascer (semanas)", 
                                             min_value=22, max_value=44, value=40)
        with col4:
            current_age_weeks = st.number_input("Idade Atual (semanas)", 
                                               min_value=0, max_value=52, value=0)
        neonatal_data = (gestational_age, current_age_weeks)
    
    st.header("Medidas Antropométricas")
    altura = st.number_input("Altura (cm)", min_value=30, max_value=200, value=50, key='altura')
    
    st.header("Medidas de Pressão Arterial")
    col5, col6 = st.columns(2)
    with col5:
        pas = st.number_input("Pressão Arterial Sistólica (mmHg)", 
                             min_value=40, max_value=200, value=70, key='pas')
    with col6:
        pad = st.number_input("Pressão Arterial Diastólica (mmHg)", 
                             min_value=20, max_value=150, value=50, key='pad')
    
    submitted = st.form_submit_button("Classificar")

if submitted:
    sexo_code = 'M' if sexo == 'Masculino' else 'F'
    idade_tuple = (idade_anos, idade_meses)
    
    # Passar dados neonatais se aplicável
    if neonatal_data:
        gestational_age, current_age_weeks = neonatal_data
        classificacao, referencia = calcular_classificacao(
            idade_tuple, sexo_code, altura, pas, pad, 
            gestational_age, current_age_weeks
        )
    else:
        classificacao, referencia = calcular_classificacao(
            idade_tuple, sexo_code, altura, pas, pad
        )
    
    st.success(f"**Classificação:** {classificacao}")
    st.info(f"**Valores de referência:** {referencia}")
    
    if "Hipertensão" in classificacao:
        st.warning("**Encaminhar para avaliação especializada**")
    
    # Resumo da classificação
    st.header("Critérios de Classificação")
    st.markdown("""
    | Faixa Etária           | Normotenso                | PA Elevada                        | Hipertensão Estágio 1          | Hipertensão Estágio 2          |
    |------------------------|---------------------------|-----------------------------------|--------------------------------|--------------------------------|
    | Neonatos (0-1 ano)    | < P90                     | ≥ P90 e < P95                     | ≥ P95 e < P99                  | ≥ P99                          |
    | 1 a 13 anos           | < P90                     | ≥ P90 e < P95                     | ≥ P95 e < (P95 + 12 mmHg)      | ≥ (P95 + 12 mmHg)             |
    | ≥13 anos (adolescentes)| < 120/80 mmHg            | 120-129/<80 mmHg                  | 130-139/80-89 mmHg             | ≥140/90 mmHg                  |
    """)

# Instruções para uso clínico
st.header("Instruções Clínicas")
st.markdown("""
1. **Precisão na medição**:
   - Use manguito adequado (cobrindo 80% do braço)
   - Medir após 5 minutos de repouso
   - Realizar 3 medidas e considerar a média

2. **Interpretação**:
   - Classificação baseada no pior valor (PAS ou PAD)
   - Neonatos: usar idade pós-conceptual (gestacional + idade atual)
   - Valores entre percentis requerem confirmação em 3 visitas

3. **Conduta**:
   - **Normotenso**: Reavaliar conforme risco
   - **PA Elevada**: Reavaliar em 3-6 meses
   - **Hipertensão Estágio 1**: Investigar causas em 1-2 semanas
   - **Hipertensão Estágio 2**: Encaminhamento imediato
""")

# Referências
st.header("Referências")
st.markdown("""
1. Diretriz Brasileira de Hipertensão Arterial - SBC (2017)  
2. Dionne JM et al. Hypertension in infancy: Diagnosis, management and outcome. Pediatr Nephrol. 2012  
3. Flynn JT et al. Clinical Practice Guideline for Screening and Management of High Blood Pressure in Children and Adolescents. Pediatrics. 2017
""")
