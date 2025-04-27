# Folder structure

The folder structure of the project is as follows: 

skyHealthproject (Project root)          
     
Inside the skyHealthProject we have the following folders:      
core - Used for home/login/signup pages (Iqra)      
quiz - used for quiz page (Barket)       
skyHealthProject - default app created when we create the project, has settings for the website.      
static - all css/js and images are here       
stats - stats app (Muhammad)      
templates - has html code that is used in multiple pages - navigation bars.       
user - Handles user dashboard and profile pages.        
       
The above are all apps, which have files inside called:       
templates - the html for your specific pages.      
models.py - may have db table structures relevant to your app     
views.py - the logic that happens before loading a page or when you submit a form.       
      
## Where is my CSS?      
It's in the static folder inside skyHealthProject, seperated into the app folders so it's all modular!    
For information on how to import css in these files to your html refer to my stats pages as a template.       

## How do I start???
Your URLS have been set up, go inside the skyHealthProject app and inside urls.py, from there it will likely import a views file inside your relevant app folder. That is where you handle logic going into loading the page. The stats app and core app have examples of how it can be used, so refer to these on what does what.
