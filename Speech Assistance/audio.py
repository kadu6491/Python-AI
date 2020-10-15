import pyttsx3
import speech_recognition as sr
# Setup the audio convertion initials
engine = pyttsx3.init()

# Set up the rate and voice character for the audio
en_voice_id = "com.apple.speech.synthesis.voice.Alex"
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)
engine.setProperty('voice', en_voice_id)


class AudioSetUp:

    def audio_date(self, d):
        engine.say("Today's Date is " + str(d))
        engine.runAndWait()

    def audio_time(self, h, m, z):
        if h < 12:
            engine.say("The time is " + str(h) + " " + str(m) + "AM" + str(z))
            engine.runAndWait()
        else:
            f = h - 12
            engine.say("The time is " + str(f) + " " + str(m) + "PM" + str(z))
            engine.runAndWait()

    def audio_weather(self, d, c, l, h):
        engine.say('''
                Today's weather is going to be {} with a current temperature {} .
                The low's will be around {} and the high will be around {} degrees
        '''.format(d, c, l, h))
        engine.runAndWait()

    def audio_search(self, find):
        engine.say("Here is what I found on the browser for " + find)
        engine.runAndWait()

    @staticmethod
    def audio_error():
        engine.say("Did not understand what you said")
        engine.runAndWait()


class Speaker:
    def speech(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Please say something")
            audio = r.listen(source)
            sh = ''

            try:
                sh = r.recognize_google(audio)
                print(sh)

            except Exception as e:
                error = AudioSetUp()
                error.audio_error()

            return sh



