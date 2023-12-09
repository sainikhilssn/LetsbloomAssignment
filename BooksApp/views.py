from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Book
from .serializer import BookSerializer 


# end point 1 to get all books (get) , end point 2 to add new book  (post)
@api_view(['GET' , 'POST'])
def books(request) : 
    if request.method == 'GET' : 
        # get all books (slect * from books)
        books = BookSerializer(Book.objects.all() , many = True)         
        return Response({"status" : "success",
                         "data" :  books.data ,
                         "message" : None 
                        } , status= status.HTTP_200_OK)

    if request.method == 'POST' : 
        book_details = request.data
        # check if given data contains isbn (which is unique for each book) then if exists
        if ('isbn' in book_details) and Book.objects.filter(isbn =  book_details['isbn']).exists() : 
            return Response({"status" : "fail" , 
                             "data" : None ,
                             "message" : "book with this isbn already exists"
                            }, status=status.HTTP_400_BAD_REQUEST)
        
        # as it does not exists , validate request data 
        serializer = BookSerializer(data = book_details)

        if serializer.is_valid() : 
            # add to the database
            serializer.save()   
            return Response({"status" : "success",
                            "data" : None, 
                            "message" : "added succesfully"
                             } , status= status.HTTP_201_CREATED)
        
        return Response({ "status" : "fail",
                          'data': None, 
                          'message' : serializer.errors
                          } , status= status.HTTP_400_BAD_REQUEST)



# end point to update book , given book id 
@api_view(['PUT'])
def update_book(request , id) : 
    book_id = int(id) 
    print(request.data)
    try : 
        # if book with id exists then validate and update                   
        curr_book = Book.objects.get(id = book_id)
        # passing (book in db , book in request) for updation
        serializer = BookSerializer(curr_book , data = request.data)  

        if serializer.is_valid() : 
            # updating current book entity in database
            serializer.save()  
            return Response({ 'status' : "success",
                              'data' : None ,
                              'message' : "updated succesfully" 
                            }, status= status.HTTP_200_OK)
        
        return Response({ 'status' : "fail" ,
                          'data' : None , 
                          'message' : serializer.errors
                        } , status= status.HTTP_400_BAD_REQUEST)

    except Book.DoesNotExist: 
        # book does not exisits 
        return Response({ 'status' : 'fail',
                          'data' : None , 
                          'message' : "book does not exists"
                        }, status=status.HTTP_404_NOT_FOUND)
    
    





