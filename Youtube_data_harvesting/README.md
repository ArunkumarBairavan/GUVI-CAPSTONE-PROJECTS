YouTube-Data-Harvesting-and-Warehousing-using-SQL-MongoDB-and-Streamlit.

Problem Statement: The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels.

NAME : ARUNKUMAR BAIRAVAN

BATCH: DW60DW61

DOMAIN : DATA SCIENCE

DEMO VIDEO URL: https://youtu.be/DzmefPfC24c

LINKED IN URL : https://www.linkedin.com/feed/update/urn:li:activity:7099373233690345472/

The application should have the following features:

$ Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.

$ Option to store the data in a MongoDB database as a data lake. Ability to collect data for up to 10 different YouTube channels and store them in the data lake by clicking a button. Option to select a channel name and migrate its data from the data lake to a SQL database as tables.

$ Ability to search and retrieve data from the SQL database using different search options, including joining tables to get channel details.

$ YouTube API: You'll need to use the YouTube API to retrieve channel and video data. You can use the Google API client library for Python to make requests to the API.

$ Store data in a MongoDB data lake: Once you retrieve the data from the YouTube API, you can store it in a MongoDB data lake. MongoDB is a great choice for a data lake because it can handle unstructured and semi-structured data easily.

$ Migrate data to a SQL data warehouse: After you've collected data for multiple channels, you can migrate it to a SQL data warehouse. You can use a SQL database such as MySQL or PostgreSQL for this.

$ Query the SQL data warehouse: You can use SQL queries to join the tables in the SQL data warehouse and retrieve data for specific channels based on user input. You can use a Python SQL library such as SQLAlchemy to interact with the SQL database.

$ Display data in the Streamlit app: Finally, you can display the retrieved data in the Streamlit app. Overall, this approach involves building a simple UI with Streamlit, retrieving data from the YouTube API, storing it in a MongoDB data lake, migrating it to a SQL data warehouse, querying the data warehouse with SQL, and displaying the data in the Streamlit app.

Configuration:

1.Open the mainfile.py file in the project directory.

2.Set the desired configuration options:

3.Specify your YouTube API key.

4.Choose the database connection details (SQL and MongoDB).

5.Get the Youtube Channel ID from the Youtube's sourcepage

6.provide the Youtube Channel ID data to be harvested.

7.Set other configuration options as needed.

Usage:

1.Launch the Streamlit app: streamlit run mainfile.py

2.Run the mainfile.py script, make sure you have main and sql files in the same folder.

3.The app will start and open in your browser. You can explore the harvested YouTube data and visualize the results.

Contributing:

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1.Fork the repository.

2.Create a new branch: "git checkout -b feature/your-feature-name"

3.Make your modifications and commit the changes: "git commit -m "Add your commit message here"

4.Push your branch: "git push origin feature/your-feature-name"

5.Open a pull request on the GitHub repository, explaining the changes you made and why they should be merged.
