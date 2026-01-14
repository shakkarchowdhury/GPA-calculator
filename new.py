import os
import time
import openai

# ---------------- CONFIG ----------------
openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key
voice_name = "Alex"              # macOS voice (Alex, Victoria, Fred, etc.)

# ---------------- HELPERS ----------------
def speak(text):
    """Say text using macOS TTS and print to terminal."""
    print(f"Jarvis > {text}")
    os.system(f'say -v {voice_name} "{text}"')

def ai_response(user_input):
    """Generate AI response using OpenAI GPT."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI error: {e}"

def execute_command(user_input):
    """Check for predefined system commands."""
    user_input = user_input.lower()
    
    if "time" in user_input:
        return time.strftime("It is %H:%M now.")
    elif "date" in user_input:
        return time.strftime("Today is %A, %B %d, %Y.")
    elif "open chrome" in user_input:
        os.system("open -a 'Google Chrome'")
        return "Opening Chrome."
    elif "open safari" in user_input:
        os.system("open -a 'Safari'")
        return "Opening Safari."
    elif "play music" in user_input:
        os.system("afplay ~/Music/song.mp3")  # replace with your music file path
        return "Playing music."
    elif "exit" in user_input:
        return "exit"
    else:
        return None

# ---------------- MAIN LOOP ----------------
print("Jarvis online. Type 'exit' to quit.")

while True:
    user = input("You > ")
    
    # First check system commands
    cmd_result = execute_command(user)
    
    if cmd_result == "exit":
        speak("Goodbye. Jarvis shutting down.")
        break
    elif cmd_result:
        speak(cmd_result)
    else:
        # Fallback to AI response
        response = ai_response(user)
        speak(response)
