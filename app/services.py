from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# punkt_tab indirme
nltk.download('punkt_tab')

# Request sayısını takip etmek için basit değişken
request_count = 0

def analyze_text(text: str):
    global request_count
    request_count += 1

    # punkt_tab kullanılıyor
    sentences = sent_tokenize(text)  
    words = word_tokenize(text.lower())

    word_count = len(words)
    sentence_count = len(sentences)
    most_common = dict(Counter(words).most_common(5))
    summary = sentences[0] if sentences else ""

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "most_common_words": most_common,
        "summary": summary
    }

def get_request_count():
    return request_count
