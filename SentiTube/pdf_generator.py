from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.HexColor("#557CC3")

heading = styles["Heading2"]
heading.textColor = colors.HexColor("#5978B1")

normal = styles["BodyText"]

small = styles["BodyText"]
small.fontSize = 12


def create_pdf(
    filename,
    details,
    score,
    positive,
    neutral,
    negative,
    keywords,
    summary,
    recommendations
):

    pdf = SimpleDocTemplate(
        filename,
        pagesize=(8.27 * inch, 11.69 * inch)
    )

    elements = []

    # =====================================================
    # TITLE
    # =====================================================

    elements.append(
        Paragraph(
            "🎬 <b>SentiTube</b>",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "<b>AI Creator Analytics Report</b>",
            title_style
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    # =====================================================
    # VIDEO DETAILS
    # =====================================================

    video_data = [

        ["📺 Video",
         details["title"]],

        ["👤 Channel",
         details["channel"]],

        ["👀 Views",
         f'{int(details["views"]):,}'],

        ["👍 Likes",
         f'{int(details["likes"]):,}'],

        ["💬 Comments",
         f'{int(details["comments"]):,}'],

        ["📅 Published",
         details["published"]]

    ]

    table = Table(
        video_data,
        colWidths=[1.6*inch,5.8*inch]
    )

    table.setStyle(
        TableStyle([

            ('BACKGROUND',(0,0),(0,-1),
             colors.HexColor("#0F62FE")),

            ('TEXTCOLOR',(0,0),(0,-1),
             colors.white),

            ('BACKGROUND',(1,0),(1,-1),
             colors.whitesmoke),

            ('GRID',(0,0),(-1,-1),
             0.5,
             colors.grey),

            ('BOTTOMPADDING',(0,0),(-1,-1),8)

        ])
    )

    elements.append(table)

    elements.append(
        Spacer(1,15)
    )

    # =====================================================
    # CREATOR SCORE
    # =====================================================

    if score >= 90:

        rating = "★★★★★"

        verdict = "Excellent"

    elif score >= 75:

        rating = "★★★★☆"

        verdict = "Very Good"

    elif score >= 60:

        rating = "★★★☆☆"

        verdict = "Good"

    else:

        rating = "★★☆☆☆"

        verdict = "Needs Improvement"
        score_table = Table([
    [
        Paragraph(
            f"""
            <b>❤️ Creator Health Score</b><br/><br/>
            <font color="green" size="24">
            {score}%
            </font>
            """,
            normal
            ),
            Paragraph(
                f"""
                <b>⭐ Creator Rating</b><br/><br/>
                 <font color="gold" size="22">
                {rating}
                 </font>
                 <br/><br/>
                 <b>{verdict}</b>
                 """,normal
                )
                ]
                ],
                colWidths=[3.6*inch, 3.6*inch]
                )
        score_table.setStyle(
            TableStyle([
                ('BACKGROUND',(0,0),(-1,-1),
                 colors.HexColor("#F8FAFC")),
                 ('BOX',(0,0),(-1,-1),1,
                  colors.lightgrey),
                  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                  ('BOTTOMPADDING',(0,0),(-1,-1),
                   18)
                   ])
                   )
        elements.append(score_table)
        elements.append(
            Spacer(1,15)
            )
    total = len(positive)+len(neutral)+len(negative)
    p = round(len(positive)/total*100,1)
    n = round(len(neutral)/total*100,1)
    neg = round(len(negative)/total*100,1)
    sentiment = [
            ["😊 Positive",f"{p}%"],

            ["😐 Neutral",f"{n}%"],

            ["😡 Negative",f"{neg}%"]
            ]
    sentiment_table = Table(
            sentiment,
            colWidths=[5*inch,2*inch]
            )
    sentiment_table.setStyle(
            TableStyle([
                ('BACKGROUND',(0,0),(-1,0),
                 colors.HexColor("#D9F99D")),
                 ('GRID',(0,0),(-1,-1),
                  0.5,
                  colors.grey),
                  ('BOTTOMPADDING',(0,0),(-1,-1),8)
                  ]))
    elements.append(
            Paragraph(
                "<b>📊 Audience Sentiment</b>",
                heading
                )
                )
    elements.append(sentiment_table)
    elements.append(
            Spacer(1,15)
            )
    elements.append(
            Paragraph(
                "<b>🔥 Top Audience Topics</b>",
                heading
                )
                )
    keyword_text = ", ".join(keywords[:5])
    elements.append(
            Paragraph(
                keyword_text,
                normal
                )
                )
    elements.append(
            Spacer(1,12)
            )

    # =====================================================
    # AI SUMMARY
    # =====================================================

    elements.append(
        Paragraph(
            "<b>🤖 AI Summary</b>",
            heading
        )
    )

    summary_table = Table(
        [[Paragraph(summary, normal)]],
        colWidths=[7.2*inch]
    )

    summary_table.setStyle(

        TableStyle([

            ('BACKGROUND',(0,0),(-1,-1),
             colors.HexColor("#EEF6FF")),

            ('BOX',(0,0),(-1,-1),
             1,
             colors.HexColor("#0F62FE")),

            ('BOTTOMPADDING',(0,0),(-1,-1),12),

            ('TOPPADDING',(0,0),(-1,-1),12),

            ('LEFTPADDING',(0,0),(-1,-1),12),

            ('RIGHTPADDING',(0,0),(-1,-1),12)

        ])

    )

    elements.append(summary_table)

    elements.append(
        Spacer(1,12)
    )

    # =====================================================
    # AI RECOMMENDATIONS
    # =====================================================

    elements.append(
        Paragraph(
            "<b>💡 AI Recommendations</b>",
            heading
        )
    )

    rec_text = ""

    for r in recommendations[:4]:

        rec_text += f"• {r}<br/>"

    rec_table = Table(
        [[Paragraph(rec_text, normal)]],
        colWidths=[7.2*inch]
    )

    rec_table.setStyle(

        TableStyle([

            ('BACKGROUND',(0,0),(-1,-1),
             colors.HexColor("#F0FDF4")),

            ('BOX',(0,0),(-1,-1),
             1,
             colors.green),

            ('BOTTOMPADDING',(0,0),(-1,-1),12),

            ('TOPPADDING',(0,0),(-1,-1),12),

            ('LEFTPADDING',(0,0),(-1,-1),12)

        ])

    )

    elements.append(rec_table)

    elements.append(
        Spacer(1,12)
    )

    # =====================================================
    # FINAL VERDICT
    # =====================================================

    elements.append(
        Paragraph(
            "<b>🏆 Final Verdict</b>",
            heading
        )
    )

    if score >= 90:

        verdict = """
<b>Excellent Performance</b><br/><br/>

The audience responded extremely well to this video.

Continue producing similar content while maintaining
consistent quality and engagement.
"""

    elif score >= 75:

        verdict = """
<b>Very Good Performance</b><br/><br/>

Audience feedback is highly positive.

Minor improvements can further increase engagement.
"""

    elif score >= 60:

        verdict = """
<b>Good Performance</b><br/><br/>

The content performed reasonably well.

Focus on audience feedback to improve future videos.
"""

    else:

        verdict = """
<b>Needs Improvement</b><br/><br/>

Audience response indicates that improvements
are required in content quality and presentation.
"""

    verdict_table = Table(
        [[Paragraph(verdict, normal)]],
        colWidths=[7.2*inch]
    )

    verdict_table.setStyle(

        TableStyle([

            ('BACKGROUND',(0,0),(-1,-1),
             colors.HexColor("#FFF7ED")),

            ('BOX',(0,0),(-1,-1),
             1,
             colors.orange),

            ('BOTTOMPADDING',(0,0),(-1,-1),12),

            ('TOPPADDING',(0,0),(-1,-1),12),

            ('LEFTPADDING',(0,0),(-1,-1),12)

        ])

    )

    elements.append(verdict_table)

    elements.append(
        Spacer(1,18)
    )

    # =====================================================
    # FOOTER
    # =====================================================

    footer = Paragraph(

        """
<para align='center'>

<font size='9' color='grey'>

Generated by <b>SentiTube AI Creator Analytics Platform</b>

<br/>

Developed by <b>Srinithi J</b>

</font>

</para>
""",

        small

    )

    elements.append(footer)
    pdf.build(elements)