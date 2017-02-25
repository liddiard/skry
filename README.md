# Skry

![Skry logo](http://i.imgur.com/vo1NjSk.png)

The extendable, decoupled CMS for small-to-medium-sized news organizations.

[![Requirements Status](https://requires.io/github/liddiard/skry/requirements.svg?branch=master)](https://requires.io/github/liddiard/skry/requirements/?branch=master)

## Overview

Skry was created for the [Daily Bruin](http://dailybruin.com) to unify the jobs of a patchwork of slow, pricey and/or isolated tools into a single CMS that does it all. 

The Daily Bruin's current workflow is split among at least five seperate systems:

1. Budget: a Django application where stories are pitched and assigned. It's super outdated and lacks a ton of features.
2. [Trello](https://trello.com): a kanban-style board planning tool where people make requests for photos/graphics/etc. It's nice but doesn't integrate with anything else in the workflow.
3. [Camayak](http://www.camayak.com): an editing and publishing tool for newsrooms. It's slow and pricey.
4. [WordPress](http://wordpress.com): needs no introduction. Well-maintined, huge community, but gross and difficult to develop anything custom with (ugly PHP, mixing logic and presentation, etc, etc).
5. [meow](https://github.com/daily-bruin/meow): Daily Bruin's homegrown social media poster, also a Django app. It's great but also doesn't integrate with anything else in the workflow.

Skry is an attempt to bring this *stuff* – all of which ultimately revolves around **stories** we produce, from the pitch, to the writing and editing, to the art and multimedia that might be associated with it, to its display on the website and its promotion on social media – into one system. Less copying and pasting, less mentally trying keeping track of where things are as you switch between several systems that don't talk to each other, less prone to errors in communication when the systems do try to talk with one another, easier to develop and customize. That's the dream.

### Decoupled design

Sounding monolithic? Skry adheres to a separation of concerns in a different way, following the [decoupled CMS paradigm](http://decoupledcms.org), concepts of which major CMSs like WordPress and Drupal have begun to adopt. The website describes the difference between a "monolithic" CMS approach vs a "decoupled" CMS approach best:

#### Monolithic

> The CMS provides content storage, routing, templating, editing tools, the kitchen sink. Probably you’re even tied to a particular relational database for content storage. Want to use a cool new editor like Aloha, or a different templating engine, or maybe a trendy NoSQL storage back-end? You’ll have to convince the whole CMS project or vendor to switch over.

#### Decoupled

> There is a content repository that manages content models and how to store them. This could be something like JCR, PHPCR, CouchDB or Midgard2. Then there is a web framework, responsible of matching URL requests to particular content and generating corresponding web pages. This could be Drupal, Neos, Django, CodeIgniter, Midgard MVC, or something similar. And finally there is the web editing tool. The web editing tool provides an interface for managing contents of the web pages. This includes features like rich text editing, workflows and image handling.

If you're not convinced on the benefits of this architecture, take a moment to read through the [decoupled CMS website](http://decoupledcms.org). It's really brief, and it explains with pictures and examples and stuff.

Skry is the "content repository" component of the CMS. Built on [Django Rest Framework](http://www.django-rest-framework.org) and PostgreSQL, it provides the database and API for everything the CMS needs to store and retrieve.

Skry is also decoupled in its application design. It follows [Django's model of projects and apps](http://stackoverflow.com/a/19351042/2487925), where each app is a "submodule" of the entire project responsible for a specific component of the CMS's functionality. For example, there's an app that handles authentication, an app that handles revision history, and an app that handles art requests. More on this below.

### Fully exposable models API

Skry has an API endpoint that exposes the entire database design (optionally behind authentication). It exposes models (tables), fields (columns), and field constraints. This enables you to create an entirely programatically-generated admin/editing interface for the CMS. Added a model? Changed a field constraint? The frontend editor updates automatically to reflect the new database schema.

### On-the-fly image generation

Request an image of any dimensions and Skry will deliver it dynamically, caching the sized image on the filesystem. In contrast, WordPress generates predefined image sizes. If you want a custom size, you're out of luck – resize it yourself in Photoshop. Also, all those sizes and crops that you're not actually using anywhere in most stories? They're just sitting on the filesystem taking up unnecessary space.

### Revision history

Skry has full-featured model revision history thanks to [django-reversion](https://github.com/etianen/django-reversion). List, view, and restore previous versions all through the API.

### Extendability

Skry's component-based application architecture makes it easy to add your own applications, mixing and matching with what Skry provides currently.

## Setup

Sold? Want to try it out? Follow the (hopefully) simple(ish) setup instructions!

### Prerequisites

- Python 2.7
- pip
- virtualenv (install it with `pip install virtualenv`)
- PostgreSQL ([Postgres.app](https://postgresapp.com) is great if you're on macOS)
- Redis: required for production, optional in development (used for caching). [Get it here.](https://redis.io/download))

### Instructions

1. Create and activate a virtualenv for the project: `virtualenv skry && cd skry && source bin/activate`
2. Clone the repo: `git clone https://github.com/liddiard/skry.git repo`
3. Install the requirements: `pip install -r requirements.txt`
4. Start Postgres (just launch the app if you're on macOS)
5. Sync the database and apply migrations: `python manage.py syncdb && python manage.py migrate`
6. Start the server! `python manage.py runserver`

## Code layout

Skry is built on Django Rest Framework (DRF). If you're not familiar with it, Skry's code layout will also be unfamiliar to you. If you are familiar, you'll see that 90% of the source code is basically just DRF's declarative "model + serializer + view + routing" layout across several applications. 

The basic concept is each app has three main files: 

1. a `models.py` file that defines the database tables an rows (i.e. what data can be stored)
2. a `serializers.py` file that defines how the data in the database is serialized into JSON when it's passed to the client
3. a `view.py` file that defines how a client can request the serialized data (e.g. what fields can be filtered and sorted by)

Complete or at least read through the [DRF quickstart tutorial](http://www.django-rest-framework.org/tutorial/quickstart/) and you'll understand what's going on a lot better.

### Applications

Below is a description of each of the apps in Skry. Apps correspond to the top-level directories in the repo with the execption of the `project` directory which contains configuration for the entire project.

#### Access

Handles the authentication and management of CMS users. It doesn't define any of its own models but instead uses the models provided by [Django's built-in and very full-featured user authentication system](https://docs.djangoproject.com/en/1.10/topics/auth/).

#### Attachments

Contains "attachments" to stories, including images, video, audio, reviews (i.e. of a movie or restaurant), and polls. The image model has a method to get a resized image at any specified resolution.

#### Authors

The authors app contains definitions for authors (big surprise). In Skry, authors are intented to be associated with any type of content that has a creator, including stories, photos, videos, etc. An author can be:

- a person associated with an organization, e.g. Joe Bruin who works at the Daily Bruin at takes photos for them),
- a person not associated with an organization, e.g. Josephine Bruin who lives in Westwood and wrote a letter to the editor)
- an organization not associated with a specific person, e.g. Getty Images (who let us use their photo) or a group with lots of members that wrote an open letter

Authors can optionally be associated with users, but authors and users are **not** the same thing. This is an important distinction. 

A user is someone who has access to something in your content management system. Users have usernames and passwords to log in to the system. Users are affiliated with your organization. 

An author is someone who creates a piece of content (story, image, etc.). Authors may or may not be affiliated with your organization.

The reason for this distinction lies in the affiliation of authors with your organization. There's no reason to have a user – with access to your CMS – for a Westwood resident who sent in a submission. A writer who is working for your organization now may not be working for you in ten years. There is no need to have a user – with a username and password – for this person who wrote an article ten years ago. 

In fact, for college newsrooms, 95% of your authors are probably people who no longer work for your news organization. Having hundreds of "inactive" user accounts for long-gone people you don't even know is difficult to reason about and has the potential to create security holes. 

Decoupling the idea of an "author" from an "user" fixes this problem. An author is a person (or organization) who has created a piece of content. A user is a person who has access to your CMS. Users are transient; they come and go. Authors are permenant; they're always associated with their work.

#### Comments

The comments app, for now, just contains *internal* comments, intended for people within your organization to communicate with one another and leave notes about a story or art request as it goes through the process from idea to published work. This app could be extended to handle *external* comments; i.e. comment from people visiting your website/app/etc., probably in conjunction with an "external user" user model. External commenents were not implmented because:

1. opening up user accounts to the public world carries with it a lot of concerns – account verification, account abuse, spam, copyright infringement, etc.
2. we use [Disqus](https://disqus.com) so it handles all this public-facing commentary for us

#### Core

Contains the core models of the Skry CMS. The core of Skry is a story model which is used from the story pitch all the way through the editing process to the publishing of the story. A story is always in a workflow status.

Pages are also in core. Pages are unrelated from stories. They're one-off pages on your public-facing website that don't really fit into any particular model. Examples include an "about us" page or a public secure submission page.

#### Display

The display app controls how stories are displayed on your public-facing frontend(s). It includes support for things like page templates (similar to WordPress templates) and per-story custom stylesheets and scripts.

#### Organization

The organization app controls how your stories are organized. It includes two models: sections and tags. 

Sections typically correspond to departments and/or beats in your newsroom and are rarely updated. Examples include Sports, Opinion, and Video. Sections can be nested to create subsections like Football, Editorials, and Breaking News Videos.

Tags are more ad-hoc than sections. They can't be nested and are usually used for a one-time event or every-once-in-a-while recurring coverage around a particular theme. For example, "campus flooding" or "student government elections".

#### Requests

Requests are internal communication, typically from one department to another, asking for a particular story component. Examples include photo requests, graphic requests, and illustration requests, each of which have their own model subclassing `ArtRequest` in this app.

#### Revisions

The revisions app provides simple verision control and the ability to view or roll back previous changes. It has no models of its own but uses the well-documented [django-reversion extension](https://django-reversion.readthedocs.io/en/stable/) and simply provides a REST API on top of it.

#### Sports

The sports app stores data specific to sporting events. It contains models for sports (e.g. Football, Basketball), schools (e.g. UCLA, Stanford), and games (e.g. a UCLA v. Stanford football game on x date). It's intended to be used to display game information along with a sports game preview story or to display the previous/upcoming games in a particular sport.

## Development notes

### Token auth example

`curl --data "username=value1&password=value2" https://localhost:8000/auth/token/login/`

`curl -X GET http://localhost:8000/v1/users/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'`

### Invariants

- Model names must be unique across the entire project namespace. E.g., you can't have an 'authors' app with an Author model and a 'reviews' app with an Author model.
- The authors.Organization with primary key 1 is the organization for which this instance of the CMS is being used.

### Design patterns

- API URLs for resources must be a pluralized, lowercased, and underscore-separated representation of the model name. E.g., an Author model should be accessible at /authors, and an InternalComment model should be available at /internal_comments.
