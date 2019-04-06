# etl_immunizations
# ETL Project - by Jamuna/Keegan/Eddie
# This is to practice the ETL process using sqlalchemy, pandas and pymysql and bring'em all together using flask

#Step_1: Thought of a task.

#Step_2: Task is to list all the kindergarten immunizations done in the year 2016 for the State of Washington.

#Step_3: Searched and identified datasets that can answer our question.

#Step_4: Data Source: http://data.gov, 
         Datasets identified: 1.Kindergarten_Immunization_Data__2016-17
                             2.WAOFM_-_April_1_-_Population_by_State__County_and_City__1990_to_Present
                             
#Step_5: Write SCHEMA to create the database and the table to hold data.

#Step_6: Saved the SCHEMA in 'schema.sql' file.

#Step_7: Create the database objects in MySql using the above SCHEMA.

#Step_8: The E-xtraction, T-ransformation, and L-oading of the data have been separated in three different files namely;
  'extract.py' - Extracts data from the given urls, transfers into pandas dataframes.
  'transform.py' - Performs cleaning up, aggregation and combining of the dataframes.
  'load.py' - Loads the combined dataframes onto the MySql database.
  
#Step_9: To retrieve a jsonified version of the above data, the following had to be performed:
  1. From the Windows command prompt, within the active Python environment(PythonData), 
      a. Generated a mysqldump of the database (mysqldump -h<localhost> <db_name>,-u<uname> and -p<pwd>).
      b. Saved the output onto a '<database_name>.sql' file.
  2. Using the DB Browser for sqlite's 'import' from .sql option(using the above .sql file), replicated the database that was created in
         Step#7 above.
  3. Saved the file as '<database_name>.sqlite'.
  4. Created 'app.py' using sqlalchemy, flask, json, and requests.
  
#Step_10: Created a repo and uploaded our ETL project!
