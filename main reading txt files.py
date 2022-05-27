# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#def read_file_content(filename):
    # [assignment] Add your code here 
 #   open("C:/Users/USER/Downloads/Reading-Text-Files/story.txt", 'r')
    
#  return "Hello World"

#def count_words():
 #   text = read_file_content("./story.txt")
    # [assignment] Add your code here

  #  return {"as": 10, "would": 20}

  #  import string

#  Read text from a file
with open("C:/Users/USER/Downloads/Reading-Text-Files/story.txt") as f:
        contents = f.read()
print(contents)
f.close()



# count the occurence of words in that text
fhand = open("C:/Users/USER/Downloads/Reading-Text-Files/story.txt")
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)