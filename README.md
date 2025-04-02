# Installation Requirements 

Download python 3.12.8 if you don't have it  per the project requirements [here](https://www.python.org/downloads/release/python-3128/)    
Install git if you havent already too    
Clone the repository by isnatlling GitHub Desktop (Easy way) or by cloning it, for the latter create a project folder, load it on VS Code and run the following commands on a VS Code terminal :     
`git clone https://github.com/m0ravat/groupSkyHealthProject.git` and            `cd repo` to go into the repository folder.    


# How to run the project

You start by pulling all changes from teammates using Github Desktop or the VS Code version control on the left. Then you start a virtual environment by running:     
`cd .\groupSkyHealthProject\` if you arent already in the project folder, then you start a virtual environment by running     
`python -m venv venv` then `venv\Scripts\activate`     
To install dependencies other people may have added run:    
`pip install -r requirements.txt`       


If you install a library or dependency using pip ensure to save it to requirements.txt so we can all install it too:    
`pip freeze > requirements.txt`     
The .gitignore is set to ignore the venv since different machines may have slightly different code so you have to create a new virtual environment everytime you run the project and install the requirements in the case someone adding something new. 







