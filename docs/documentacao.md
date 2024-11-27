## Script para criação de um dataset fake(criacao_dataset.py)

### Utilizei a biblioteca Fake e random(padrão do Python) para a criação do dataset

### Logo, percebi que os dados estavam muito organizados e sem nenhum problema, então para dificultar resolvi adicionar alguns problemas no dataset

#### Na coluna 'Preço' resolvi colocar valores nulos aleatoriamente

#### Na coluna 'Data' resolvi colocar uma data fora do padrão
##### Padrão atual - Ano-Mês-Dia - Apenas no ano de 2023

#### Na coluna 'Quantidade' coloquei valores que não são números utilizando a biblioteca 'num2words' que transforma numeros em no seu respectivo valor por extenso

# Análise e tratamento do dataset
## Script para análise e tratamento do dataset

### Comecei pela coluna 'Preço'
#### Utilizei a técnica de interpolação linear para preencher os valores vazios
###### Utilizei essa técnica pois achei a melho, visto que é um dataset de vendas.

### Logo após resolvi ir para a coluna 'Quantidade' para realizar a conversão de número por extenso para número normal.
#### Me deparei com um problema. 
#### Tentei utilizar a biblioteca word2number para realizar essa conversão.

#### Porém, a biblioteca word2number não reconhece números em português.
#### Então, tive que primeiramente traduzir todos os números por extenso para inglês utilizando a biblioteca 'translate'.

#### Me deparei com outro problema: por algum motivo a biblioteca translate não traduz a palavra 'sete', então tive que realizar essa conversão 'manualmente'.

### Agora realizei o tratamento na coluna 'Data', fiz um filtro onde as datas em formato errado, transforma os valores em nulos e logo apos exclui ele.
### Depois, fiz um filtro onde so aceite as datas durante o período desejado

### Para criar os gráficos eu utilizei a biblioteca matplotlib
### Criei diversos gráficos, por exemplo, tendência de vendas ao longo do tempo, Vendas por categoria, Produtops mais vendidos