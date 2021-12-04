# dva-team24
## 1. install flask
    pip3 install flask
    virtualenv flask
    cd flask
    source bin/activate

## 2. install twint
    git clone --depth=1 https://github.com/twintproject/twint.git
    cd twint
    pip3 install . -r requirements.txt
    pip3 install twint
    
Source: https://github.com/twintproject/twint/issues/1297

//put recommendation.py under the /twint

//create a file named "web" in the twint file

//put data, lib, icon and html files in the web directory

## 3. install eel
    pip install eel
    
Source: https://github.com/ChrisKnott/Eel

## 4. execute
    python recommendation.py
    
Error MSG: "[IMPORTERROR] cannot import name 'CeilTimeout' from 'aiohttp.helpers'"

Solution: pip install aiohttp==3.7.0 //in the flask

//run in the twint directory

## Directory Structure

flask/
twint/
    recommendation.py
    web/
        data/ --> Preprocessed_data.csv
        lib/
        icon/
        welcome.html
        visualization.html
        selection.html

