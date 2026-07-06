from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(filename, score, p, n, ne, total):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    title = Paragraph(
        "<b><font size=24 color='#E53935'>SentiTube Report</font></b>",
        styles["Title"]
    )

    story.append(title)

    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph(
            "<b>AI Creator Insight Platform</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 0.2 * inch))

    data = [

        ["Metric", "Value"],

        ["Creator Health Score", f"{score}%"],

        ["Positive Comments", str(p)],

        ["Neutral Comments", str(ne)],

        ["Negative Comments", str(n)],

        ["Total Comments", str(total)]

    ]

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),HexColor("#E53935")),

        ("TEXTCOLOR",(0,0),(-1,0),"white"),

        ("GRID",(0,0),(-1,-1),1,"grey"),

        ("BACKGROUND",(0,1),(-1,-1),HexColor("#F8F9FA")),

        ("BOTTOMPADDING",(0,0),(-1,0),10)

    ]))

    story.append(table)

    story.append(Spacer(1,0.3*inch))

    if score>=80:

        result="Excellent Audience Response"

    elif score>=60:

        result="Good Audience Response"

    elif score>=40:

        result="Mixed Audience Response"

    else:

        result="Needs Improvement"

    story.append(

        Paragraph(

            "<b>AI Conclusion</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph(result,styles["BodyText"])

    )

    story.append(Spacer(1,0.3*inch))

    story.append(

        Paragraph(

            "<b>Recommendations</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph("""

• Continue engaging with your audience.<br/>

• Improve content quality.<br/>

• Respond to viewer feedback.<br/>

• Upload consistently.<br/>

• Monitor audience sentiment regularly.

""",

styles["BodyText"])

)

    doc.build(story)