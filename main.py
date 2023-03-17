import speech_recognition as sr
from translate import Translator

lang = 'fa-IR'
from_lang = 'Persian'
to_lang = 'English'

while True:
    print('')
    from_lang, lang = ('English', 'en-US') if lang == 'fa-IR' else ('Persian', 'fa-IR')
    to_lang = 'Persian' if to_lang == 'English' else 'English'

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak in', from_lang)
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing...')

            query = r.recognize_google(audio, language=lang)
            print(from_lang, ':', query)

            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(query)
            print(to_lang, ':', translation)

        except Exception as e:
            print('Unable to Recognize your voice; because:', e)
