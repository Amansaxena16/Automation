import os
import google.generativeai as genai

genai.configure(api_key="Chachu Paste Your Key Here!!")

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

  message = f"behave like a expert in bhagavad gita {input}"
  response = chat_session.send_message(message)

  with open('Data.txt', "a",encoding='utf-8') as file:
      file.write("Problem:- ")
      file.write("\n")
      file.write(input)
      file.write("\n\n")
      file.write("Solution:- ")
      file.write("\n")
      file.write(response.text)
      file.write("\n\n\n\n**************************************************************************************\n\n\n\n")
      
  print('done')
  
# Search()
