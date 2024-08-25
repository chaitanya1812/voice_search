# Voice Search

basic and simple voice google search. takes input query from user voice and then speaks out the details related to the query.

## Project Setup

step 1: navigate to voice_search folder
`cd path_to/voice_search`

step 2: create an conda environment using the environment.yml file. This will create the environment (speech_to_text) with all the required packages.
`conda env create -f environment.yml`

Note: you can change the env name "speech_to_text" in environment.yml to any other name like my_temp_env, dummy_env, etc.

step 3: activate the created environment
`conda activate speech_to_text`

step 5: make sure the python interpreter in the IDE is pointing to the one in created conda enviroement
typically found at this path: `/Users/$USER/anaconda3/envs/speech_to_text/bin/python`

step 6: now run the voice_search.py
`python src/voice_search.py`

Note: please say the query in high level like history of country, details about a specific product, etc. sharp questions are generally not answerable in a staightforward way.

step 7: say something you want to search when system says `Listening...`

step 8: just cross check the text
`Recognized Text: you_query_from_speech`

step 9: now get ready to listen...
