import speech_recognition as sr
r = sr.Recognizer()

def my_stt(audio) :
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)
    mySpeech = r.recognize_google(audio_data, language='ko', show_all=True)
    try :
        return mySpeech
    except sr.UnknownValueError:
        print("Google 음성 인식이 오디오를 이해할 수 없습니다.")
    except sr.RequestError as e:
        print("Google 음성 인식 서비스에서 결과를 요청할 수 없습니다.; {0}".format(e))