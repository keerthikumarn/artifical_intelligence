'''
Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
'''

def count_lines_and_words(file):
   line_count = 0
   word_count = 0
   with open(file, 'r', encoding='utf-8') as file:
       for line in file:
          line_count += 1
          word_count += len(line.split())
   return line_count, word_count
   

lines, words = count_lines_and_words("obama_speech.txt")
print("No. of lines: ", lines)
print("No. of words: ", words)
