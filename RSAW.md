# rsaw
RSAW is a API wrapper for Random Stuff API.

visit project on [PyPi](https://pypi.org/project/rsaw/0.8/) (python package index)

## Examples
the best way to learn is too look at examples. Here are some examples for RSAW.
- - -
#### Installing RSAW

`pip install rsaw==0.8`
- - -
#### Setting Up client:
```py
from rsaw.v5.rsa import *
client = RandomStuff(key="OOGA BOOGA", server="main/backup")
```
with this client you can access all the functions for random stuff api.
The parameters with the client are: 

- debug (boolean, also broken so set it to false or dont use it)
- key (string)
- server (string it can be main or backup)
- plan (string, your plan with rsa for better server connection or something like that)
- - -
the first function is `ai_response`. it is used for the *ai* endpoint with RSA.
here is an example:
```py
from rsaw.v5.rsa import *
client = RandomStuff(key="OOGA BOOGA", server="main")
ai = client.ai_response(res_type="text", message="hello ai!", custom={'bot_name': 'John'})
print(ai)
```
The *ai* function has theese paramaters:
- message (string, what the ai will respond to)
- res_type (string, can either be text so it auto indexes everything to just the response or it can be json)
- custom (dict, use custom bot settings more info [here](https://api-docs.pgamerx.com/AI%20Response/optional-customisation/))

 
- - -
### Message backups:
message backups will make your function return a random string from a list instead of an error.

to do this:
```py
from rsaw.v5.rsa import *
client = RandomStuff(key="kanyewest", server="main")
client.set_backups(ai=['String', 'other string'], joke=['a'])
ai = client.ai_response(message='') #empty string gives error in RSA
print(ai)
```
This will print either `String` Or `other string` because of the backup we set up.
