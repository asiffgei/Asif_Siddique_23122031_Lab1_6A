from google import genai

client = genai.Client(api_key="AIzaSyAifY3wS0COFVoo2l0ygtqX_UdvNro6CsA")


MODEL = "models/gemini-3.5-flash"


def travel_agent(user_input):

    prompt = f"""
You are a professional travel agent for Pakistan tourism.

Provide a well-structured travel plan with clear headings:

1. Destination Overview
2. Budget Travel Options (Bus, Train, Flight with approx cost in PKR)
3. Places to Visit (specific locations)
4. Food Suggestions (local dishes)
5. Money-Saving Tips

Make response detailed but easy for students.

User request: {user_input}

Travel Plan:
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text



print("Gemini Travel Agent Started (type 'exit' to stop)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye ")
        break

    try:
        reply = travel_agent(user)
        print("\nAgent:\n", reply, "\n")

    except Exception as e:
        print("Error:", e)