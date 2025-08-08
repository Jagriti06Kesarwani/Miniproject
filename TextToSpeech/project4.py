import os
print("HELLO I AM A ROBO SPEAKER!")
if __name__ == '__main__':
    print("Enter text (type 'q' to quit):")
    while True:
        x = input("You: ")
        if x.lower() == "q":
            os.system('powershell "Add-Type –AssemblyName System.Speech; '
                      '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'bye bye friends\')"')
            break
        command = f'powershell "Add-Type –AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)
