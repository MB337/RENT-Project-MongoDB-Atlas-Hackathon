# RENT Project MongoDB Atlas Hackathon
The RENT project is an e-commerce where the user can rent products, previously uploaded by the website admin.<br/>
<a target="_blank" href="https://www.youtube.com/watch?v=jAQ3H5vML2E">Youtube Video</a>
# Installation
1) You need to clone this repository on your machine:<br/>
      ```
      git clone git@github.com:MB337/RENT-Project-MongoDB-Atlas-Hackathon.git
      ```
2) Add .env file to your project and set it like this:<br/> 
      ```
      COMPOSE_PROJECT_NAME=mongodb-hackathon
      MONGODB_URI=<YOUR-MONGODB-PROJECT-URI>
      ```
3) Your MongoDB Database should look like this:
      ```
      |ecommerce
      ---products
      ---stats
      ---report
      ```
4) If you have Docker:
      ```
      docker-compose up
      ```
   Else (note that you'll need to export env variables):
      ```
      python3 app.py
      ```
      

# Tools/Modules
Those are MongoDB services and modules or tool that I used:
- <a target="_blank" href="https://flask.palletsprojects.com/en/2.0.x/">Flask:</a> micro web framework written in Python.
- <a target="_blank" href="https://docs.atlas.mongodb.com/atlas-search/">Atlas Search:</a> Atlas Search provides options for several kinds of text analyzers, score-based results ranking, and a rich query language.
- <a target="_blank" href="https://pymongo.readthedocs.io/en/stable/">Pymongo:</a> Python distribution containing tools for working with MongoDB.
- <a target="_blank" href="https://www.chartjs.org/">Chart.js:</a> an open source JavaScript library for creating interactive and animated charts on web pages.
- <a target="_blank" href="https://axios-http.com/docs/intro">Axios:</a> Axios is a promise-based HTTP Client for node.js and the browser.
- <a target="_blank" href="https://getbootstrap.com/">Bootstrap 5:</a> Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.

# Category
This project is "E-Commerce Creation" category.

# Preview
<img src="https://i.imgur.com/tJEBJZb.png"/>

# More
Thanks for your attention, if you have any suggestions write me at <a href="mailto:mbmatteobianchi@gmail.com">mbmatteobianchi@gmail.com</a>

# Atlashackathon Runner Up project
https://dev.to/devteam/congrats-to-the-mongodb-atlas-hackathon-winners-4cc0
