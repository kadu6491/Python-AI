
from Token import *
from PrintData import *
from Mutator import *
from audio import *

s = Speaker()
show_time = DateAndTime()
speak_data = FindData()
audio_repeat = AudioSetUp()


def greetings():
    checktime = datetime.datetime.now()

    if checktime.hour < 12:
        engine.say("Good Morning, How may I assist you")
        engine.runAndWait()

    elif 12 <= checktime.hour < 18:
        engine.say("Good Afternoon, How may I assist you")
        engine.runAndWait()

    else:
        engine.say("Good Evening, How may I assist you")
        engine.runAndWait()
    # engine.say("Good")


class TrainMachine:
    @staticmethod
    def train_time():
        txt = "Display the current time"
        txt1 = "What is the current time"
        txt2 = "what time is it"

        tt = Tokenizer()
        pp = tt.time_token(txt2)

        print(pp)

        if pp == "time":
            speak_data.look_up_time()
        else:
            audio_repeat.audio_error()

    @staticmethod
    def train_date():
        speak_date = FindData()
        audio_repeat = AudioSetUp()
        txt = "What's today's date"

        tt = Tokenizer()
        dd = tt.date_token(txt)
        print("Today's " + dd)

        if dd == 'date':
            speak_date.look_up_date()
        else:
            audio_repeat.audio_error()

    def train_weather(self):
        speak_data.look_up_weather("Virginia Beach")

    def train_search(self):
        speak_data.search("Java")


class TestMachnine:
    def machine(self):
        m = TrainMachine()
        # greetings()
        sh = s.speech()

        if "time" in sh:
            m.train_time()

        elif "date" in sh:
            m.train_date()

        elif "weather" in sh:
            m.train_weather()

        elif "exit" or "goodbye" or "bye" or "close" in sh:
            engine.say("No problem, it was my pressure to assist. Goodbye")
            engine.runAndWait()
            exit()

        else:
            audio_repeat.audio_error()

        engine.say("Anything else you need")
        engine.runAndWait()



greetings()
while 1:
    # tr = TrainMachine
    # tr.train_time()
    # tr.train_date()

    tm = TestMachnine()
    tm.machine()