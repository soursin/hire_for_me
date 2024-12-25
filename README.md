# HireMe

## LinkedIn Job Scraper and Backend Server

This project consists of two parts:

LinkedIn Job Scraper: A Python script that scrapes job listings from LinkedIn and stores them in a MongoDB database.

Backend Server: A Node.js Express backend that serves job data through an API and provides basic filtering for job listings.

## Features

Scrapes job listings from LinkedIn using Selenium and stores the data in a MongoDB database.
A REST API to filter job listings based on location, skills, description, and experience.
Database schema for job listings and user profiles.

### Notes

First run the scrapper before backend

## Scraper Setup (Python)

### Requirements

Python 3.x  
MongoDB (local or remote)  
Selenium  
Firefox (with geckodriver) or ChromeDriver

#### Setup

Install all files in requirement.txt
Just run the script.py file first

## Backend Server Setup (Express.js)

#### Requirements

#### Node.js (v14 or higher)

#### MongoDB (installed locally or using a cloud instance like MongoDB Atlas)

#### TypeScript

Clone the repository  
Create .env file with our own database name , email and password  
npm install
