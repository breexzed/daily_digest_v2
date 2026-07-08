import extract



def news_ai_transform(source, headline,text):
    return f"""
    You are an elite intelligence analyst monitoring global events.
    Analyze the following report from {source}.
    
    HEADLINE: {headline}
    RAW TEXT: {text}
    
    TASK:
    Provide a hyper-dense, 2-sentence executive summary. 
    Focus strictly on geopolitical or situational impact. 
    Do not repeat the headline.

    Analyze the text for operational threats, supply chain disruptions, or security anomalies
    Output a single status: [LOW risk], [MEDIUM risk], or [HIGH risk], followed by a 1-sentence justification.

    You must format your response EXACTLY matching the markdown template below. 
    Do not alter the headers, wording, or bolding of the template structure.

    ### Executive Summary
    [Insert your dense 2-sentence summary here]

    ### Risk Assessment
    [Insert status: LOW, MEDIUM, or HIGH risk] - [Insert your threat analysis here]

    """

