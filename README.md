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

# TODO

* Cover more languages
* GUI
 
# Sources

* [openai-cookbook](https://github.com/openai/openai-cookbook)

# Contact

Please, let me know about any comment or feedback.
