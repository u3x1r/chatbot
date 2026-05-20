# chatbot
A lightweight, terminal-based Python chatbot interacting natively with the Google Gemini 2.5 Flash API via direct REST requests
# Live Gemini API CLI Chatbot

A lightweight, terminal-based chatbot application written in Python that establishes a continuous, interactive chat loop directly with Google's Gemini 2.5 Flash model. 

This repository serves as a clean, dependency-minimal starter template for developers looking to integrate the Gemini API into custom Python applications without relying on heavy third-party SDKs.

## Features

*   **Direct REST Integration:** Connects directly to Google's Generative Language API endpoints via standard HTTP POST requests.
*   **Continuous Chat Loop:** Runs an uninterrupted terminal session allowing back-and-forth user interaction until explicitly closed.
*   **Graceful Exception Handling:** Explicitly catches network failures (`requests.exceptions.RequestException`), API payload mutations (`KeyError`, `IndexError`), and sudden user exits (`Ctrl+C` / `KeyboardInterrupt`).
*   **Minimalist Design:** Only requires the standard `requests` library.

---

## How it Works under the Hood

The script avoids high-level wrapper libraries to keep the underlying architecture fully transparent:

1. **Payload Compilation:** It structures user input into the strict JSON hierarchy required by Google's developer endpoints:
   ```json
   {
     "contents": [
       {
         "parts": [{"text": "Your message here"}]
       }
     ]
   }
