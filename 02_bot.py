import pyautogui
import time
import pyperclip
import openai
import os


os.environ["OPENAI_API_KEY"] = "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"  # Replace with your new API key

# Initialize OpenAI client securely
client = openai.OpenAI()


# check user
def is_last_message_from_sender(chat_log, sendername="Omkar Chavan"):
    message=chat_log.strip().split("/2025]") [-1]
    if sendername in message:
        return True
    return False

    # for message in reversed(message):
    #     parts=message.split(": ",2)
    #     if len(parts) >=3:
    #         timestamp, sender, content=parts
    #         if sender.strip()== sendername:
    #             return True
    #         else:
    #             return False
            
pyautogui.click(1145,1157)  
time.sleep(1)  # Wait for UI to respond

while True:
    # Wait for 2 seconds before starting (optional, to switch to the right window)
    time.sleep(2)

    # Click on the  what app icon at (1222,1168)

    # Drag from (548,163) to (1884,1100) to select text
    # 691,226  to 1834,1083
    pyautogui.moveTo(691,226)    
    pyautogui.dragTo(1834,1083, duration=1, button='left')
    time.sleep(1)

    # Copy to clipboard     
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click()
    time.sleep(1)

    # Get clipboard data
    Chat_history = pyperclip.paste()
    print(Chat_history)
    
    if is_last_message_from_sender(Chat_history):
        # Make a request
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Person name Jay who speaks hindi , gujarati as well as english  but give ans in english text. You are  from India and you are  a coder. You analyzed chat history and respond like jay. Output should be next chat response as jay and remove the timestamp from the respone and give ans in hindi but in english text  "},
                {"role": "user", "content": Chat_history}
            ]
        )

        #  assistant's response
        response=completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(904, 1138)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Press Enter
        pyautogui.press('enter')
