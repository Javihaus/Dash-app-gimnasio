# Developing and Deploying Dash via Heroku

Creating a Dash app to check a pandas dataframe including time series and other columns. Dash app allows to compare pair of columns and visualize each column's time series. 

1. Setup account on Heroku
2. Create a new app and deploy using GitHub. Connect to your Github repo where app files are. 
3. Commit this folder to Git
4. 'heroku git:remote -a [YOUR-APP-GIT-URL]' where YOUR-APP-GIT-URL refers to the Git link returned by 5.
5. 'git push heroku master' will deploy your app to Heroku
6. 'heroku ps:scale web=1' will create a Dyno and make your app live

If you want to make changes to your app repeat steps 2. 3. and 5.

Delete the runtime.txt if you wish to run on Python 2.7.x instead of 3.6.x

