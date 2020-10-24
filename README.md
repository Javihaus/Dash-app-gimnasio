# Developing and Deploying Dash via Heroku

Creating a Dash app to check a pandas dataframe including time series and other columns. Dash app allows to compare pair of columns and visualize each column's time series. 

1. Setup account on Heroku
2. Create a new app and deploy using GitHub. Connect to your Github repo where app files are. 
3. As alternative, create app with [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#getting-started)
4. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
5. Change to directory where your app files are:  
'''
    $ cd ~/myapp
    '''
6. Login in Heroku:

    $ heroku login   
7. Create an app: 
'''
    $ heroku create
    '''
8. Initialize a git repository in a new or existing directory with:
    '''
    $ git init 
    $ heroku git:remote -a <app-name>
    '''
9. Deploy application:
   ``` 
   $ git add 
   
   $ git commit -am "make it better"
   
   $ git push heroku master
    ```

Delete the runtime.txt if you wish to run on Python 2.7.x instead of 3.6.x

