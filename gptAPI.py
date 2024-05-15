from openai import OpenAI

Key = ""

client = OpenAI(api_key = Key)

def Search(para):
  input = para

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": "Assist me as per the Bhagvat Geeta"},
      {"role": "user", "content": input}
    ]
  )

  data = str(completion.choices[0].message.content)

  with open('Data.txt', "a") as file:
      file.write("Problem:- ")
      file.write("\n")
      file.write(input)
      file.write("\n\n")
      file.write("Solution:- ")
      file.write("\n")
      file.write(data)
      file.write("\n\n\n\n**************************************************************************************\n\n\n\n")
      
  print('done')
  
# Search()
