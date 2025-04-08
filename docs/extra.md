# The .gitignore file

The .gitignore file is designed to ignore files for security reasons or otherwise, so while you see it on VS Code it isn't visible on the GitHub repo site. I ignored the venv folder which is created when starting a virtual environment since some files may be exclusive to certain local machines/operating systems.        
        
I also set it to ignore the .env file for security reasons but commented it out. This is because in the context of this project being a coursework, it makes sense to allow lecturers to see everything, so even if the .env file is visible by undoing the commenting you can easily see how the IDE puts the file in gray to indicate the gitignore took effect.        
      
# The .env file     
          
This file is stored in the skyHealthProject directory and is used to store environment variables. This is typically hidden but for educational reasons I kept it. It contains a Django secret key which is created when the project is first created. I ensured to put the key in the .env file before commiting it to github so it wouldn't be visible under normal circumstances. 