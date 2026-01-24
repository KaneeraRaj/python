import pyaudio,numpy as np,speech_recognition as sr
import matplotlib.pyplot as plt

RATE=1600
CHUNK=1024

def record (seconds):
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,
                  rate=RATE,input=True,frames_per_buffer=CHUNK)
    
    frames=[
        stream.read(CHUNK,exception_on_overflow=False)
        for _ in range(int(RATE/CHUNK*seconds))
        ]

    stream.stop_stream()
    stream.close()
    p.terminate()
    return b''.join(frames)

def  analyze(audio):
    samples=np.frombuffer(audio,np.int16)

    return{
        "duration":len(samples)/RATE,
        "avg":np.mean(np.abs(samples)),
        "max":np.max(np.abs(samples)),
        "samples":samples

    }

def transcribe(audio):
    try:
        r=sr.Recognizer()
        return r.recognize_google(sr.AudioData(audio,RATE,2))
    except:
        return "Not Clear"

def plot(a1,a2):
    plt.plot(a1["samples"],label="Recording 1")
    plt.plot(a2["samples"],label="Recording 2")
    plt.legend()
    plt.show()
    
print("Speak Normally....")
audio1=record(3)
s1=analyze(audio1)
text1=transcribe(audio1)

print("Speak Loudly....")
audio2=record(3)
s2=analyze(audio2)
text2=transcribe(audio2)

print("\n-----RESULTS-----")
print ("R1 Duration:",s1["duration"],"Average volume",s1["avg"])
print ("R1 text:",text1)
print ("R2 Duration:",s2["duration"],"Average volume",s2["avg"])
print ("R2 text:",text1)

plot(s1,s2)