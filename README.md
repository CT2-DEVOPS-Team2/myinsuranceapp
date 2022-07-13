"# My Insurance App" 

Dependencies :
	
    - If you have old version of project: pip uninstall -r requirements.txt
	- pip install -r requirements.txt

Init database :

    - py project/init/init_db.py

Run the server:

    - py runserver.py
    - Access web at: http://localhost:5000/
    - API at: http://localhost:5000/api/v1/


Authentication:
    - For web and API use:
      - Email: jd@myinsuranceapp.com
      - Password: passwordjd

API endpoints:
    - Authenticate: http://localhost:5000/api/v1/token
      - Method POST
      - Payload {email:<email_value>,password:<pass_value>}
    - All endpoints require token in header
      - {Aunthenticate: Bearer <token>}
    - Users: http://localhost:5000/api/v1/users
    - Products: http://localhost:5000/api/v1/products


 py -m unittest discover -s tests/acceptancetest -v

 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY5ODM0NywianRpIjoiMTMyMDQwODgtMGUzZi00NjgwLWFhY2QtMzU5NDJhNmRlYjlkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjU3Njk4MzQ3LCJleHAiOjE2NTc2OTkyNDd9.hcUUMKI_r3L77kiKmgUSA9R0llLor4og6lX0uFWGWWE