def generate_recommendations(score, positive, neutral, negative, engagement):

    recommendations = []

    if score >= 85:
        recommendations.append("🎉 Audience response is excellent. Continue your current content strategy.")
    elif score >= 70:
        recommendations.append("👍 Audience enjoys your content. Small improvements can boost performance.")
    else:
        recommendations.append("⚠️ Audience satisfaction is low. Review negative comments carefully.")

    if engagement >= 8:
        recommendations.append("🔥 Your engagement rate is excellent. Viewers are actively interacting.")
    elif engagement >= 4:
        recommendations.append("📈 Engagement is good. Encourage viewers to comment and share.")
    else:
        recommendations.append("💬 Ask more questions in your videos to increase engagement.")

    if len(negative) > len(positive):
        recommendations.append("🎤 Improve video quality and presentation based on audience feedback.")

    if len(neutral) > len(positive):
        recommendations.append("✨ Add more engaging hooks to convert neutral viewers into fans.")

    if len(positive) > len(negative):
        recommendations.append("❤️ Keep your current content style because your audience appreciates it.")

    recommendations.append("📅 Maintain a consistent upload schedule.")

    return recommendations