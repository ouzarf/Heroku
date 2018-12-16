heroku-php-sample
=================

Sample Heroku PHP project that demonstrates elastic.io add-on. 

See this sample already running here 

https://elasticio-php-demo.herokuapp.com

How to start this demo
=================

Deploying this demo on your Heroku app is very simple. First clone this project

```
git clone https://github.com/elasticio/heroku-php-sample.git
```

Please note that you will get a read-only clone of this repository, if you want write permissions just fork the repository.

Now create a new heroku app:

```
cd heroku-php-sample
heroku create
```


New Heroku app will be created, now add the elastic.io add-on to your new heroku app (don't worry if you can import up to 20K contacts per month for free)

```
heroku addons:add elasticio
```

Now push the content of the repository to your new heroku app:

```
git push heroku master
```

And then open the app in browser:
```
heroku open
```

That's it.

