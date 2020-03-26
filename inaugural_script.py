from __future__ import division
import nltk
import matplotlib.pyplot as plt
from textblob import TextBlob
from nltk.corpus import inaugural

republican = ['1869-Grant.txt', '1873-Grant.txt', '1877-Hayes.txt', '1881-Garfield.txt', '1889-Harrison.txt', '1897-McKinley.txt', '1901-McKinley.txt', '1905-Roosevelt.txt', '1909-Taft.txt', '1921-Harding.txt', '1925-Coolidge.txt', '1929-Hoover.txt', '1933-Roosevelt.txt', '1937-Roosevelt.txt', '1953-Eisenhower.txt', '1957-Eisenhower.txt', '1969-Nixon.txt', '1973-Nixon.txt',  '1981-Reagan.txt', '1985-Reagan.txt', '1989-Bush.txt', '2001-Bush.txt', '2005-Bush.txt', '2017-Trump.txt']
democratic = ['1885-Cleveland.txt', '1893-Cleveland.txt', '1913-Wilson.txt', '1917-Wilson.txt', '1937-Roosevelt.txt', '1941-Roosevelt.txt', '1945-Roosevelt.txt', '1949-Truman.txt', '1961-Kennedy.txt', '1965-Johnson.txt', '1977-Carter.txt', '1993-Clinton.txt', '1997-Clinton.txt', '2009-Obama.txt', '2013-Obama.txt']

politics = ["justice", "constitution", "democracy", "president", "communism", "republic", "congress"]
finance = ["tax", "money", "commerce", "economy"]
emotions = ["love", "happiness", "dignity", "courage", "sacrifice", "compassion", "loyalty", "patriotism", "morality", "generosity"]
spirit = ["bible", "god", "spirit", "soul", "destiny", "prayer", "faith", "truth", "wisdom", "conscience"]

################################################################## Liczenie słów

def CountWords(words):
    x = []
    y = []
    for fileid in inaugural.fileids():
        count = 0
        for w in inaugural.words(fileid):
            if w.lower() in words:
                count += 1
        per = (count/len(inaugural.words(fileid)))*100
        y.append(fileid[:4])
        x.append(per)

    plt.title('Liczba wystąpień:')
    plt.xticks(rotation=90)
    plt.plot(y, x)
    plt.show()

############################################################ Average word length

def avgWord():
    x1 = []
    y1 = []
    for fileid in inaugural.fileids():
        words = inaugural.raw(fileids=fileid)
        words = words.split()
        average = sum(len(word) for word in words) / len(words)
        print(fileid[:4], "-", average)
        y1.append(fileid[:4])
        x1.append(average)

    plt.title('Średnia długość słowa:')
    plt.xticks(rotation=90)
    plt.plot(y1, x1)
    plt.show()

############################################################ Average sent length

def avgSent():
    x2 = []
    y2 = []

    for fileid in inaugural.fileids():
        average = sum(len(sent) for sent in inaugural.sents(fileids=[fileid])) / len(inaugural.sents(fileids=[fileid]))
        print(fileid[:4], "-", average)
        y2.append(fileid[:4])
        x2.append(average)

    plt.title('Średnia długość zdania:')
    plt.xticks(rotation=90)
    plt.plot(y2, x2)
    plt.show()

###################################################################### Sentiment

def senti():
    x3 = []
    y3 = []
    x31 = []

    for fileid in inaugural.fileids():
        text = inaugural.raw(fileids=fileid)
        senti = TextBlob(text)
        print(fileid[:4], "-", senti.sentiment)
        y3.append(fileid[:4])
        x3.append(senti.sentiment[0])
        x31.append(senti.sentiment[1])
    plt.title('Polarity')
    plt.xticks(rotation=90)
    plt.plot(y3, x3)
    plt.show()
    plt.title('Subjectivity')
    plt.xticks(rotation=90)
    plt.plot(y3, x31)
    plt.show()

################################################################## Lex diversity

def lexDiv():
    y4 = []
    x4 = []

    for fileid in inaugural.fileids():
        div = len(set(fileid)) / len(fileid)
        print(fileid[:4], "-", div)
        y4.append(fileid[:4])
        x4.append(div)

    plt.title('Różnorodność słownictwa')
    plt.xticks(rotation=90)
    plt.plot(y4, x4)
    plt.show()

################################################## Porownanie wystepowania slow

def compare(word, word2):
    cfd = nltk.ConditionalFreqDist(
              (target, fileid[:4])
              for fileid in inaugural.fileids()
              for w in inaugural.words(fileid)
              for target in [word, word2]
              if w.lower().startswith(target))
    cfd.plot()

def main():
    while True:
        print("1. Występowanie danego słowa/słów \n2. Średnia długość słów \n3. Średnia długość zdania \n4. Analiza sentymentu \n5. Różnorodność słownictwa \n6. Porównanie występowania słów \n\n0. Zamknij program")
        choice = int(input("Wybierz liczbę: "))

        if choice == 1:
            word = input("Wybierz jedną z grup słów (politics, finance, emotion, spirit) \nlub podaj inne słowo: ")
            if word == politics:
                CountWords(politics)
            elif word == finance:
                CountWords(finance)
            elif word == emotions:
                CountWords(emotion)
            elif word == spirit:
                CountWords(spirit)
            else:
                CountWords(word)
        elif choice == 2:
            avgWord()
        elif choice == 3:
            avgSent()
        elif choice == 4:
            senti()
        elif choice == 5:
            lexDiv()
        elif choice == 6:
            word = input("Podaj pierwsze słowo: ")
            word2 = input("Podaj drugie słowo: ")
            compare(word, word2)
        elif choice == 0:
            break
        else:
            print("Niepoprawne polecenie")

main()
