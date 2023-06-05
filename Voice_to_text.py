import speech_recognition as sr
from pydub import AudioSegment
import numpy as np
import os

test_filename = "voice_test.wav"
VOICE_TEXT_FILENAME = "VOICE_AS_TEXT.txt"

# initialize the recognizer
r = sr.Recognizer()

def recognize_from_file(filename):
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        try:
            text = r.recognize_google(audio_data, language="fr-FR")
            return text 
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# load the audio file using pydub
audio = AudioSegment.from_wav(test_filename)

# define segment length in milliseconds
segment_length_ms = 30000

# get the total duration of the audio file in milliseconds
audio_duration_ms = len(audio)

# loop through the audio file, segmenting and processing each segment
for i, start_time in enumerate(range(0, audio_duration_ms, segment_length_ms)):
    # calculate the end time for the segment
    end_time = start_time + segment_length_ms
    if end_time > audio_duration_ms:
        end_time = audio_duration_ms
    
    # extract the segment and save it to a new file
    segment = audio[start_time:end_time]
    segment_filename = f"segment_{i+1}.wav"
    segment.export(segment_filename, format="wav")
    
    # recognize speech in the segment and write the result to the output file
    text = recognize_from_file(segment_filename)
    if text:
        with open(VOICE_TEXT_FILENAME, "a") as f:
            f.write(f"Segment {i+1}: {text}\n")
        
        # Remove temporary segment file
        os.remove(segment_filename)
