# Final Project


## Setup

Create virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate virtual environment (whenever you come back):

```sh
conda activate reports-env-2024
```

Install Packages:

```sh
pip install -r requirements.txt
```


## Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run
```

## Run Testing

```sh
pytest
```