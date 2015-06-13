[![Requirements Status](https://requires.io/github/liddiard/appletini/requirements.svg?branch=master)](https://requires.io/github/liddiard/appletini/requirements/?branch=master)

![Appletinis make me feel fancy.](http://i.imgur.com/ENFVTr5.gif)

# Token auth example
`curl --data "username=value1&password=value2" https://localhost:8000/auth/token/login/`
`curl -X GET http://localhost:8000/v1/users/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'`

# Invariants

- Model names must be unique across the entire project namespace. E.g., you can't have an 'authors' app with an Author model and a 'reviews' app with an Author model.
- The authors.Organization with primary key 1 is the organization for which this instance of the CMS is being used.

# Design patterns

- API URLs for resources must be a pluralized, lowercased, and underscore-separated representation of the model name. E.g., an Author model should be accessible at /authors, and an InternalComment model should be available at /internal_comments.
