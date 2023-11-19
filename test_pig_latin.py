import pytest


# function to test
def pig_latin(text):
    def translate(word):
        vowels = 'aeiou'
        if word[0] in vowels:
            return word + 'way'
        else:
            consonants = ''
            for letter in word:
                if letter not in vowels:
                    consonants += letter
                else:
                    break
            return word[len(consonants):] + consonants + 'ay'

    words = text.lower().split()
    translated_words = [translate(word) for word in words]
    return ' '.join(translated_words)


# unit tests
@pytest.mark.parametrize('text, expected', [
    # Words starting with a vowel
    ('apple', 'appleway'),
    ('elephant', 'elephantway'),
    
    # Words starting with a consonant
    ('banana', 'ananabay'),
    ('cherry', 'errychay'),
    
    # Words with multiple consonants at the beginning
    ('string', 'ingstray'),
    ('glove', 'oveglay'),
    
    # Words with uppercase letters
    ('Python', 'onPythay'),
    ('JuMP', 'uMPJay'),
    
    # Words with punctuation marks
    ('hello!', 'ellohay!'),
    ('world,', 'orldway,'),
    
    # Sentences or phrases with multiple words
    ('Hello world', 'ellohay orldway'),
    ('Python is fun', 'onPythay isway unfay'),
    
    # Empty input
    ('', ''),
    
    # Input with leading or trailing spaces
    ('  hello  ', 'ellohay'),
    ('   Python is cool   ', 'onPythay isway oolcay'),
    
    # Input with numbers or special characters
    ('123', '123'),
    ('@#$', '@#$'),
    
    # Input with non-English characters
    ('éclair', 'éclairway'),
    ('über', 'überway'),
    
    # Rare or unexpected edge cases
    # Empty word
    (' ', ' '),
    
    # Word with only consonants
    ('rhythm', 'ythmrhay'),
    ('brr', 'rrbay'),
    
    # Word with only vowels
    ('ai', 'aiway'),
    ('oo', 'ooway'),
    
    # Word with alternating consonants and vowels
    ('ababa', 'ababaay'),
    ('oxoxox', 'oxoxoxway'),
    
    # Word with repeated consonants
    ('letter', 'etterlay'),
    ('grass', 'assgray'),
    
    # Word with repeated vowels
    ('moon', 'oonmay'),
    ('see', 'eesay'),
    
    # Word with a single letter
    ('a', 'away'),
    ('i', 'iway'),
    
    # Word with non-alphabetic characters
    ('123abc', '123abc'),
    ('!@#$', '!@#$'),
    
    # Long words
    ('supercalifragilisticexpialidocious', 'upercalifragilisticexpialidocioussay'),
    ('antidisestablishmentarianism', 'antidisestablishmentarianismway'),
    
    # Very long input
    ('This is a very long sentence with many words.', 'isThay isway away eryvay onglay entencesay ithway anymay ordsway.'),
    ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.', 'oremLay ipsumway olorday itsay ametway, onsecteturcay adipiscingway elitway. edSay onway isusray.')
])
def test_pig_latin(text, expected):
    assert pig_latin(text) == expected