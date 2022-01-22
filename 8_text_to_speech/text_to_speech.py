from gtts import gTTS
  

# The text that you want to convert to audio
mytext = 'I am a python programmer'
  
# Language in which you want to convert
language = 'en'
  
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file
myobj.save("voice.mp3")
