## Automating AWS with Boto3 
This repository contains some Python codes for manipulating AWS resources with Boto3 library. Here, the necessary keys required for accessing the AWS resources are supplied through environment variables in the run configurations. 
  
### The core concepts of Boto3:
1. **Resource:** It is a higher level object to connect to AWS services. As it is higher level, some operations might not be available with it.

2. **Client:** Low level object to work with AWS services. It has access to all operations, however, to use client you need to have the knowledge of working with python dictionaries.

3. **Meta:** Meta object helps you to enter into a client object using from a resource object.It is helpful when you are working with resource and at some point realize that some operations are not available through a resource object. 

4. **Session:** Configuration states are stored by session which is helpful to create resource and client objects.

5. **Collection:** It is used to iterate and manipulate resource objects. 

6. **Paginators:** are useful when you have more objects than the maximum limit of number of boto3 response object. For example, if you have 3000 objects and boto3 number of response object limit is 1000, then you have to create a paginator which will create 3 pages to access all 3000 objects. 

7. **Waiters:** used to block some services until certain state has been reached. One example can be, you delay the deployment of application until your EC2 instances enter into running state.      
