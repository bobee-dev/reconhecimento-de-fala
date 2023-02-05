import speech_recognition as sp;
from translate import Translator;
import gtts
from playsound import playsound;



rec = sp.Recognizer()

with sp.Microphone(device_index=1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale alguma coisa: ")
    audio = rec.listen(mic)
    frase = rec.recognize_google(audio, language="pt-BR")
    print(frase)
    copiaFrase = Translator(from_lang="pt-BR", to_lang="english")
    respostaTraduzida = copiaFrase.translate(frase)
    print(f'Sua frase em inglês é: \033[35m{respostaTraduzida}\033[m')
