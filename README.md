# **AirBnB clone - The console** :computer:
![This is an image](https://github.com/Qcarvalhooliveira/holbertonschool-AirBnB_clone/blob/39cdc489e35389209ad336fcb8b49857d0b21a76/65f4a1dd9c51265f49d0.png)

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

# **Project Files**

|     Directories                |    Files                                                           |
|--------------------------------|--------------------------------------------------------------------|
|models                          |__init__.py, amenity.py, base_model.py, city.py, place.py, review.py|                 |                                |state.py, user.py                                                   |
|models/engine                   |__init__.py,  file_storage.py                                       |
|tests                           |__init__.py                                                         |
|tests/test_models               |__init__.py, test_amenity.py, test_base_model.py, test_city.py,     |
|                                |test_place.py, test_review.py, test_state.py, test_user.py          |
|tests/test_models/test_engine   |__init__.py, test_file_storage.py                                   |
|AUTHORS                         |                                                                    |
|README.md                       |                                                                    |
|console.py                      |__init__.py                                                         |

## **USAGE** :memo:

* Our command interpreter will work following these steps:

> Step 1: Clone our repository using this command, (you need to have git installed on your machine first):
```
https://github.com/Qcarvalhooliveira/holbertonschool-AirBnB_clone.git
```
> Step 2: Change directory to :
```
cd holbertonschool-AirBnB_clone
```
> Step 3: Run the command interpreter:
```
./console.py
```
Exiting the command interpreter when you want to exit, you can use one of the following methods:


> 1: Type the command "quit"
```
quit
```
> 2: Press on Ctrl + D


## **EXEMPLE**

```
queise@DESKTOP-AHLKCP0:~/holbertonschool-AirBnB_clone$ ls
AUTHORS    __init__.py  file.json            models              test_base_model_dict.py         tests
README.md  console.py   generate_authors.sh  test_base_model.py  test_save_reload_base_model.py
queise@DESKTOP-AHLKCP0:~/holbertonschool-AirBnB_clone$
```


## **Testing** :warning:

* Our shell should work like this in interactive mode:

```
queise@DESKTOP-AHLKCP0:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
queise@DESKTOP-AHLKCP0:~/holbertonschool-AirBnB_clone$
```

* But also in non-interactive mode:

```
```

## **Tasks** :books:

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

* models/base_model.py
* Public instance attributes:
    * id: string - assign with an uuid when an instance is created:
         * you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
         * the goal is to have unique id for each BaseModel
    * created_at: datetime - assign with the current datetime when an instance is created
    * updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
* __str__: should print: [<class name>] (<self.id>) <self.__dict__>
* Public instance methods:
    * save(self): updates the public instance attribute updated_at with the current datetime
    * to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
        * by using self.__dict__, only instance attributes set will be returned
        * a key __class__ must be added to this dictionary with the class name of the object
        * created_at and updated_at must be converted to string object in ISO format:
            * format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            * you can use isoformat() of datetime object
        * This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
```

* ## **4. Create BaseModel from dictionary**
```
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

```<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
Update models/base_model.py:```

    * __init__(self, *args, **kwargs):
        * you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
        * *args won’t be used
        * if kwargs is not empty:
             * each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
             * each value of this dictionary is the value of this attribute name
             * Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
         * otherwise:
             * create id and created_at as you did previously (new instance)
```

* ## **5. Store first object**
```
Now we can recreate a BaseModel from another one by using a dictionary representation:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

    * Python doesn’t know how to convert a string to a dictionary (easily)
    * It’s not human readable
    * Using this file with another program in Python or other language will be hard.
So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

```<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>```

Magic right?

Terms:

    * simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }
    * JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'

Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

    * models/engine/file_storage.py
    * Private class attributes:
        *__file_path: string - path to the JSON file (ex: file.json)
        * __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
* Public instance methods:
    * all(self): returns the dictionary __objects
    * new(self, obj): sets in __objects the obj with key <obj class name>.id
    * save(self): serializes __objects to the JSON file (path: __file_path)
    * reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update models/__init__.py: to create a unique FileStorage instance for your application

    * import file_storage.py
    * create the variable storage, an instance of FileStorage
    * call reload() method on this variable

Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

    * import the variable storage
    * in the method save(self):
        * call save(self) method of storage
    * __init__(self, *args, **kwargs):
        * if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
```

* ## **6. Console 0.0.1**
```
Write a program called console.py that contains the entry point of the command interpreter:

    * You must use the module cmd
    * Your class definition must be: class HBNBCommand(cmd.Cmd):
    * Your command interpreter should implement:
        * quit and EOF to exit the program
        * help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
        * a custom prompt: (hbnb)
        * an empty line + ENTER shouldn’t execute anything
    * Your code should not be executed when imported
```

* ## **7. Console 0.1**
```
Update your command interpreter (console.py) to have these commands:

    * create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        * If the class name is missing, print ** class name missing ** (ex: $ create)
        * If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
    * show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        * If the class name is missing, print ** class name missing ** (ex: $ show)
        * If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
        * If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        * If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
    * destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        * If the class name is missing, print ** class name missing ** (ex: $ destroy)
        * If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        * If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        * If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
    * all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
        * The printed result must be a list of strings (like the example below)
        * If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
    * update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        * Usage: update <class name> <id> <attribute name> "<attribute value>"
        * Only one attribute can be updated at the time
        * You can assume the attribute name is valid (exists for this model)
        * The attribute value must be casted to the attribute type
        * If the class name is missing, print ** class name missing ** (ex: $ update)
        * If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
        * If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
        * If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
        * If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        * If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
        * All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
        * id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
        * Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

* ## **8. First User**
```
Write a class User that inherits from BaseModel:

    * models/user.py
    * Public class attributes:
        * email: string - empty string
        * password: string - empty string
        * first_name: string - empty string
        * last_name: string - empty string
Update FileStorage to manage correctly serialization and deserialization of User.

Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.```



* ## **9. More classes!**
```
Write all those classes that inherit from BaseModel:

    * State (models/state.py):
        * Public class attributes:
            * name: string - empty string
    * City (models/city.py):
        * Public class attributes:
            * state_id: string - empty string: it will be the State.id
            * name: string - empty string
    * Amenity (models/amenity.py):
        * Public class attributes:
            * name: string - empty string
    * Place (models/place.py):
        * Public class attributes:
            * city_id: string - empty string: it will be the City.id
            * user_id: string - empty string: it will be the User.id
            * name: string - empty string
            * description: string - empty string
            * number_rooms: integer - 0
            * number_bathrooms: integer - 0
            * max_guest: integer - 0
            * price_by_night: integer - 0
            * latitude: float - 0.0
            * longitude: float - 0.0
            * amenity_ids: list of string - empty list: it will be the list of Amenity.id later
    * Review (models/review.py):
        * Public class attributes:
            * place_id: string - empty string: it will be the Place.id
            * user_id: string - empty string: it will be the User.id
            * text: string - empty string ```


* ## **10. Console 1.0**
```
Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!
```

* ## **AUTHORS** :black_nib:

* **Queise Carvalho de Oliveira** - [Queise Carvalho de Oliveira](https://github.com/Qcarvalhooliveira)
