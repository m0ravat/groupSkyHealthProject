# Django Architecture 

The Django web framework is a full stack framework - It covers development on both the backend and frontend. It follows the MVT Architecture which bears similarities to Express.js, with the components split as follows: 

- Model - This is used to represent our data from the database. It's structured similar to classes in OOP, we define a structure and use it to create an instance to pass data into other areas. An example of this would be creating a User model with a defined structure like (UserID: Int, firstName: String, lastName: String). When logging in if we get a user from the db we can create an instance and pass the attributes from the database. This increases data integrity as if the db structure is flimsy it won't pass through the model (ie using string IDs wouldn't be valid if we define ID as an int). 

- View - This handles the logic side of our program, when we create an instance of a model we typically pass it to our view folder. This can handle logic like for login dehashing db results or handle API Logic which is covered [here](extra.md). 

- Template - This would be our HTML files rendered that in a framework environment have some sort of logic implemented as well so we dont need to use the <script> </script> tag. The common uses would be if we pass a user model to the template like render(https://localhost/quiz, user: user1) we could use:       
{% if(user1.role != "Engineer" || user1.role != "TeamLeader"):     
<p> You cannot access this page, too high access level </p> %}      
What this snippet does is conditionally check if a user has access based off their role, if they did we would use an else and render the rest.   

## How it links together 

Our model allows us to pass database values into models that can be modified or otherwise in our view folder, then sent to a template which is what the user sees. To put it simply : Model = Data, View = Backend logic, Template = Frontend logic. 