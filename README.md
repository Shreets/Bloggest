# Bloggest
Implementation of initially pushed Blogger app in class based views in Django with additional features

## Added features

1. Implementation of class based views
2. pagination added in class based views
3. use of caching
4. email confirmation for verifying account
5. user profile can be created if it doesnt already exists and can be updated

## To Enable Mailing feature

[mailtrap](http://mailtrap.io/) is being used to add mailing feature on signup. Add your *mailtrap* credentials in setting.py file 
and uncomment send_mail() funtions in signup view from portfolio/view.py to test mailing feature in development environment.
