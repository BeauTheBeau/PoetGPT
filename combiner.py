
import os

with open('poems.txt', 'w') as outfile:
    for directory in os.listdir('dataset/topics/'):
        for filename in os.listdir('dataset/topics/' + directory):
            with open('dataset/topics/' + directory + '/' + filename) as f:
                outfile.write(f.read())
                outfile.write("\n\n")

    for directory in os.listdir('dataset/forms/'):
        for filename in os.listdir('dataset/forms/' + directory):
            with open('dataset/forms/' + directory + '/' + filename) as f:
                outfile.write(f.read())
                outfile.write("\n\n")

print("Done!")
