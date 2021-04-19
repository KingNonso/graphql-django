# Graphql with Django
As the web evolves, the responses from the servers are becoming less and less chatty. They transformed from gigantic SOAP responses to simple JSON responses. That doesn’t stop us from inventing new methods to simplifying it further. GraphQL gives more flexibility to front end developers where they can request only the details they need. This avoids the need for parsing unnecessary data on frontend.
## Setting up your local environment
* Endeavor to copy .env.example to your site root and rename as .env (should be at the same level with manage.py)
* Make sure you have git, pip and virtualenv and postgreSQL installed
* Clone the git repo by running `git clone git@github.com:peddlesoft/web-app.git`
* run `virtualenv env` to create a new virtual environment
* activate env by running `source env/bin/activate` or  `env/scripts/activate` for windows
* run `pip install -r requirements.txt` to install all required app extensions
* create NEW postgres database named 'peddlesoft'
* add the new database name to your `.env` file

### In Postgres
```
-sudo -u postgres psql # ubuntu command to access the postgres terminal
-CREATE DATABASE peddlesoft;
-CREATE USER myprojectuser WITH PASSWORD 'password';
-ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
-ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
-ALTER ROLE myprojectuser SET timezone TO 'Africa/Lagos';
-CREATE EXTENSION pg_trgm; # for full text search - evaluate the similarity of two strings by the number of “trigrams” they share.
-CREATE EXTENSION unaccent; # search without worrying about accented characters, useful in different languages
-GRANT ALL PRIVILEGES ON DATABASE peddlesoft TO myprojectuser;
```
Then exit postgres

### In your IDE
```python
-python manage.py makemigrations
-python manage.py migrate
-python manage.py createsuperuser # create a user with d details
-python manage.py collectstatic
-python manage.py runserver
```
Boom ......... and you are up and running

### Setting up .env
All the secret keys and site config are kept in an .env file. 
To set up the platform properly, you will need to create one from .env.example, copy the following inside, then add to gitignore and never commit it. 
It must live and die in your local.


## Bash Aliases
List of all my aliases when working with Python/Django Projects... Smh..don't like typing long things. Save it in your .bash_aliases and include in .bashrc.
```python
alias pym="python3 manage.py"
alias djm="django-admin"
alias pym:mm='python3 manage.py makemigrations'
alias pym:m='python3 manage.py migrate'
alias pym:r='python3 manage.py runserver'
alias pym:app='python3 manage.py startapp'
alias s:env='source env/bin/activate'
alias ga*='git add *'
alias gcm='git commit -m'

```
Please note that these aliases will form the convention used (King)

## Working with Views (views.py)
Always reference (https://ccbv.co.uk/)[https://ccbv.co.uk/]

## Templates
* Javascript inclusion: There are two js blocks. One Js block for script file inclusion and another domready block, for quick execution without worrying about CSRF
* When working on the frontend, you can view and use any of the available resources that came with the theme here:

## Pull Requests
Feel free to open pull requests before you've finished your code or tests. Opening your pull request soon will allow others to comment on it sooner.
A checklist of things to remember when making a feature:
* Write tests if applicable
* Note important changes in the commit
* Update the README file if needed
* Update the documentation if needed

# SOLID
Try to be as SOLID as possible. Because until we have a solid test framework, these principles will keep us working sanely together so you don't break things when you change them
Models are closed for modification and only open for extension So also are views
 
SOLID is an acronym for 5 important design principles when doing OOP (Object Oriented Programming).
The intention of these principles is to make software designs more understandable, easier to maintain and easier to extend.
## S — Single responsibility principle
In programming, the Single Responsibility Principle states that every module or class should have responsibility over a single part of the functionality provided by the software.
##  O — Open/closed principle
In programming, the open/closed principle states that software entities (classes, modules, functions, etc.) should be open for extensions, but closed for modification.
## L — Liskov substitution principle
More generally it states that objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. This one is probably the hardest one to wrap your head around when being introduced for the first time. Don't worry, if you don't get it. Neither do I. ;)
## I — Interface segregation principle
In programming, the interface segregation principle states that no client should be forced to depend on methods it does not use. Put more simply: Do not add additional functionality to an existing interface by adding new methods. Ummmm... don't get it yet.. OK. Just remember Rule 2. Open/closed - they are related kinda
## D - Dependency inversion principle
In programming, the dependency inversion principle is a way to decouple software modules. This principle states that
- High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.# graphql-django
