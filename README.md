# Audio Segmentation and Speech-to-Text Conversion
This Python script allows you to segment an audio file into smaller segments and convert the speech in each segment into text using the Google Speech Recognition API. The resulting text is then saved to an output file.

## Requirements
To run this script, you need to have the following dependencies installed:

speech_recognition library: Used for speech recognition and interacting with the Google Speech Recognition API.
pydub library: Used for audio file manipulation and processing.
numpy library: Required by pydub for audio processing.
Python 3.x

## Usage
1. Install the required dependencies by running the following command:
```python
pip install speechrecognition pydub numpy
```
2. Place your input audio file in the same directory as the script. Make sure the audio file is in WAV format..

3. Open the script in a Python IDE or text editor.

4. Modify the following variables in the script according to your needs:

- test_filename: Specify the name of your input audio file.
- VOICE_TEXT_FILENAME: Specify the name of the output text file.

5.  Run the script using the Python interpreter:
```python
python audio_segmentation.py
````
6. The script will segment the audio file into smaller segments, process each segment, and convert the speech to text using the Google Speech Recognition API. The resulting text will be saved to the specified output file.

7. Once the script finishes running, you can open the output file (VOICE_AS_TEXT.txt) to view the segmented speech converted to text.

## Limitations
The script currently supports only WAV audio files. You can modify the script to handle other audio formats if needed.
The Google Speech Recognition API is used for speech-to-text conversion, so an internet connection is required for the script to work properly.
## Notes
The script uses a segment length of 30 seconds by default. You can modify the segment_length_ms variable to change the segment length according to your requirements.
