# To run the application
1. In main Folder LetsbloomAssignment , create a virtual environment 
```
python -m venv venv
```
2. Activate virtual environment by running Activate.ps1 in the venv/Scripts/ folder. Ex:

Windows:
```Windows
& venv/Scripts/activate
```
Linux:
```Linux
source venv/bin/activate
```
3.Install all required libraries listed in the requirements.txt
```
pip install -r requirements.txt
```
4. run the following commands
```  
python manage.py makemigrations
```
```
python manage.py migrate
```
5. to add dummy data to database run command
```
python manage.py loaddata fixtures/books.json --app BooksApp.Books
```
6. to start server 
```
python manage.py runserver
```
server should be running at http://127.0.0.1:8000/

# API endpoints 
```
1.
  GET /api/books/
  HTTP 200 OK
  Allow: OPTIONS, GET, POST
  Content-Type: application/json
  Vary: Accept
  
  {
      "status": "success",
      "data": [
          {
              "id": 1,
              "title": "The Space Between Worlds",
              "subtitle": "ultimate space scifi",
              "author": "Micaiah Johnson",
              "isbn": "9780593156919",
              "published": "2012-09-03"
          },
          {
              "id": 2,
              "title": "C++",
              "subtitle": "complete c++",
              "author": "stroupe",
              "isbn": "9780593126919",
              "published": "1999-04-02"
          }
          
      ],
      "message": null
  }

```
```
  2.

  POST /api/books/
  HTTP 201 Created
  Allow: OPTIONS, GET, POST
  Content-Type: application/json
  Vary: Accept
  
  {
      "status": "success",
      "data": null,
      "message": "added succesfully"
  }
  
  Example Data format for post 
   {
              "title": "Steve Jobs",
              "subtitle": "steve jobs : a biography",
              "author": "issac walter",
              "isbn": "7080593126910",
              "published": "2011-07-08"
   }
```

```
3.

PUT /api/books/<int:id>
HTTP 200 OK
Allow: OPTIONS, PUT
Content-Type: application/json
Vary: Accept

{
    "status": "success",
    "data": null,
    "message": "updated succesfully"
}
```

# API code 
code for API endpoints is located in BooksApp/views.py 
