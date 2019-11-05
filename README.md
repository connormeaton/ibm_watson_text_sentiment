### ibm_nlu

This repository contains code to analyze sentiment and emotion from text using IBM Watson's NLU API. 

The code does the follow:
  - Input the final, utterance-based transcript for a couple ID as a pandas dataframe.
  - Isolate text (utterances) from the datarame and convert to a list.
  - Iterate through list, passing each utterance to the IBM API.
  - Store emotion and sentiment output for each utterance in a dictionary.
  - Append each dictionary to a list.
  - Create pandas dataframe where each row is an utterance containing 8 columns:
          - utterance text (string)
          - sentiment score (float) (-1-1)
          - sentiment label (string) (categorical [positive, negative, neutral])
          - anger (float)(0-1)
          - sadness (float)(0-1)
          - disgust (float)(0-1)
          - fear (float)(0-1)
          - joy (float)(0-1)
