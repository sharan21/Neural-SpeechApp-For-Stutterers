This is the implememtation for the paper: https://www.semanticscholar.org/paper/Neural-Network-based-Speech-Assistance-tool-to-the-Narasimhan-Rao/24dd9e7d428a560b23fa5b8f1f08bc66ca945c37

# What is it?
This is a tool used for people who stutter, who are undergoing therapy, to help keep them in track with their speaking technique in real time situations. The technique this app monitors is a popular technique prescribed to stutterers and consists of 3 features:

1. Slow rate of speech (~80 words per minute)
2. Word by word speakin (there must be a small gap in between each word)
3. Each word must follow a sing song like prosody (please check documentation for more info)

It is know that generally while following these techniques, the degree of fluency increases significantly. This app helps ensure that the person sticks to this technique as much as possible but analysing every word spoken, feeding it to a specially trained neural network and deciding if each word is a) correctly spoken using the technique or b) incorrectly spoken. Statistics are built regarding the users speech and are stored for later use. This app is ideally for 'post therapy' use, where the user is already well informed of the technique and how to successfuly use it. This app is only web-based for now, there is no smartphone implementation of it yet.

# Requirements
Earphones with a mic are required
Run: pip3 install requirements.txt

# Usage
Run: ./openapp.sh

# Contact
Please report any issues on the issues section of this repo. The model is constantly being improved as more data accumulates. Email me at sharan.n21@gmail.com for the paper. Please feel free to contact me with feedback or ideas for improvement.




