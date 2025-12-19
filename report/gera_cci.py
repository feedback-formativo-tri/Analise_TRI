import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def theta_to_enem(habilidade_tri):
   habilidade_enem = ((habilidade_tri + 4) / 8) * 800 + 200
   return habilidade_enem


def scatter_plot(df, area_conhecimento, item, aluno, habilidade_normalizada, dificuldade, examinando="", titulo=""):
    coluna_y = item

    habilidade_enem = theta_to_enem(df['theta'])
    
    scatter = go.Figure()

    if area_conhecimento == "MT" and item > 40:
      scatter.add_trace(go.Scatter(
          x=habilidade_enem,
          y=df[f"Item  {coluna_y}"],
          name=df.columns[coluna_y-1],
          mode='lines'
      ))
    else:
      scatter.add_trace(go.Scatter(
          x=habilidade_enem,
          y=df[f"Item  {coluna_y}"],
          name=df.columns[coluna_y],
          mode='lines'
      ))

    # Layout do gráfico
    scatter.update_layout(
        title=dict(
          text=titulo,
          y=1.0  # valor padrão ≈ 0.9; aumente para subir o título
      ),
        xaxis=dict(
            title='Habilidade θ',
            range=[200, 1000],
            zeroline=False
        ),
        yaxis=dict(
            title='Probabilidade P(θ)',
            range=[0, 1.0],
            zeroline=False
        )
    )

    scatter.add_shape(
      type="line",
      x0=habilidade_normalizada,
      x1=habilidade_normalizada,
      y0=0,
      y1=aluno['probabilidade'],
      line=dict(
          width=1.5,
          dash="dot",
          color="#888"
      )
    )

    scatter.add_shape(
      type="line",
      x0=200,
      x1=habilidade_normalizada,
      y0=aluno['probabilidade'],
      y1=aluno['probabilidade'],
      line=dict(
          width=1.5,
          dash="dot",
          color="#888"
      )
    )

    if aluno['probabilidade'] > 0.90:
       ay = -50
    else:
       ay = -100

    # Anotação
    scatter.add_annotation(
        x=habilidade_normalizada,
        y=aluno['probabilidade'],
        text=f"{examinando}<br>Habilidade (θ): {habilidade_normalizada:.2f}"
             f"<br>Probabilidade P(θ): {np.round(aluno['probabilidade'] * 100, 2)}%",
        showarrow=True,
        arrowhead=7,
        arrowwidth=2,
        ax=aluno['theta'] - 100,
        ay=ay,
        arrowcolor="#636363",
        bordercolor="#c7c7c7",
        bgcolor="#2CA02C",
        font=dict(color="white")
    )

    cor_dificuldade = "#ff7f0e"

    scatter.add_trace(go.Scatter(
        x=[dificuldade],
        y=[(1 + aluno["prob_chute"]) / 2],
        mode='markers',
        marker=dict(size=10, color=cor_dificuldade),
        name="Dificuldade da questão"
    ))

    scatter.add_annotation(
      x=habilidade_normalizada,
      y=0,
      text=f"{habilidade_normalizada:.2f}",
      showarrow=False,
      yshift=9,
      font=dict(size=10, color="#333"),
      bgcolor="white",
      bordercolor="#999",
      borderwidth=1,
      opacity=0.8
    )

    scatter.add_annotation(
      x=200,
      y=aluno['probabilidade'],
      text=f"{(aluno['probabilidade']*100):.2f}%",
      showarrow=False,
      xshift=22,
      font=dict(size=10, color="#333"),
      bgcolor="white",
      bordercolor="#999",
      borderwidth=1,
      opacity=0.8
    )
    
    return scatter

def gera_scatter(df, area_conhecimento, item, prob_chute, dificuldade, titulo=""):
    coluna_y = item

    habilidade_enem = theta_to_enem(df['theta'])
    
    scatter = go.Figure()

    if area_conhecimento == "MT" and item > 40:
      scatter.add_trace(go.Scatter(
          x=habilidade_enem,
          y=df[f"Item  {coluna_y}"],
          name=df.columns[coluna_y-1],
          mode='lines'
      ))
    else:
      scatter.add_trace(go.Scatter(
          x=habilidade_enem,
          y=df[f"Item  {coluna_y}"],
          name=df.columns[coluna_y],
          mode='lines'
      ))

    # Layout do gráfico
    scatter.update_layout(
        title=titulo,
        xaxis=dict(
            title='Habilidade θ',
            range=[200, 1000],
            zeroline=False
        ),
        yaxis=dict(
            title='Probabilidade P(θ)',
            range=[0, 1.0],
            zeroline=False
        )
    )

    scatter.add_shape(
      type="line",
      x0=dificuldade,
      x1=dificuldade,
      y0=0,
      y1=(1 + prob_chute) / 2,
      line=dict(
          width=1.5,
          dash="dot",
          color="#888"
      )
    )

    scatter.add_shape(
      type="line",
      x0=200,
      x1=dificuldade,
      y0=(1 + prob_chute) / 2,
      y1=(1 + prob_chute) / 2,
      line=dict(
          width=1.5,
          dash="dot",
          color="#888"
      )
    )

    cor_dificuldade = "#ff7f0e"

    scatter.add_trace(go.Scatter(
        x=[dificuldade],
        y=[(1 + prob_chute) / 2],
        mode='markers',
        marker=dict(size=10, color=cor_dificuldade),
        name="Dificuldade da questão"
    ))

    scatter.add_annotation(
      x=dificuldade,
      y=0,
      text=f"{dificuldade:.2f}",
      showarrow=False,
      yshift=9,
      font=dict(size=10, color="#333"),
      bgcolor="white",
      bordercolor="#999",
      borderwidth=1,
      opacity=0.8
    )

    scatter.add_annotation(
      x=200,
      y=(1 + prob_chute) / 2,
      text=f"{(((1 + prob_chute) / 2)*100):.2f}%",
      showarrow=False,
      xshift=22,
      font=dict(size=10, color="#333"),
      bgcolor="white",
      bordercolor="#999",
      borderwidth=1,
      opacity=0.8
    )
    
    return scatter


def get_habilidade_aluno(matricula, estado, area_conhecimento, questao):
  df_habil_3PL = pd.read_csv(f"../codigos_R/LTM_3PL/habilidades/habil_3PL_ltm_{area_conhecimento}_{estado}.csv")
  df_habil_3PL["alunos_id_string"] = df_habil_3PL["alunos_id_string"].astype(str)
  habil_examinando = df_habil_3PL[df_habil_3PL["alunos_id_string"] == matricula]
  
  return habil_examinando

def get_dificuldade_item(estado, area_conhecimento, item):
  df_dificuldade = pd.read_csv(f"../codigos_R/LTM_3PL/dificuldades/dif_modelo_3PL_ltm_{area_conhecimento}_{estado}.csv")
  df_dificuldade = df_dificuldade[df_dificuldade["questao"] == item]
  
  chute = df_dificuldade["acerto_acaso_item"].values[0]
  dificuldade = df_dificuldade["dificuldade_item"].values[0]
  discriminacao = df_dificuldade["discriminacao_item"].values[0]
  
  return chute, dificuldade, discriminacao

def get_prob_acerto(area_conhecimento, estado):
  df_probabilidade = pd.read_csv(f"../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv")
  
  return df_probabilidade

def get_item_prova(area, questao):
    prova_amarela = pd.read_csv(f'../pre-processamento/Itens_provas_amarela/dt_itens_{area}_amarela.csv')
    prova_amarela = prova_amarela.drop(columns=["Unnamed: 0"])
  
    if area == "MT":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao+135]
    elif area == "CN":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao+90]
    elif area == "CH":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao+45]
    elif area == "LC":
        item = prova_amarela[prova_amarela["CO_POSICAO"] == questao]
    else:
        return 0
    
    return item["CO_POSICAO"].values[0]

def gera_cci_aluno_no_llm(matricula, questao, area_conhecimento, estado):
  cci_file = f"plots/cci_{matricula}_{estado}_{area_conhecimento}_{questao}.html"

  habil_examinando = get_habilidade_aluno(matricula, estado, area_conhecimento, questao)
  habil_examinando = habil_examinando["habilidade"].values[0]
  if habil_examinando > 4:
    habil_examinando = 4.00
  elif habil_examinando < -4:
    habil_examinando = -4.00
  
  habil_examinando_normalizada = ((habil_examinando + 4)/8) * 800 + 200
  habil_examinando = round(habil_examinando, 4)

  acerto_acaso_item, dificuldade_item, discriminacao_item = get_dificuldade_item(estado, area_conhecimento, questao)
  
  dificuldade_normalizada = dificuldade_item

  if dificuldade_item > 4:
    dificuldade_normalizada = 4.00
  elif dificuldade_item < -4:
    dificuldade_normalizada = -4.00
  
  dificuldade_normalizada = ((dificuldade_normalizada + 4)/8) * 800 + 200

  df_probabilidade = get_prob_acerto(area_conhecimento, estado)

  prob_acerto = df_probabilidade[round(df_probabilidade["theta"], 4) == habil_examinando]
  prob_acerto = prob_acerto[f'Item  {questao}'].values[0]

  dados_examinando = {
    "theta": habil_examinando,
    "probabilidade": prob_acerto,
    "prob_chute": acerto_acaso_item,
    "discriminacao": discriminacao_item,
    "dificuldade": dificuldade_item
  }

  item_prova = get_item_prova(area_conhecimento, questao)


  cci = scatter_plot(df_probabilidade, area_conhecimento, questao, dados_examinando, habil_examinando_normalizada, dificuldade_normalizada, f"Código do examinando: {matricula}", f"CCI para o item {item_prova} da prova de {area_conhecimento}")

  cci_html = cci.to_html(include_plotlyjs="cdn", full_html=False)

  with open(cci_file, "w", encoding="utf-8") as f:
      f.write(cci_html)
  
  return cci_file


if __name__ == "__main__":
    matricula = "210057348542"
    questao = 18
    area_conhecimento = "CN"
    estado = "PR"

    scatter_file = f"plots/cci_{matricula}_{estado}_{area_conhecimento}_{questao}_teste.html"

    habil_examinando = get_habilidade_aluno(matricula, estado, area_conhecimento, questao)
    habil_examinando = habil_examinando["habilidade"].values[0]
    if habil_examinando > 4:
      habil_examinando = 4.00
    elif habil_examinando < -4:
      habil_examinando = -4.00
    
    habil_examinando_normalizada = ((habil_examinando + 4)/8) * 800 + 200
    habil_examinando = round(habil_examinando, 4)

    acerto_acaso_item, dificuldade_item, discriminacao_item = get_dificuldade_item(estado, area_conhecimento, questao)
    
    dificuldade_normalizada = dificuldade_item

    if dificuldade_item > 4:
      dificuldade_normalizada = 4.00
    elif dificuldade_item < -4:
      dificuldade_normalizada = -4.00
    
    dificuldade_normalizada = ((dificuldade_normalizada + 4)/8) * 800 + 200

    df_probabilidade = get_prob_acerto(area_conhecimento, estado)

    item_prova = get_item_prova(area_conhecimento, questao)

    scatter = gera_scatter(df_probabilidade, area_conhecimento, questao, acerto_acaso_item, dificuldade_normalizada, f"CCI para o item {item_prova} da prova de {area_conhecimento}")

    scatter_html = scatter.to_html(include_plotlyjs="cdn", full_html=False)

    with open(scatter_file, "w", encoding="utf-8") as f:
        f.write(scatter_html)

    # gera_cci_aluno_no_llm(matricula, questao, area_conhecimento, estado)
