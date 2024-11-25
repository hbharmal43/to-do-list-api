# to-do-list-api
Build a RESTful API for a simple to-do list application
Ill use Flask

GET -- to retrive any information
POST -- to add any new information
PUT -- to update given info
DELETE -- to delete a resource

Info on how to run: 
    execute the main.py file via terminal : python main.py

    Open Postman and paste the link for the specific tasks:
        1) want to view all the to-do's:
            http://127.0.0.1:5000/view by using GET function
        2) Adding new to-dos
            http://127.0.0.1:5000/view by using POST function
            input values according to the format:
                title: " "
                description: " "
                done: True or False
                priority : Higher the priority, higher the number and vice-versa
        3) Edit the to-dos:
            First use GET to view the information stored for the id 
            http://127.0.0.1:5000/edit/id
            
            Use PUT method in postman to change the values accordingly
            if done key changed to True it will automatically delete that to-do

        4) for deleteing the notes:
            use DELETE method from postman and use this link to delete the specif file with its id             
            http://127.0.0.1:5000/edit/id

Commetns form this bearded ass guy;
    