from openai import OpenAI

Key = ""

client = OpenAI(api_key = Key)

def Search():
  input = ''' Wrong thinking is the only problem in life Based on above part of bhavat gita create a real-life problem related to "Family Relationships Problems" on "Communication issues"
 which is answered from above but make sure my Solution has the below properties: (Part 1: Write the solution to the problem which is positive and boost morale) (Part 2: Solution based on the gist of the Bhagwat Gita quotes) (Part 3: Please share the Verse in sanskrit(english) but write it into english language as it is from bhagvat geeta along with also from Bhagwat Geeta from which this data is pulled in below format.)'''
 

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": "Assist me as per the Bhagvat Geeta"},
      {"role": "user", "content": input}
    ]
  )

  data = str(completion.choices[0].message.content)
  
  with open('Data.txt', "a",encoding='utf-8') as file:
    file.write("Problem:- ")
    file.write("\n")
    file.write(input)
    file.write("\n\n")
    file.write("Solution:- ")
    file.write("\n")
    file.write(data)
    file.write("\n\n\n\n**************************************************************************************\n\n\n\n")
      
  print('done')
  
Search()