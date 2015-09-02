SET UP

1 You need to install vagrant, virtualBox and git. you can download both of them from here:https://www.udacity.com/wiki/ud197/install-vagrant
(Strongly recommand to install virtual box 4.3.xx because other version may not be compatible with vagrant and cause 
varies kind of problems)

2 Clone the fullstack-nanodegree-vm repository, just type the following in the Git Bash program: git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack Then in the file github, you can find that a file called fullstack is cloned for you.

3 Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine

4 Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt.
To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.




RUNNING APP

1 After you download the app package, database_setup.py, sports_and_equipments.py and applcation.py will be used while
  running the app.

2 Make sure you are in the catalog index and you could check whether these files I mentioned below by type ls in the command line.

3 Type 'python database_setup.py' in the command line which will help you establish the database we will use in this app.
  One important thing is when you want to initialize your database, you have to delete it first and run this command again.
  
4 After creating the database, next step is to add some instances into it. Type 'python sports_and_equipments.py' in the command line
  and adding is successful when some items are showed in the command line.
  
5 Next type 'python application.py' in the command line which it makes you have a server to deal with different kind of clients requests.

6 Open 'localhost:8000' on your laptop and you could see the homepage. In this page, some sports and equipments related to it 
  are shown on the left side and right side seperately. If you want to add some new items you could log in through the topright
  button. Noticed that if you don't have google account, it is neccessary to sign up a google acount before sign in this app.
  You could create your google acount here: https://accounts.google.com/signUp?service=mail
  
7 Except add, edit and delete operation, you could also fetch json file by typing related url listed in the application.py

