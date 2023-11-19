# Unit test writing using a multi-step prompt

Complex tasks, such as writing unit tests, can benefit from multi-step prompts. In contrast to a single prompt, a multi-step prompt generates text from GPT and then feeds that output text back into subsequent prompts. This can help in cases where you want GPT to reason things out before answering, or brainstorm a plan before executing it.

In this notebook, we use a 3-step prompt to write unit tests in Python using the following steps:

1. **Explain**: Given a Python function, we ask GPT to explain what the function is doing and why.
2. **Plan**: We ask GPT to plan a set of unit tests for the function.
    - If the plan is too short, we ask GPT to elaborate with more ideas for unit tests.
3. **Execute**: Finally, we instruct GPT to write unit tests that cover the planned cases.

The code example illustrates a few embellishments on the chained, multi-step prompt:

- Conditional branching (e.g., asking for elaboration only if the first plan is too short)
- The choice of different models for different steps
- A check that re-runs the function if the output is unsatisfactory (e.g., if the output code cannot be parsed by Python's `ast` module)
- Streaming output so that you can start reading the output before it's fully generated (handy for long, multi-step outputs)


# Requirements

* python3.11 version


# Setup

```bash
conda create -n unittest-LLM python=3.11
```

```sh
pip install -r requirements.txt
```

Set openAI API key for environment

```bash
mkdir -p /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/activate.d/
touch /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/activate.d/env_vars.sh
echo "export OPENAI_API_KEY=your-api-key-here" >> /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/activate.d/env_vars.sh

mkdir -p /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/deactivate.d/
touch /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/deactivate.d/env_vars.sh
echo "unset OPENAI_API_KEY" >> /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/deactivate.d/env_vars.sh

conda activate unittest-LLM
```

# Run

Run in python:
```python
example_function = '''def pig_latin(text):
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
    '''

import unittestLLM as ut

unit_tests = ut.unit_tests_from_function(
            example_function,
            approx_min_cases_to_cover=10,
            print_text=True
        )

# Save the unittest to a .py file
with open("test_pig_latin.py", "w") as file:
    file.write(unit_tests)
```

Run in terminal:
```bsh
pytest test_pig_latin.py
```

```console
$ python test_pig_latin.py

.
.
.

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.'
expected = 'oremLay ipsumway olorday itsay ametway, onsecteturcay adipiscingway elitway. edSay onway isusray.'

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
>       assert pig_latin(text) == expected
E       AssertionError: assert 'oremlay ipsu...nnay isus.ray' == 'oremLay ipsu...nway isusray.'
E         - oremLay ipsumway olorday itsay ametway, onsecteturcay adipiscingway elitway. edSay onway isusray.
E         ?     ^                                 -                                    -   ^     ^          -
E         + oremlay ipsumway olorday itsay amet,way onsecteturcay adipiscingway elit.way edsay onnay isus.ray
E         ?     ^                              +                                    +      ^     ^       +

test_pig_latin.py:106: AssertionError
================================================================================== short test summary info ==================================================================================
FAILED test_pig_latin.py::test_pig_latin[Python-onPythay] - AssertionError: assert 'onpythay' == 'onPythay'
FAILED test_pig_latin.py::test_pig_latin[JuMP-uMPJay] - AssertionError: assert 'umpjay' == 'uMPJay'
FAILED test_pig_latin.py::test_pig_latin[hello!-ellohay!] - AssertionError: assert 'ello!hay' == 'ellohay!'
FAILED test_pig_latin.py::test_pig_latin[world,-orldway,] - AssertionError: assert 'orld,way' == 'orldway,'
FAILED test_pig_latin.py::test_pig_latin[Python is fun-onPythay isway unfay] - AssertionError: assert 'onpythay isway unfay' == 'onPythay isway unfay'
FAILED test_pig_latin.py::test_pig_latin[   Python is cool   -onPythay isway oolcay] - AssertionError: assert 'onpythay isway oolcay' == 'onPythay isway oolcay'
FAILED test_pig_latin.py::test_pig_latin[123-123] - AssertionError: assert '123ay' == '123'
FAILED test_pig_latin.py::test_pig_latin[@#$-@#$] - AssertionError: assert '@#$ay' == '@#$'
FAILED test_pig_latin.py::test_pig_latin[\xe9clair-\xe9clairway] - AssertionError: assert 'airéclay' == 'éclairway'
FAILED test_pig_latin.py::test_pig_latin[\xfcber-\xfcberway] - AssertionError: assert 'erübay' == 'überway'
FAILED test_pig_latin.py::test_pig_latin[ - ] - AssertionError: assert '' == ' '
FAILED test_pig_latin.py::test_pig_latin[rhythm-ythmrhay] - AssertionError: assert 'rhythmay' == 'ythmrhay'
FAILED test_pig_latin.py::test_pig_latin[brr-rrbay] - AssertionError: assert 'brray' == 'rrbay'
FAILED test_pig_latin.py::test_pig_latin[ababa-ababaay] - AssertionError: assert 'ababaway' == 'ababaay'
FAILED test_pig_latin.py::test_pig_latin[123abc-123abc] - AssertionError: assert 'abc123ay' == '123abc'
FAILED test_pig_latin.py::test_pig_latin[!@#$-!@#$] - AssertionError: assert '!@#$ay' == '!@#$'
FAILED test_pig_latin.py::test_pig_latin[This is a very long sentence with many words.-isThay isway away eryvay onglay entencesay ithway anymay ordsway.] - AssertionError: assert 'isthay isway...ymay ords.way' == 'isThay isway...ymay ordsway.'
FAILED test_pig_latin.py::test_pig_latin[Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.-oremLay ipsumway olorday itsay ametway, onsecteturcay adipiscingway elitway. edSay onway isusray.] - AssertionError: assert 'oremlay ipsu...nnay isus.ray' == 'oremLay ipsu...nway isusray.'
=============================================================================== 18 failed, 20 passed in 1.04s ===============================================================================
```

# TODO

* Cover more languages
* GUI
 
# Sources

* [openai-cookbook](https://github.com/openai/openai-cookbook)

# Contact

Please, let me know about any comment or feedback.
