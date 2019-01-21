# Speech-Assisting-App (Ongoing)
Monitors speech in real time and provides feedback to stammerer, based on features like Vocal modulation, length, rhythm. Trained using Tensorflow. 
# Refer Report 
Speech-Assisting-App/Documentation/project-synopsis.pdf 

# Idea and Working
Based on a technique used to attain fluency in stressfull situations called the "Long lengthning style", developed by Partha Bagchi, a mentor of mine and speech pathologist.
This technique essentially has 3 features:
1. Person talks slowly (60 words per minute)
2. Person uses correct natural "rhythm" (talking in a sing song manner)
3. Person thinks in a word by word manner (assists mental visualization)

All these 3 features can be monitored and fed to a tf graph and the output can be determined as 1 (proper technique used) or 0 (improper technique used).

If the proper technique is used, these is a very low chance that disfluency can occur. Thus this app makes sure that person is conscious of using the prescribed technique in the proper manner, alleviating stress in stressfull speaking situations. 


