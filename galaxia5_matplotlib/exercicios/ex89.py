import pandas as pd
import yfinance as yf

acoes = []

for n in range(1, 4):
    acao = str(input(f'Digite o ticker: ')).upper() + '.SA'
    acoes.append(acao)

df_acoes = pd.DataFrame(yf.download(acoes)['Adj Close'])

# - Um gráfico de linha com a trajetória das cotações das empresas.

df_acoes = ((df_acoes.pct_change().dropna()) + 1).cumprod() - 1

df_acoes.plot()

# - Um gráfico de área com o volume de cada ação.

df_acoes_adj_close = pd.DataFrame(yf.download(acoes)['Adj Close'])
df_acoes_volume = pd.DataFrame(yf.download(acoes)['Volume'])

volume = df_acoes_adj_close * df_acoes_volume

volume = volume.dropna().resample("M").mean()

volume.plot.area()

# - Um gráfico boxsplot com os retornos mensais de cada ação.

df_boxsplot = df_acoes_adj_close.resample("M").last().pct_change().dropna()

df_boxsplot.plot.box()

# - Três gráficos de dispersão entre as ações e o ibovespa pra cada ano. 

df_acoes = pd.DataFrame(yf.download(acoes)['Adj Close'])

ibov = yf.download('^BVSP')['Adj Close']

retorno_anual_ibov = ibov.resample("Y").last().pct_change().dropna()
retornos_anual = df_acoes.resample("Y").last().pct_change().dropna()

for acao in df_acoes:
    
    df = pd.DataFrame({acao: retornos_anual[acao],
                      'Ibovespa': retorno_anual_ibov}, index = retorno_anual_ibov.index)
    
    df['Ano'] = df.index.year
    df['Ano'] = df['Ano'].astype("category")
    
    df.plot.scatter(x = acao, y = "Ibovespa", c = "Ano",  cmap = "viridis")