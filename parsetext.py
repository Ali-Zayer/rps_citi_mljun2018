# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:29:52 2018

@author: Balasubramaniam
"""

import Algorithmia

#parsing text
input = {
  "src": """she was shocked and deeply saddened by Mr. Bukhari's sudden demise. 
  The scourge of terror has reared its ugly head on the eve of Eid. 
  I strongly condemn this act of mindless violence & pray for his soul to rest in peace. 
  My deepest condolences to his family, she tweeted.""",
  "format": "tree",
  "language": "english"
}
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('deeplearning/Parsey/1.1.0')
print(algo.pipe(input).result)

#a given sentence may be 45% happy, 23% sad, 89% excited, and 55% hopeful.
input = {
  "document": "I really love to travel!"
}
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('nlp/SentimentAnalysis/1.0.4')
print(algo.pipe(input).result)

#language identification

input = {
  "sentence": "हैलो, मैं अंग्रेजी बोल रहा हूँ। क्या आप अनुमान लगा सकते हैं कि मैं किस भाषा में बात कर रहा हूं?"
}
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('nlp/LanguageIdentification/1.0.0')
print(algo.pipe(input).result)

input = {
  "sentence": "வணக்கம், நான் ஆங்கிலம் பேசுகிறேன். நான் எந்த மொழியில் பேசுகிறேன் என்று யூகிக்க முடியுமா?"
}
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('nlp/LanguageIdentification/1.0.0')
print(algo.pipe(input).result)

#auto tag
input = "A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending. We propose a solution to the double-spending problem using a peer-to-peer network. The network timestamps transactions by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work. The longest chain not only serves as proof of the sequence of events witnessed, but proof that it came from the largest pool of CPU power. As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers. The network itself requires minimal structure. Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone."
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('nlp/AutoTag/1.0.1')
print(algo.pipe(input).result)

# Named Entity Recognition.
input = {
  "document": "Jim went to Stanford University, Tom went to the University of Washington. They both work for Microsoft."
}
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
print(algo.pipe(input).result)

#summarizer

input = "A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending. We propose a solution to the double-spending problem using a peer-to-peer network. The network timestamps transactions by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work. The longest chain not only serves as proof of the sequence of events witnessed, but proof that it came from the largest pool of CPU power. As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers. The network itself requires minimal structure. Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone."
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('nlp/Summarizer/0.1.7')
print(algo.pipe(input).result)

#parts of speech
input = "This is a sample text. More sample text. Banana."
client = Algorithmia.client('simbkmpSACnKPXl5AAr6vewxsd21')
algo = client.algo('StanfordNLP/PartofspeechTagger/0.1.0')
print(algo.pipe(input).result)

