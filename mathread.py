import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"math-read-3d2556162d8a.json"

client = vision.ImageAnnotatorClient()

# file_name = 'img8.jpg'
# image_path = f'/Users/butterchicken/desktop/dubhacks19/images' 
# curr_url = 'https://www.wikihow.com/images/thumb/3/3d/Solve-Two-Step-Algebraic-Equations-Step-1-Version-3.jpg/aid17666-v4-728px-Solve-Two-Step-Algebraic-Equations-Step-1-Version-3.jpg'

def detectText(url):
	# with io.open(img, 'rb') as image_file:
	#     content = image_file.read()

	# # construct an iamge instance
	# img = vision.types.Image(content=content)

	# or we can pass the image url
	img_url = url
	image = vision.types.Image()
	image.source.image_uri = img_url
	# annotate Image Response
	response = client.text_detection(image=image)  # returns TextAnnotation
	df = pd.DataFrame(columns=['locale', 'description'])
	texts = response.text_annotations

	for text in texts:
	    df = df.append(
	        dict(
	            locale=text.locale,
	            description=text.description
	        ),
	        ignore_index=True
	    )
	return df['description'][0]
	#return df

#print text
#print(detectText(curr_url))



##############text to speech

#!/usr/bin/env python



# Copyright 2018 Google Inc. All Rights Reserved.

#

# Licensed under the Apache License, Version 2.0 (the "License");

# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at

#

#      http://www.apache.org/licenses/LICENSE-2.0

#

# Unless required by applicable law or agreed to in writing, software

# distributed under the License is distributed on an "AS IS" BASIS,

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and

# limitations under the License.



"""Google Cloud Text-To-Speech API sample application .

Example usage:

    python quickstart.py

"""





def run_quickstart(url):

    # [START tts_quickstart]

    """Synthesizes speech from the input string of text or ssml.

    Note: ssml must be well-formed according to:

        https://www.w3.org/TR/speech-synthesis/

    """

    from google.cloud import texttospeech



    # Instantiates a client

    client = texttospeech.TextToSpeechClient()



    # Set the text input to be synthesized

    synthesis_input = texttospeech.types.SynthesisInput(text=detectText(url))



    # Build the voice request, select the language code ("en-US") and the ssml

    # voice gender ("neutral")

    voice = texttospeech.types.VoiceSelectionParams(

        language_code='en-US',

        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)



    # Select the type of audio file you want returned

    audio_config = texttospeech.types.AudioConfig(

        audio_encoding=texttospeech.enums.AudioEncoding.MP3)



    # Perform the text-to-speech request on the text input with the selected

    # voice parameters and audio file type

    response = client.synthesize_speech(synthesis_input, voice, audio_config)



    # The response's audio_content is binary.

    with open('output.mp3', 'wb') as out:

        # Write the response to the output file.

        out.write(response.audio_content)

        print('Audio content written to file "output.mp3"')

    # [END tts_quickstart]

run_quickstart(curr_url)

 