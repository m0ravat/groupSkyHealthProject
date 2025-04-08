# How to set up your environment

You start by pulling all changes from teammates using Github Desktop or the VS Code version control on the left. Then you start a virtual environment by running:         
`cd .\groupSkyHealthProject\` if you arent already in the project folder, then you start a virtual environment by running     
`python -m venv venv` then `venv\Scripts\activate`          
To install dependencies other people may have added run:           
`pip install -r requirements.txt`           

If you install a library or dependency using pip ensure to save it to requirements.txt so we can all install it too:       
`pip freeze > requirements.txt`     

# How to run project

Ensure you are in the first skyHealthProject folder by running `cd skyHealthProject` assuming you are in the groupSkyHealthProject folder already.       
Run ` python manage.py runserver` which will start it up.
