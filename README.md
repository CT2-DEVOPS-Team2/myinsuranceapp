"# My Insurance App" 

<<<<<<< HEAD
"hola esto es una actualizacion"
"team 2"
"NEW TEST"
=======
"actualizacion"
"Elleta is awesome yay!!"

>>>>>>> ce9114da0aeb2d97ae4bd0da003ebde93c9e934f
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


 py -m unittest discover -s project/acceptancetest -v