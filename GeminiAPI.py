import os
import google.generativeai as genai
from excel import insertIntoExcel

genai.configure(api_key="PASTE YOUR API")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)

def Search(para):
  input = para

  message = f'''behave like a expert in bhagavad gita {input}
  For Example : 
  Question:
  A family is experiencing communication issues, leading to misunderstandings and conflicts. Members feel unheard and frustrated, which strains their relationships.

  Answer:
  In moments of discord, it is vital to remember the importance of calm and clear communication. Embrace the idea that every individual has their own perspective and feelings. By practicing empathy, patience, and openness, you can bridge the gaps in understanding and strengthen your familial bonds. Approach each conversation with the intention of mutual respect and love.

  Based on Bhagavad Gita Quotes:

  "Perform all your actions with your mind concentrated on the Divine, renouncing attachment and looking upon success and failure with an equal eye. Spirituality means equanimity." - Bhagavad Gita 2.48

  "One who is not disturbed by the incessant flow of desires—that enter like rivers into the ocean, which is ever being filled but is always still—can alone achieve peace, and not the person who strives to satisfy such desires." - Bhagavad Gita 2.70

  
  -Verse:  Bhagavad Gita, Chapter 2, Verse 47
  "karmany evadhikaras te ma phalesu kadachana
  ma karma-phala-hetur bhur ma te sango 'stv akarmani"

  -Meaning in English:

  One who performs duties without attachment, surrendering the results unto the Supreme Lord, is unaffected by sinful action, as the lotus leaf is untouched by water.
  '''
  
  # input_list = []
  # input_list.append(message)
  
  # for question in input_list:
  #   response = chat_session.send_message(message)
    
  
  # output_list = []
  # output_list.append(response.text)
  
  # insertIntoExcel(message,response.text)
  
  


