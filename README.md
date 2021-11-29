# dva-team24
## 1. install flask
    ```
    pip3 install flask
    virtualenv flask
    cd flask
    source bin/activate
    ```

## 2. install twint
    https://github.com/twintproject/twint/issues/1297
    ```
    git clone --depth=1 https://github.com/twintproject/twint.git
    cd twint
    pip3 install . -r requirements.txt
    pip3 install twint
    ```

//create a file named "web" in the twint file

## 3. install eel
    https://github.com/ChrisKnott/Eel
    ```
    pip install eel
    ```


## 4. execute
    ```
    python recommendation.py
    ```
    error: "[IMPORTERROR] cannot import name 'CeilTimeout' from 'aiohttp.helpers'"
    solution: pip install aiohttp==3.7.0

## Directory Structure
```
flask/
twint/
    recommendation.py
    web/
        data/
        lib/
        welcome.html
        visualization.html
        selection.html
```
