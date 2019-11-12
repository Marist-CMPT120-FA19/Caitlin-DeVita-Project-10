#Caitlin De Vita
#caitlin.devita1@marist.edu
#Automated Censor Program


def censor(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word=word[:i] + '*' + word [i+1:]
    return word



def main():
    file= input ("Enter the file name of what you want to censor: ")
    text= open(file, 'r')
    words_file= input ("Enter the file name that contains the censord words: ")
    censored= open(words_file, 'r')
    censorWords= censored.read().split()

    censoredText= ""
    for line in text:
        words=line.split()

        for i in range(len(words)):
            word= ""
            for letter in words [i]:
                if letter.isalpha():
                    word+= letter
            if word in censorWords:
                words[i]= censor(words[i])
        censoredText += " ".join(words) + '\n'

        text.close()
        censored.close()
        
        newfile=open("censored:" + file, 'w')
        newfile.write(censoredText)
        newfile.close()
        

main()
