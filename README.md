<h1>Secret Santa Generator - Django Edition!</h1>

A rework of the Secret Santa Generator idea I had and implemented previously. I have been debating learning 
how to use Django for a while now, so this was an opportunity to step outside my comfort zone! 

<h2>Technologies used</h2>
  <li>Python 3</li>
  <li>Django</li> 
  <li>PostgreSQL</li>
  <li>VirtualEnv</li>

<h2>Run Book</h2>

First, clone this project onto your local machine. You should be running Python 3 and have `pip` installed. This project
has been built to run in a virtual environment. If you don't have it installed, you'll need to install virtualenv. <br><br>

`pip install virtualenv` <br><br>

Next, you'll navigate to the root of the project if you haven't already and spin up the virtual environment. <br><br>

`python3 -m venv secret_santa_env` <br>

`source secret_santa_env/bin/activate` <br><br>

This project loads sensitive information from a YAML file stored in the root of the project. This configuration can be found in 
`secret_santa_generator/settings.py` on line 16. You'll need to create `config.yml` at the root level. The contents of this file
are: <br><br>

```database: <your database name>
user: <user>
password: <password>
host: <database host>
port: <database port>
engine: <database engine>
secret: <secret key> 
``` 

<br>You should notice `(secret_santa_env)` prefixed on your command line at this point. This indicates that the environment is running. 
Finally, you'll need to install the modules within this local environment. You can do this with this command: <br><br>

`pip install -r requirements.txt` <br><br>
