1. DESCRIPTION
    <Directory Structure>
    flask/
    twint/
        recommendation.py
        web/
            data/ --> "Preprocessed_data.csv" downloaded from Kaggle
            lib/
            icon/
            welcome.html
            visualization.html
            selection.html
    
2. INSTALLATION
    (1) <Download Dataset>
        https://www.kaggle.com/ruchi798/bookcrossing-dataset

    (2) <Install Flask>
        pip3 install flask
        virtualenv flask
        cd flask
        source bin/activate

    (3) <Install Twint>
        git clone --depth=1 https://github.com/twintproject/twint.git
        cd twint
        pip3 install . -r requirements.txt
        pip3 install twint

    (4) <install eel>
        pip install eel
    
3. EXECUTION
    Run "python recommendation.py" //under the twint directory
    ***
    error msg: "[IMPORTERROR] cannot import name 'CeilTimeout' from 'aiohttp.helpers'"
    solution: pip install aiohttp==3.7.0
    ***

4. DEMO VIDEO