##Test Manual
###Pre-requisits:
1. Python (preferably 2.7.6)
2. Flask

###Steps to setup:
1. Install Python
2. Install Flask
3. Install suffixml

###Installing Python:
To install Python on different OS, follow [official python documentation](https://docs.python.org/2/using/index.html)

###Installing Flask:
Flask is a simple web server written in Python. We're going to use it for showing the hosting capability of the code on localhost. You can host the same on some other server of your choice.To install it, you need to install two tools: pip and virtualenv.
pip comes installed with virtualenv.

###Installing virtualenv with Python:
`$ easy_install-2.7 virtualenv`
Note: If you get error, try running it with sudo (admin user).

Once you have virtualenv installed, switch to the directory you'll use for your test, and create a virtual environment:

`$ cd /home/suffix`
`$ virtualenv --no-site-packages .`

Now activate the virtual environment.

`$ source bin/activate`

Now we're going to install Flask. We will make use of requirements.txt in the suffix folder which came along with the zipped content.
Install this packages with pip, in your terminal:

`$ bin/pip install -r requirements.txt`

