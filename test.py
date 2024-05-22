import os
import google.generativeai as genai

genai.configure(api_key="")

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
message = '''Wrong thinking is the only problem in life Based on above part of bhavat gita create a real-life problem related to "Career and Work Problems" on 'Communication issues' which is answered from above but make sure my Solution has the below properties: (Part 1: Write the solution to the problem which is positive and boost morale) (Part 2: Solution based on the gist of the Bhagwat Gita quotes) (Part 3: Please share the Verse along with simple English Translation also from Bhagwat Geeta from which this data is pulled in below format. -Verse : -Meaning in English) '''

response = chat_session.send_message(message)

# print(response.text)

  
with open('test.txt', "a",encoding='utf-8') as file:
  file.write("Problem:- ")
  file.write("\n")
  file.write(message)
  file.write("\n\n")
  file.write("Solution:- ")
  file.write("\n")
  file.write(response.text)
  file.write("\n\n\n\n**************************************************************************************\n\n\n\n")
      
  print('done')
  
