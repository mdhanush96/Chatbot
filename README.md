# Chatbot
# Text Processing Utility

## Overview
This Python script provides basic text processing functionalities, including:
- Converting text to lowercase
- Converting text to uppercase
- Removing stopwords using NLTK
- Stemming words using the PorterStemmer algorithm

## Requirements
Ensure you have Python installed along with the required NLTK library. You can install NLTK using:
```bash
pip install nltk
```
Additionally, download the stopwords dataset for NLTK:
```python
import nltk
nltk.download('stopwords')
```

## How to Use
Run the script and enter any text when prompted. You will then be given the following options:
1. Convert text to lowercase
2. Convert text to uppercase
3. Remove stopwords
4. Perform stemming

To exit, type "exit", "quit", or "stop".

### Example Usage
```bash
Enter text: This is an example sentence
Give 1, 2, 3, or 4 option:
1. Lowercase
2. Uppercase
3. Remove Stopwords
4. Stemming
```
If you choose option 3 (Remove Stopwords), the output will be:
```bash
example sentence
```

## Potential Issues
- Ensure you have installed and downloaded NLTK stopwords before running the script.
- The script may not work correctly if the input contains special characters or non-English words.

## License
This project is open-source and available under the MIT License.

