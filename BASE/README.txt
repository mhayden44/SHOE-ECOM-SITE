**FOR WINDOWS**
(Check runtime.txt for the version of python used but as long as it is python 3, preferablly 3.6+, it should run fine)
Open command prompt
cd \
cd to SHOE ECOM SITE/BASE (it may be different depending on how the project was downloaded, just right click on the top BASE directory and select copy path and cd to that)
python -m venv myvenv
myvenv\scripts\activate
pip install -r requirements.txt
create a .env file within SHOE ECOM SITE/BASE
Run the file BASE\secretKey.py
Copy the output and paste into .env
save all
python manage.py runserver
go to http://127.0.0.1:8000/home/
Navigate around the different pages


**NOTE ON FUNCTIONALITY**
Website features a navbar that allows the user to navigate around to the different pages.

Along the navbar are the buttons for the home page, men's page (with dropdown for specific men's shoe types), women's page (with dropdown for specific women's shoe types),
a search bar that allows the user to search for shoes by name or brand, a welcome "username" box, cart page, and login/logout page.

The shoes for men's and women's are split up into there own pages and then they are furthur split up based on type (all types, athletic, work, dress, and casual).

Each shoe lists the brand, name, short description, and price of the shoe. Each shoe also has an add to cart button that adds that shoe to the user's cart if they are signed in.

If the user is not signed in, they will be redirected to login (from which they can choose to create an account if they do not already have one).

Once the user has all the shoes in their cart that they want, they can click the cart button in the top right of the navbar to view their cart.

From the cart page, the user can view all the shoes they have in their cart including a photo, price, quantity, and total price for each shoe. 

The total price of all the shoes in the cart is summed up and displayed at the top of the screen along with the total number of shoes the user has in their cart.

The user can also choose to change the quantity of each shoe they have in their cart, ranging from 0 (removes the shoe from the cart) up to 99.

There is also a button to clear the cart which will remove all the shoes from the user's cart.

A continue shopping button is located in the top left and will take the user back to the base shoe page.

Checkout functionality is not implemented since it was never intended to be implemented from the get go as I did not ant users actually inputting any payment information.

The site is also able to handle different monitor resolutions and zooming in and out just fine as it auto adjusts the things on the pages to compensate.


**ERRORS**
There are no issues displayed when starting the server as well as none when accessing the different pages.

I put the site through vigerous testing, trying out all sorts of different combinations of pages and functions to try and break it but none returned any problems.


**SECURITY**
The proper security settings should be in place, "@login_required" and "if request.user.is_authenticated" are placed throughout the code where needed.

The Django SECRET_KEY is also hidden and must be regenerated whenever downloaded from Github as described in the instruction methods above.

In reality, the static folder and db.sqlite3 would be hidden in the .env file since they would be handled by the production web server. 
Since this is not the case and it is instead run locally, this is not necessary.

In reality, in settings, DEBUG would be set to "False" but since this is run locally, it does not matter and it would instead cause the static files to not be registered properly.