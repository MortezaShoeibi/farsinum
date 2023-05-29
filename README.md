# Farsi num

A Django REST framework based API to convert Latin numbers to Persian(Farsi) text.

# Usage

This API supports both GET and POST HTTP methods:

to use the API with GET method pass the parameter `number` like the following:

```bash
GET: farsinum.ir/api/converter?number=1234
```

for a POST request do this and pass the `number` parameter in the body form-data:

```bash
POST: farsinum.ir/api/converter
```

# Setup and run
To run `farsi num` in development mode:

- Install `git` and `python3`

- Clone and cd to the project:
```bash
git clone https://github.com/MortezaShoeibi/farsinum.git && cd farsinum/
```
- Create and activate a virtual environment: 
```bash
python3 -m venv env
# then:
source env/bin/activate
```
- On windows:
```powershell
python -m venv env
# then:
./env/Scripts/activate
```
- Install required packages:
```bash
pip3 install -r requirements.txt
```
- run:
```bash
python3 ./manage.py runserver
```
Your version of farsinum will be running on this address: `127.0.0.1:8000` add it to your browser search path and you will be able to see your own farsinum running locally.
