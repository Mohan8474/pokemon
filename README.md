# pokemon


Pokemon project

## Installation

1. Clone the repository:
    https://github.com/Mohan8474/pokemon.git


2. Navigate to the project directory:

    cd pokemon


3. Create a virtual environment and activate it:

    python3 -m venv venv

    source venv/bin/activate


4. Install the dependencies:

    pip install -r requirements.txt

## Usage

1. Load the intial data

    python3 load__data.py

2. Run the application

    flask run 

    or
    
    run the run.py file

3. Access the API Endpoints

   - Open your web browser or use an API testing tool (e.g.Postman).

   - Use the following base URL to access the API endpoints:

     ```
     http://127.0.0.1:5000/pokemon
     ```

   - Endpoint 1: `/pokemon`
     - Method: GET (To retrieve all pokemon)
     - Method: POST (To create a new pokemon(single and multiple) )
     - Method: PUT (To Update a pokemon(single and multiple))
     - Method: DELETE (To Delete all pokemon)

   - Endpoint 2: `/pokemon/{id}`
     - Method: GET (To retrieve pokemon based on id)
     - Method: PUT (To update pokemon based on id)
     - Method: DELETE (To delete pokemon based on id)
 



