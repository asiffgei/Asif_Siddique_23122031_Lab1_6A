"""
===============================================
     AI PHISHING DETECTION AGENT - LAB 2
===============================================

An AI-powered URL Safety Checker

User enters a URL, the program sends it to
Gemini AI, and the AI analyzes the URL for
possible phishing indicators.

The agent provides:
    • Classification
    • Risk Level
    • Security Analysis
    • Reasons
    • Safety Recommendation

This is an AI-based extension of Lab 1.
===============================================
"""

from google import genai


# --------------------------------------------
# Gemini AI Configuration
# --------------------------------------------

client = genai.Client(api_key="MyAPIKeyHere")  # Replace with your actual API key

MODEL = "models/gemini-3.5-flash"


# --------------------------------------------
# AI Phishing Detection Agent
# --------------------------------------------

def phishing_agent(url):

    prompt = f"""
You are an AI-Based Phishing Detection Agent.

Your job is to analyze the URL provided by the user
and determine whether it appears to be:

🟢 LEGITIMATE
🟡 SUSPICIOUS
🔴 PHISHING

Analyze the URL using these indicators:

• HTTPS usage
• URL length
• Domain name
• IP address instead of domain
• Suspicious keywords
• Special characters
• Subdomains
• Suspicious URL paths
• Suspicious parameters
• Brand impersonation
• Unusual domain structure
• Other phishing indicators

IMPORTANT:
- Do not open or visit the URL.
- Analyze only the URL text.
- HTTPS does NOT automatically mean a website is safe.
- Do not claim 100% certainty.
- If there is not enough evidence, use SUSPICIOUS.
- Explain your reasoning in simple language.

Return the result in exactly this format:

========================================
       AI PHISHING DETECTION REPORT
========================================

🔗 URL:
{url}

🤖 CLASSIFICATION:
[LEGITIMATE / SUSPICIOUS / PHISHING]

⚠️ RISK LEVEL:
[LOW / MEDIUM / HIGH / CRITICAL]

----------------------------------------
🔍 URL ANALYSIS
----------------------------------------

🔐 HTTPS:
Explain whether HTTPS is being used.

🌐 DOMAIN:
Analyze the domain name and structure.

📏 URL LENGTH:
Comment on whether the URL appears unusually long.

📡 IP ADDRESS:
State whether an IP address is being used instead
of a normal domain.

🚨 SUSPICIOUS KEYWORDS:
Identify suspicious words such as:
login, verify, secure, account, update, bank, etc.

🔣 SPECIAL CHARACTERS:
Identify unusual or excessive special characters.

📂 URL PATH:
Analyze the path and parameters for suspicious patterns.

🏢 BRAND IMPERSONATION:
Determine whether the URL appears to imitate a
known company, bank, social media platform, etc.

----------------------------------------
🧠 REASONS
----------------------------------------

List the most important reasons for your classification.

----------------------------------------
🛡️ SECURITY RECOMMENDATION
----------------------------------------

Give practical advice to the user.

If the URL is PHISHING or HIGH/CRITICAL risk,
clearly warn the user not to enter:

• Passwords
• OTPs
• Bank details
• Credit/debit card information
• Personal information

========================================

AI Detection Result:
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


# --------------------------------------------
# Main Program
# --------------------------------------------

def main():

    print("""
===============================================
       🤖 AI PHISHING DETECTION AGENT
===============================================

🔍 Analyze suspicious URLs using Gemini AI

Enter a URL to analyze.
Type 'exit' to stop the program.

===============================================
""")

    while True:

        url = input("🔗 Enter URL: ").strip()

        # ---- Exit Program ----
        if url.lower() == "exit":
            print("\n👋 Goodbye! Stay safe online.\n")
            break

        # ---- Empty Input Check ----
        if not url:
            print("\n⚠️ Please enter a URL.\n")
            continue

        try:

            print("\n🔄 Analyzing URL with AI...")
            print("⏳ Please wait...\n")

            result = phishing_agent(url)

            print(result)
            print()

        except Exception as e:

            print("\n❌ Error:", e)
            print("Please check your API key or internet connection.\n")


# --------------------------------------------
# Program Start
# --------------------------------------------

if __name__ == "__main__":
    main()