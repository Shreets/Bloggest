# Bloggest
Implementation of initially pushed Blogger app in class based views in Django with additional features

## Added features

-Implementation of class based views
-pagination added in class based views
-use of caching
-email confirmation for verifying account
-user profile can be created if it doesnt already exists and can be updated

## To Enable Mailing feature

[mailtrap](http://mailtrap.io/) is being used to add mailing feature on signup. Add your *mailtrap* credentials in setting.py file 
and uncomment send_mail() funtions in signup view from portfolio/view.py to test mailing feature in development environment.
