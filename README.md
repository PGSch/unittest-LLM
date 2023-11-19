# Automated EDA on financial dataset

Just a simple way to get automated Exploration Data Analysis from financial dataset (OHLCV) using [Streamlit](https://github.com/streamlit/streamlit) and [ta](https://github.com/bukosabino/ta).

To use this library you need a financial time series dataset including `Timestamp`, `Open`, `High`, `Low`, `Close` and `Volume` columns.


# Requirements

* python3.7 version


# Run

```sh
pip install streamlit==0.48.1 ta==0.4.5
streamlit run https://raw.githubusercontent.com/bukosabino/streamlit-demo-financial-eda/master/app.py
```


# TODO

* Heatmap: Visualize the correlation coefficient in between ta features.
* Web application user can load a .csv file


# Extra

Are you interested in more Streamlit demos related to financial data? 

* [Yahoo Finance data web app](https://github.com/paduel/streamlit_finance_chart)


# Contact

Developed by Darío López Padial (Bukosabino).

Please, let me know about any comment or feedback.


## Setup

```bash
mkdir -p /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/activate.d/
touch /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/activate.d/env_vars.sh
echo "export OPENAI_API_KEY=your-api-key-here" >> /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/activate.d/env_vars.sh


mkdir -p /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/deactivate.d/
touch /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/deactivate.d/env_vars.sh
echo "unset OPENAI_API_KEY" >> /Users/Patrick/anaconda3/envs/unittest-LLM/etc/conda/deactivate.d/env_vars.sh
```