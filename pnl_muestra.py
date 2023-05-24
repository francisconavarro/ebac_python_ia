"""
Script de ejercicio que muestra como definir variables, funciones y el uso de librerias
Python version: Python 3.8

"""
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords

def process_text(_str_text):
    """
    Funcion que  procesa una cadena con funciones de nltk

    Parameters
    ----------
    _str_text:
                       Cadena a procesar

    """
    # Tokenización de oraciones
    sentences = sent_tokenize(_str_text)
    print("Oraciones:", sentences)

    # Tokenización de palabras
    tokens = word_tokenize(_str_text)
    print("Tokens:", tokens)

    # Etiquetado gramatical
    tagged = pos_tag(tokens)
    print("Etiquetas gramaticales:", tagged)

    # Reconocimiento de entidades nombradas
    named_entities = ne_chunk(tagged)
    print("Entidades nombradas:", named_entities)

    # Eliminación de palabras vacías (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_words = [token for token in tokens if token.lower() not in stop_words]
    print("Palabras filtradas:", filtered_words)

# Texto de ejemplo
with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read().rstrip()

# Procesar el texto
process_text(data)
