# Installation Requirements 

Download python 3.12.8 if you don't have it  per the project requirements [here](https://www.python.org/downloads/release/python-3128/)    
Install git if you havent already too    
Clone the repository by isnatlling GitHub Desktop (Easy way) or by cloning it, to do so run the following commands on a VS Code terminal :     
`git clone https://github.com/m0ravat/groupSkyHealthProject.git` and            `cd repo` to go into the repository folder.    

If not using Github desktop ensure to always pull requests using VS Code version control to pull changes from teammates, and to push your requests when you make them, the more meaningful the commit messages the easier it is to figure out what has been changed and the more marks we get. 

# Setting up django Virtual environment 

In the repository whenever you start create a virutal environment (this is so external libraries are only installed on the project and not the system)    
`python -m venv venv` then `venv\Scripts\activate`    
To install dependencies other people may have added run:    
`pip install -r requirements.txt`       


If you install a library or dependency using pip ensure to save it to requirements.txt so we can all install it too:    
`pip freeze > requirements.txt`






