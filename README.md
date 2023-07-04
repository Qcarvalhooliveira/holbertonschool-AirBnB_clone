# **AirBnB clone - The console** :computer:
![This is an image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png)

## **Description** :speech_balloon:

* The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

* We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## **What we should learn from this project:** :bookmark_tabs:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## **Tasks**

* ## **0. README, AUTHORS**
```
* Write a README.md:
  * description of the project
  * description of the command interpreter:
  * how to start it
  * how to use it
  * examples
* We should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
* We should use branches and pull requests on GitHub - it will help you as team to organize your work
```

* ## **1. Be pycodestyle compliant!**
```
* Write beautiful code that passes the pycodestyle checks.
```

* ## **2. Unittests**

All your files, classes, functions must be tested with unit tests

* ## **3. BaseModel**
```
Write a class BaseModel that defines all common attributes/methods for other classes:

models/base_model.py
Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at with the current datetime
to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
```

