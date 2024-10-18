import speech_recognition as sr

r = sr.Recognizer()

print("Type 'exit' and press Enter to quit the program.")

while True:
    command = input("Press Enter to listen or type 'exit': ")

    if command.lower() == 'exit':
        print("Exiting the program.")
        break

    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
