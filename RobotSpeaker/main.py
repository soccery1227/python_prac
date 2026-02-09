# for windows
import win32com.client  # pip install pywin32

if __name__ == '__main__':
    print("...Welcome to Robo Speaker created by Manleen...")

    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    speaker.Rate = 0  # -10 (slow) to +10 (fast)
    speaker.Volume = 100  # 0 to 100

    while True:
        text = input("Enter what do you want to say (q to quit): ")

        if text.lower() == 'q':
            speaker.Speak("Goodbye")
            break

        speaker.Speak(text)

'''
# for mac
import os

if __name__ == '__main__':
    print("...Welcome to Robo Speaker created by Manleen...")
    while True:
        x = input("Enter what do you want to say: ")
        if x == "q":
            break
        command = f"say {x}"
        os.system(command)    
'''


