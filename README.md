# Capstone Project Backend

This repository contains the backend service for the capstone project built using Flask, MySQL, and Google Cloud Pub/Sub. The project is designed with a modular architecture to support a scalable and maintainable codebase.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Pub/Sub Integration](#pubsub-integration)
- [Testing and Debugging](#testing-and-debugging)
- [License](#license)

## Overview

This backend service provides RESTful API endpoints using Flask to interact with a MySQL database and integrates with Google Cloud Pub/Sub for asynchronous messaging. It is designed to:
- Serve API requests and respond with data from the MySQL database.
- Publish and subscribe to messages using Google Cloud Pub/Sub.
- Keep sensitive credentials secure using environment variables.

## Features

- **Flask API**: Serves endpoints such as `/` (welcome) and `/users` to fetch user data.
- **MySQL Database**: Stores user data and other application information.
- **Google Cloud Pub/Sub**: Enables asynchronous message processing between different parts of the application.
- **Modular Structure**: Organized codebase separating configuration, database logic, API endpoints, and utility functions.

## Technologies Used

- [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
- [Google Cloud Pub/Sub](https://cloud.google.com/pubsub)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## File Structure

```plaintext
my-capstone-backend/
├── .env                   # Environment variables (keys, credentials, connection strings)
├── .gitignore             # Files to ignore in version control
├── README.md              # Project documentation (this file)
├── requirements.txt       # Python package dependencies
├── app.py                 # Flask application entry point
├── config.py              # Configuration loader (loads .env variables)
├── db.py                 # Database connection helper (MySQL connector)
├── producer.py            # Publishes messages to Google Cloud Pub/Sub
├── consumer.py            # Consumes messages from Google Cloud Pub/Sub
└── sql/
    └── db_model.sql       # SQL script for creating the database schema
