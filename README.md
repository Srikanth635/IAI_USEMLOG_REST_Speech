## Speech To Text Transcription in Unreal Engine (RobCoG VR)

### Different Approaches

* **Sphinx Based Plugin**

  GIT : [Sphinx Unreal Engine Plugin](https://github.com/shanecolb/sphinx-ue4)

  _Acoustic Model_ : Contains a statistical representation of the distinct sounds for every word in vocab and each sound corresponds to a phoneme
  _Language Model_ : Contains list of words and their probability of occurrence in sequence

  ![](Documentation/Sphinx_folder_structure.jpg)
  ![](Documentation/Sphinx_phonemes.jpg)</br>
  Fig. (a) Folder structure inside content/model directory (b) Phonemes inside the vocab

  ![](Documentation/Sphinx_blueprint1.jpg)
  ![](Documentation/Sphinx_blueprint2.jpg)</br>
  Fig. (a) Setting Probability tolerance for Recognised phrases (b) Reading and Displaying Recognised text

  ![](Documentation/Sphinx_working.jpg)</br>
  Fig. Overview of Sphinx plugin Speech to Text operation

  _Drawbacks_: 
    * Need to add phonemes (vocabulary) for the words to get recognised
    * Performance is not good for text with 2 or more words
</br>
</br>

* **Whisper Speech-to-Text Unreal Engine Plugin**
  
  Reference : [Whisper Cpp](https://github.com/ggerganov/whisper.cpp)</br>
  GIT : [../blob/main/SpeechRecognition.zip](https://github.com/Srikanth635/IAI/blob/main/SpeechRecognition.zip)

  _Libraries Used_:
    * SDL2
    * Whisper (C++)
    * Standard Library C++ 17
    * Containers : Array, Vector, Map, Set
    * Streams : fstream, iostream, sstream
    * Concurrency : thread, mutex, atomic
 
  ![](Documentation/Whisper_plugin_build.jpg)</br>
  Fig. Code snippet inside Build.cs of speech-to-text unreal engine plugin

  Inside 'SpeechRecognition\Source\SpeechRecognition\Private\ MySpeechWorker ', functions to record audio, scaling, filtering are found.

  Processed audio is passed on to  whisper network to get transcripted text as output.

  ![](Documentation/Whisper_plugin_blueprint.jpg)</br>
  Fig. Code snippet to retrieve audio buffer and invoke whisper for transcriptions

  _Drawbacks_: 
    * Speed : The speed of transciption is greater than 8 secs which is not reliable
    * Accuracy : Obtained transcriptions doesnt match the speaker utterances always

* **REST API (Unreal Engine) – Flask**

  GIT (USemLog) : [../USemLog/tree/SpeechRecord](https://github.com/AbhijitVyas/USemLog/tree/SpeechRecord)</br>
  GIT (Flask Python file) : [../IAI_USEMLOG_REST_Speech/blob/master/voice.py](https://github.com/Srikanth635/IAI_USEMLOG_REST_Speech/blob/master/voice.py)</br>

  * _FLASK_ :
    * Flask, a lightweight framework for building web applications in Python
    * Used Python’s PyAudio to read in audio data with required format, rate etc.,
    * Used routes to map URLs to functions that handle the requests
    * Listened for incoming HTTP requests and responds with appropriate HTTP responses (transcriptions)
    
  * _Unreal REST API_ :
    * Used Unreal engine’s C++ HTTP modules to raise API requests (start and stop recordings)
    * Used parsing libraries (JSON) to parse the received response from flask

  _Libraries and Tools Used_ : 
    * Unreal Engine (4.27,5.1.1)
    * USemlog Plugin
    * C++ Libraries (STL:Containers, JSON, HTTP)
    * PyCharm (Flask API)
    * Python Libraries (PyAudio, Whisper, os, wave, datetime, torch, threading)
 
  ![](Documentation/Whisper_Flask_working.jpg)</br>
  Fig. Overview of Speech to Text Operation in ‘RobCoG’ using FLASK API

  ![](Documentation/Whisper_Flask_blueprint1.jpg)</br>
  Fig. Code snippet of variables to facilitate controller mappings
  
  ![](Documentation/Whisper_Flask_blueprint2.jpg)</br>
  Fig. Code snippet of controller mappings to functions
  
  ![](Documentation/Whisper_Flask_blueprint3.jpg)</br>
  Fig. Code snippet of mapped functions calls definition

  ![](Documentation/Whisper_Flask_blueprint4.jpg)</br>
  Fig. Code snippet of function to send start audio signal API request

  ![](Documentation/Whisper_Flask_blueprint5.jpg)</br>
  Fig. Code snippet of function to send stop audio signal API request

  
