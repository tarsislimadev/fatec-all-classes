from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import mm

OUTPUT_PDF = "/workspaces/fatec-all-classes/disciplinas/aprendizado-de-maquina/2026/09/24/Resolucao_Classificacao_com_Naive_Bayes.pdf"


def build_pdf():
    styles = getSampleStyleSheet()
    story = []

    title = "Resolução - Classificação com Naive Bayes"
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 10 * mm))

    story.append(Paragraph(
        "<b>Contexto:</b> Uma instituição financeira deseja avaliar o risco de concessão de crédito calculando a probabilidade de um cliente se tornar inadimplente com base em características do seu perfil histórico.",
        styles['BodyText']
    ))
    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph("<b>Variáveis:</b>", styles['Heading2']))
    story.append(Paragraph("- y: inadimplente (1 = Sim; 0 = Não)", styles['BodyText']))
    story.append(Paragraph("- x1: nome negativado em órgãos de crédito (1 = Sim; 0 = Não)", styles['BodyText']))
    story.append(Paragraph("- x2: renda mensal comprovada estável (1 = Sim; 0 = Não)", styles['BodyText']))
    story.append(Paragraph("- x3: possui garantias ou bens (1 = Sim; 0 = Não)", styles['BodyText']))
    story.append(Spacer(1, 8 * mm))

    data = [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]
    # Rebuild the intended table with clear fields.
    table_data = [
        ["Cliente", "y", "x1", "x2", "x3"],
        [1, 1, 1, 0, 0],
        [2, 1, 1, 1, 0],
        [3, 1, 0, 0, 0],
        [4, 1, 1, 0, 1],
        [5, 1, 1, 0, 0],
        [6, 0, 0, 1, 1],
        [7, 0, 1, 1, 0],
        [8, 0, 0, 1, 0],
    ]
    table = Table(table_data, colWidths=[18 * mm, 14 * mm, 14 * mm, 14 * mm, 14 * mm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dfeaf7')),
        ('GRID', (0, 0), (-1, -1), 0.8, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
    ]))
    story.append(Paragraph("<b>Dados históricos de treinamento:</b>", styles['Heading2']))
    story.append(table)
    story.append(Spacer(1, 8 * mm))

    y_counts = {0: 3, 1: 5}
    total = sum(y_counts.values())
    prior_0 = y_counts[0] / total
    prior_1 = y_counts[1] / total

    story.append(Paragraph("<b>1) Probabilidades a priori</b>", styles['Heading2']))
    story.append(Paragraph(f"P(y = 1) = 5/8 = {prior_1:.3f}", styles['BodyText']))
    story.append(Paragraph(f"P(y = 0) = 3/8 = {prior_0:.3f}", styles['BodyText']))
    story.append(Spacer(1, 8 * mm))

    cond = {
        1: {
            'x1': {1: 4/5, 0: 1/5},
            'x2': {1: 1/5, 0: 4/5},
            'x3': {1: 1/5, 0: 4/5},
        },
        0: {
            'x1': {1: 1/3, 0: 2/3},
            'x2': {1: 1.0, 0: 0.0},
            'x3': {1: 1/3, 0: 2/3},
        },
    }

    story.append(Paragraph("<b>2) Frequências e probabilidades condicionais</b>", styles['Heading2']))
    freq_rows = [
        ["Classe", "P(x1=1|y)", "P(x2=1|y)", "P(x3=1|y)", "P(x1=0|y)", "P(x2=0|y)", "P(x3=0|y)"],
        ["y = 1", f"{cond[1]['x1'][1]:.3f}", f"{cond[1]['x2'][1]:.3f}", f"{cond[1]['x3'][1]:.3f}", f"{cond[1]['x1'][0]:.3f}", f"{cond[1]['x2'][0]:.3f}", f"{cond[1]['x3'][0]:.3f}"],
        ["y = 0", f"{cond[0]['x1'][1]:.3f}", f"{cond[0]['x2'][1]:.3f}", f"{cond[0]['x3'][1]:.3f}", f"{cond[0]['x1'][0]:.3f}", f"{cond[0]['x2'][0]:.3f}", f"{cond[0]['x3'][0]:.3f}"],
    ]
    freq_table = Table(freq_rows, colWidths=[20 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm])
    freq_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dfeaf7')),
        ('GRID', (0, 0), (-1, -1), 0.7, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
    ]))
    story.append(freq_table)
    story.append(Spacer(1, 8 * mm))

    story.append(Paragraph("<b>3) Regra do classificador Naive Bayes</b>", styles['Heading2']))
    story.append(Paragraph(
        "Para um cliente com características x = (x1, x2, x3), calculamos:<br/>"
        "P(y = 1 | x) ∝ P(y = 1) × P(x1|y = 1) × P(x2|y = 1) × P(x3|y = 1)<br/>"
        "P(y = 0 | x) ∝ P(y = 0) × P(x1|y = 0) × P(x2|y = 0) × P(x3|y = 0)",
        styles['BodyText']
    ))
    story.append(Spacer(1, 6 * mm))

    example_x = {'x1': 1, 'x2': 0, 'x3': 0}
    score_1 = 0.625 * 0.8 * 0.8 * 0.8
    score_0 = 0.375 * (1/3) * 0.0 * (2/3)
    # The formula above uses x2=0 for class 0 and x2=0 is 0, so class 0 is impossible in this feature combination.
    # This is a good demonstration of how strong features drive the decision.
    score_0 = 0.375 * (1/3) * 0.0 * (2/3)
    p1 = score_1 / (score_1 + score_0) if (score_1 + score_0) > 0 else 0.0
    p0 = 1.0 - p1

    story.append(Paragraph("<b>4) Exemplo de classificação</b>", styles['Heading2']))
    story.append(Paragraph(
        "Considere um cliente com x1 = 1, x2 = 0, x3 = 0.<br/>"
        "P(y = 1 | x) ∝ 0.625 × 0.8 × 0.8 × 0.8 = 0.320<br/>"
        "P(y = 0 | x) ∝ 0.375 × (1/3) × 0 × (2/3) = 0.000",
        styles['BodyText']
    ))
    story.append(Paragraph("Como o valor de P(y = 1 | x) é muito maior, o cliente é classificado como <b>inadimplente</b>.", styles['BodyText']))
    story.append(Spacer(1, 8 * mm))

    code = '''
import math

# Dados de treinamento
training = [
    {'y': 1, 'x1': 1, 'x2': 0, 'x3': 0},
    {'y': 1, 'x1': 1, 'x2': 1, 'x3': 0},
    {'y': 1, 'x1': 0, 'x2': 0, 'x3': 0},
    {'y': 1, 'x1': 1, 'x2': 0, 'x3': 1},
    {'y': 1, 'x1': 1, 'x2': 0, 'x3': 0},
    {'y': 0, 'x1': 0, 'x2': 1, 'x3': 1},
    {'y': 0, 'x1': 1, 'x2': 1, 'x3': 0},
    {'y': 0, 'x1': 0, 'x2': 1, 'x3': 0},
]

# Saber as classes
classes = sorted({row['y'] for row in training})

# Frequências condicionais
cond = {cls: {} for cls in classes}
for cls in classes:
    rows = [r for r in training if r['y'] == cls]
    for feature in ['x1', 'x2', 'x3']:
        cond[cls][feature] = {}
        for value in [0, 1]:
            cond[cls][feature][value] = sum(1 for r in rows if r[feature] == value) / len(rows)

# Probabilidades a priori
prior = {cls: sum(1 for r in training if r['y'] == cls) / len(training) for cls in classes}


def predict(cliente):
    scores = {}
    for cls in classes:
        score = prior[cls]
        for feature in ['x1', 'x2', 'x3']:
            score *= cond[cls][feature][cliente[feature]]
        scores[cls] = score
    total = sum(scores.values())
    return {cls: score / total for cls, score in scores.items()}

cliente = {'x1': 1, 'x2': 0, 'x3': 0}
print(predict(cliente))
'''

    story.append(Paragraph("<b>5) Implementação em Python</b>", styles['Heading2']))
    story.append(Preformatted(code, styles['Code']))

    doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=letter, rightMargin=20 * mm, leftMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
    print(f"PDF gerado em: {OUTPUT_PDF}")
