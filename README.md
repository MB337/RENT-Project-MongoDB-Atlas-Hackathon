# RENT Project MongoDB Atlas Hackathon
The RENT project is an e-commerce where the user can rent products, previously uploaded by the website admin.<br/>

# Installation
1) You need to clone this repository on your machine:<br/>
      ```bash
      git clone git@github.com:MB337/RENT-Project-MongoDB-Atlas-Hackathon.git
      ```
2) Add .env file to your project and set it like this:<br/> 
      ```bash
      COMPOSE_PROJECT_NAME=mongodb-hackathon
      MONGODB_URI=<YOUR-MONGODB-PROJECT-URI>
      ```
3) If you have Docker:
      ```
      docker-compose up
      ```
   Else (note that you'll need to export env variables):
      ```
      python3 app.py
      ```
      

# Tools/Modules
Those are MongoDB services and modules or tool that I used:
- <a href="https://flask.palletsprojects.com/en/2.0.x/">Flask:</a> micro web framework written in Python.
- <a href="https://docs.atlas.mongodb.com/atlas-search/">Atlas Search:</a> Atlas Search provides options for several kinds of text analyzers, score-based results ranking, and a rich query language.
- <a href="https://pymongo.readthedocs.io/en/stable/">Pymongo:</a> Python distribution containing tools for working with MongoDB.
- <a href="https://www.chartjs.org/">Chart.js:</a> an open source JavaScript library for creating interactive and animated charts on web pages.
- <a href="https://axios-http.com/docs/intro">Axios:</a> Axios is a promise-based HTTP Client for node.js and the browser.

# Category
This project is "E-Commerce Creation" category.

# More
Thank you for your attention, if you have any suggestions write me <a href="mailto:mbmatteobianchi@gmail.com">mbmatteobianchi@gmail.com</a>