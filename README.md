<h5>Starting point for Postgresql, Django, Vue, and Oauth app</h5>

<h6>Requirements:</h6>
<ul>
<li>Django Rest Framework<li>
<li>Postgresql</li>
<li>Needs a Google Oauth2 Client, information needs to be placed in myproject/settings.py: [Google Oauth2](https://developers.google.com/identity/protocols/oauth2) </li>
<li>Needs a Github Oauth app, information needs to be placed in myproject/views.py: [Github Oauth Apps](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)</li>
</<ul>>

<h6>Requirements for Django:</h6>
<ul>
<li>found in requirements.txt<li>
</ul>

<h6>Requirements for Vue:</h6>
<ul>
<li>npm install in /minimal-oauth</li>
<li>yarn serve in /minimal-oauth</li>
</ul>

<h6>What it does:</h6>
<ul>
<li>Allows user to register for the application using Allauth and a Google Oauth2 client</li>
<li>After logging in a user can authorize a connection to their github account. This flow is handled by django views.</li>
<li>If github is authorized the user's github account name and access token are stored in an entry in the database using the Django Rest Framework /api/notes</li>
<li>The token from the database is used by the Vue app and gives a function to get their public repos using the Github API</li>
<li>The repos are returned and the user can then click on a repo to store it's information in their database entry. They can keep overwriting this selected repo if they want</li>
</ul>

<h6>Issues: </h6>
<ul>
<li>The user records created by the DRF (api/notes) is not directly linked with the entries created by Allauth, it is a new entry. Features still work with a single sign on, but a bit of duplication. Allauth is a heavy solution though it handles the Oauth2 registration and provides good security</li>
<li>The tokens are stored in plain text, could have improved security</li>
<li>Overall there is still room for refactoring and improving naming throughout</li>
</<ul>>