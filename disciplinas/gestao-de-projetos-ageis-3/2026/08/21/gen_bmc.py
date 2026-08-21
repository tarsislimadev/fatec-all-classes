import matplotlib.pyplot as plt

data = {
    'Key Partners': 'Secretaria da Mulher\nFatec Rio Claro\nONGs de apoio\nDelegacia da Mulher\nHospitais/Saúde',
    'Key Activities': 'Desenvolvimento IA\nColeta/Análise dados\nCampanhas conscientização\nTreinamento equipe',
    'Key Resources': 'Equipe Fatec\nConhecimento IA\nInfraestrutura Tech\nApoio Institucional',
    'Value Propositions': 'Soluções de IA para\nprevenção, monitoramento\ne combate à violência\ncontra a mulher',
    'Customer Relationships': 'Atendimento humanizado\nOficinas/Palestras\nSuporte à Secretaria\nComunicação acessível',
    'Channels': 'App/Plataforma Digital\nRedes Sociais\nEventos Comunitários\nParcerias Escolas/Univ',
    'Customer Segments': 'Secretaria da Mulher\nMulheres vulneráveis\nComunidade local\nONGs/Escolas/Hospitais',
    'Cost Structure': 'Desenvolvimento Tech\nTreinamentos\nCampanhas Divulgação\nManutenção Plataforma',
    'Revenue Streams': 'Financiamento Público\nParcerias ONGs/Empresas\nBenefício Social (Redução Violência)'
}

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.axis('off')

grid = {
    'Key Partners': [0, 1, 1, 3],
    'Key Activities': [1, 2, 1, 1.5],
    'Key Resources': [1, 0.5, 1, 1.5],
    'Value Propositions': [2, 1, 1, 3],
    'Customer Relationships': [3, 2, 1, 1.5],
    'Channels': [3, 0.5, 1, 1.5],
    'Customer Segments': [4, 1, 1, 3],
    'Cost Structure': [0, 0, 2.5, 1],
    'Revenue Streams': [2.5, 0, 2.5, 1],
}

for key, pos in grid.items():
    x, y, w, h = pos
    rect = plt.Rectangle((x, y), w, h, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    plt.text(x + w/2, y + h/2, f'{key}\n\n{data[key]}', 
             ha='center', va='center', wrap=True, fontsize=9)

plt.title('Business Model Canvas - Projeto Fatec & Secretaria da Mulher', fontsize=16, pad=20)
plt.savefig('/workspaces/fatec-all-classes/disciplinas/gestao-de-projetos-ageis-3/2026/08/21/bmc.png', bbox_inches='tight')
