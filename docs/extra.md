# Virtual Environment 

The reason why we use a virtual environment is so every person doesn't have to manually download every extension on their machine. This is done so if that extension is updated down the line it won't make a difference since we have defined our versions in the Requirements.txt file.

# The .gitignore file

The .gitignore file is designed to ignore files for security reasons or otherwise, so while you see it on VS Code it isn't visible on the GitHub repo site. I ignored the venv folder which is created when starting a virtual environment since some files may be exclusive to certain local machines/operating systems.        
        
I also set it to ignore the .env file for security reasons but commented it out. This is because in the context of this project being a coursework, it makes sense to allow lecturers to see everything, so even if the .env file is visible by undoing the commenting you can easily see how the IDE puts the file in gray to indicate the gitignore took effect.        
      
# The .env file     
          
This file is stored in the skyHealthProject directory and is used to store environment variables. This is typically hidden but for educational reasons I kept it. It contains a Django secret key which is created when the project is first created. I ensured to put the key in the .env file before commiting it to github so it wouldn't be visible under normal circumstances. 

# API Logic 

Typically when creating backend logic API's are used. They are prompted by a URL endpoint and can be used for multiple reasons. The main URL endpoints are : 

- Get requests: Typically when we search a url like https://localhost/quiz this would send a get request to our server which would run a function that renders the template for it. This way we can run verification or get data before loading the websites frontend. 
- Post requests: When a user submits a form a post request is sent to a url, this is typically used to indicate we want to insert data into a database. 
- Delete requests: Indicates we would want to delete something, like deleting a user profile. 
- Put requests: Indicating we may want to update a database record like updating personal info.        

## Why use this? 

We use different endpoints because the same url may handle multiple requests. To load the login page we would handle that logic by defining it as a get request, but when we submit the login form we would send a post request to the same URL. This way GET(https://localhost/login) and POST(https://localhost/login) are carried out on the same website but handle different aspects, we may emulate this on the user profile page with a GET(localhost/user) to load the profile page, a DELETE(localhost/user) to send a request to delete the user account and have a PUT(localhost/user) to indicate we want to update user info. 
