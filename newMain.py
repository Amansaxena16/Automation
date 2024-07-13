import re
import os
import google.generativeai as genai
import xlsxwriter
from reading import read_heading

# INSERTING DATA EXCEL SECTION START FROM HERE

# Initialize workbook and worksheet
workbook = xlsxwriter.Workbook('Bhagavad Gita.xlsx')
worksheet = workbook.add_worksheet('Chapter 1')

# Write headers
worksheet.write(0, 0, 'Questions')
worksheet.write(0, 1, 'Answers')

# Initialize row counter
row = 2

def insertIntoExcel(input, output):
    global row
    worksheet.write(row, 0, input)
    worksheet.write(row, 1, output)
    row += 1
    print('Done')

# AI SECTION START FROM HERE 
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

def main():
    # QUESTION GENERATION START FROM HERE
    questionList = []

    para = '''Wrong thinking is the only problem in life Based on above part of bhavat gita create a real-life problem related to "Career and Work Problems" on 'Communication issues' which is answered from above but make sure my Solution has the below properties: (Part 1: Write the solution to the problem which is positive and boost morale) (Part 2: Solution based on the gist of the Bhagwat Gita quotes) (Part 3: Please share the Verse along with simple English Translation also from Bhagwat Geeta from which this data is pulled in below format. -Verse : -Meaning in English)

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
    # here i am reading heading
    sub_heading = read_heading()

    # find word in para
    def find_words(para):
        words = re.findall(r"'(.*?)'", para)
        words = str(words)
        return words[2:-2]

    found_word = find_words(para)

    # Replace word function
    def replace_word(para, old_string, new_string):
        new_para = para.replace(old_string, new_string)
        return new_para

    new_word = sub_heading[1]   

    #Creating question and inserting into the list
    for i in sub_heading:
        new_para = replace_word(para, found_word, i)
        questionList.append(new_para)

    # Respond prompt to the ChatBot
    for question in questionList:
        response = chat_session.send_message(question)
        insertIntoExcel(question, response.text)
    
    # Close workbook to save changes
    workbook.close()

if __name__ == "__main__":
    main()
