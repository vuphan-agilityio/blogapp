# Django GraphQL Demo

Simple blog app created with Django, REST framework, GraphQL and SQLite

## Motivation

This is a simple application called `Blog App`. The purpose of this application is to present the outstanding features of GraphQL.

## Highlights

* Can use Django GraphQL with Django REST framework. It works OK, not conflict.
* Resolved issue: Best folder structure for large schemas.
* Integration with Django REST framework (only reuse Serializer for Mutations)

## Installation

```bash

pipenv install

```

## Up and runing

```bash

pipenv shell

bash bin/dj-migrate.sh

bash bin/dj-run.sh

```

Go to [GraphQL Interface](http://localhost:8000/graphql/) for the result.
