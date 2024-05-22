from reading import read_heading
from gptAPI import Search
import re


para = '''Wrong thinking is the only problem in life Based on above part of bhavat gita create a real-life problem related to "Career and Work Problems" on 'Communication issues' which is answered from above but make sure my Solution has the below properties: (Part 1: Write the solution to the problem which is positive and boost morale) (Part 2: Solution based on the gist of the Bhagwat Gita quotes) (Part 3: Please share the Verse along with simple English Translation also from Bhagwat Geeta from which this data is pulled in below format. -Verse : -Meaning in English)'''

sub_heading = read_heading()


def find_words(para):
    words = re.findall(r"'(.*?)'", para)
    words = str(words)
    return words[2:-2]

found_word = find_words(para)


def replace_word(para,old_string,new_string):
    new_para = para.replace(old_string, new_string)
    
    return new_para

new_word = sub_heading[1]   

for i in sub_heading:
    new_para = replace_word(para,found_word,i)
    Search(new_para)


        