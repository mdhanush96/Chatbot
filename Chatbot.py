import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

def stem_text(text):
    stemmer = PorterStemmer()
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)

def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

exit_words = ["exit", "quit", "stop"]
x = input("Enter text: ")
while x not in exit_words:
    choice = input("Give 1, 2, 3, or 4 option: \n1. Lowercase \n2. Uppercase \n3. Remove Stopwords \n4. Stemming\n")

    if choice == "1":
        print(lowercase(x))
    elif choice == "2":
        print(uppercase(x))
    elif choice == "3":
        print(remove_stopwords(x))
    elif choice == "4":
        print(stem_text(x))
    else:
        print("Invalid choice")

    x = input("Enter text: ")