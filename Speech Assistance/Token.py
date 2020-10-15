import spacy
import re


class Tokenizer:
    def token_spacy(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        for entity in doc.ents:
            name = entity.text
            print(name, entity.label_)

    @staticmethod
    def time_token(speech):
        x = re.findall("[Dd]isplay" and "[Tt]ime", speech)
        x1 = re.findall("[Cc]urrent time", speech)
        x2 = re.findall('[Ww]hat' and '[Ii]s' and 'time', speech)
        if x or x1 or x2:
            send_time = "time"
            return send_time
        else:
            print("Repeat that again")

    @staticmethod
    def date_token(speech):
        x = re.findall("[Tt]oday's" and "[Dd]ate", speech)

        if x:
            send_date = "date"
            return send_date
        else:
            print("Repeat that again")


# t = Tokenizer()
# txt = "Peter is in living norfolk virginia"
# t.token_spacy(txt)

