import sys
import requests

# 1. Your official Gemini API Configuration
API_KEY = "YOUR API KEY HERE"

# We use gemini-2.5-flash because it's the recommended model for fast, responsive chat
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def get_api_response(user_message):
    """
    Sends the user's message directly to Google Gemini's web servers 
    and extracts the text reply.
    """
    headers = {
        "Content-Type": "application/json"
    }
    
    # This is the exact JSON structure the Gemini API looks for
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }
    
    try:
        # Fire the POST request across the web
        response = requests.post(API_URL, json=payload, headers=headers)
        
        # If the API key becomes invalid or a network block happens, this flags it
        response.raise_for_status()
        
        # Unpack the response data structure
        data = response.json()
        
        # Navigate through Google's response format to pull out the raw response text
        bot_reply = data["candidates"][0]["content"]["parts"][0]["text"]
        return bot_reply

    except requests.exceptions.RequestException as e:
        return f"Network Error: Unable to reach Gemini's servers. ({e})"
    except (KeyError, IndexError):
        return "Parsing Error: The server replied, but the data layout wasn't what we expected."

# 2. Continuous User Chat Loop
def start_bot():
    print("🤖 Live Gemini API Chatbot initialized!")
    print("Type your message and press Enter. (Type 'exit' to quit)")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ")
            
            # Check if the student wants to end the program
            if user_input.lower() in ['quit', 'exit']:
                print("Bot: Goodbye! Happy coding!")
                break
                
            # Don't send blank spaces to the API
            if not user_input.strip():
                continue
                
            # Get the real-time AI answer
            reply = get_api_response(user_input)
            print(f"\nBot: {reply}")

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    start_bot()