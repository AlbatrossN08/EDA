# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *eda*
```
conda create -n eda python=3.8
```
Secondly, we will login to the *eda* environment
```
conda activate eda
```
### Install prerequisite libraries
Pip install libraries
```
pip install -r requirements.txt
```
###  Launch the app

```
streamlit run app.py
```
