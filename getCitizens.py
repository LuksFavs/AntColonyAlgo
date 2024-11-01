import requests
import numpy as np

capitais_estaduais = {
    "Rio Branco": 1200401,
    "Maceió": 2704302, 
    "Macapá": 1600303,
    "Manaus": 1302603, 
    "Salvador": 2927408,
    "Fortaleza": 2304400,
    "Brasília": 5300108, 
    "Vitória": 3205309,  
    "Goiânia": 5208707,  
    "São Luís": 2111300,  
    "Cuiabá": 5103403,  
    "Campo Grande": 5002704,  
    "Belo Horizonte": 3106200,  
    "Belém": 1501402,  
    "João Pessoa": 2507507,  
    "Curitiba": 4106902,  
    "Recife": 2611606,  
    "Teresina": 2211001,  
    "Rio de Janeiro": 3304557,  
    "Natal": 2408102,  
    "Porto Alegre": 4314902,  
    "Porto Velho": 1100205,  
    "Boa Vista": 1400100,  
    "Florianópolis": 4205407,  
    "São Paulo": 3550308,  
    "Aracaju": 2800308,  
    "Palmas": 1721000  
}
index = {
    "Rio Branco": 0,  
    "Maceió": 1,  
    "Macapá": 2,  
    "Manaus": 3,  
    "Salvador": 4,  
    "Fortaleza": 5,  
    "Brasília": 6,  
    "Vitória": 7,  
    "Goiânia": 8,  
    "São Luís": 9,  
    "Cuiabá": 10,  
    "Campo Grande": 11,  
    "Belo Horizonte": 12,  
    "Belém": 13,  
    "João Pessoa": 14,  
    "Curitiba": 15,  
    "Recife": 16,  
    "Teresina": 17,  
    "Rio de Janeiro": 18,  
    "Natal": 19,  
    "Porto Alegre": 20,  
    "Porto Velho": 21,  
    "Boa Vista": 22,  
    "Florianópolis": 23,  
    "São Paulo": 24,  
    "Aracaju": 25,  
    "Palmas": 26
}
pops = np.zeros(27)

# Função para obter dados das regiões metropolitanas e suas populações
def obter_regioes_metropolitanas():
            for i in capitais_estaduais:
                url = 'https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/-6/variaveis/93?localidades=N6['+str(capitais_estaduais[i])+']'
                response = requests.get(url)

                if response.status_code == 200:
                    regioes = response.json()
                    pops[index[i]] = regioes[0]['resultados'][0]['series'][0]['serie']['2022']
                else:
                    print("Erro ao acessar a API:", response.status_code)
                    return None
            np.save('pops', pops)

