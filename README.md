##### Starting point for Postgresql, Django, Vue, and Oauth app

<h6>Requirements:</h6>

- Django Rest Framework
- Postgresql
- Needs a Google Oauth2 Client, information needs to be placed in myproject/settings.py: [Google Oauth2](https://developers.google.com/identity/protocols/oauth2)
- Needs a Github Oauth app, information needs to be placed in myproject/views.py: [Github Oauth Apps](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)


###### Requirements for Django:

- found in requirements.txt


###### Requirements for Vue:

- npm install in /minimal-oauth
- yarn serve in /minimal-oauth


###### What it does:

- Allows user to register for the application using Allauth and a Google Oauth2 client
- After logging in a user can authorize a connection to their github account. This flow is handled by django views.
- If github is authorized the user's github account name and access token are stored in an entry in the database using the Django Rest Framework /api/notes
- The token from the database is used by the Vue app and gives a function to get their public repos using the Github API
- The repos are returned and the user can then click on a repo to store it's information in their database entry. They can keep overwriting this selected repo if they want


###### Issues: 

- The user records created by the DRF (api/notes) is not directly linked with the entries created by Allauth, it is a new entry. Features still work with a single sign on, but a bit of duplication. Allauth is a heavy solution though it handles the Oauth2 registration and provides good security
- The tokens are stored in plain text, could have improved security
- Overall there is still room for refactoring and improving naming throughout
