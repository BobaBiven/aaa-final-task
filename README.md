# pizza
This is a final project in Python basic level course in Avito Analytics Academy.


## Installation Instructions
1. Clone this repository with:

```
git clone https://github.com/BobaBiven/aaa-final-task
```

2. Create a virtual enviroment with:
(Further - assuming you have python3 installed, if not - install first.)
```
python3 -m venv venv
```

3. Install all the needed packages with requirements.txt file.
```
pip install -r requirements.txt
```

Now you are good to go.

You can also run tests to see if all working good with:
```
python3 -m pytest -v 
```

## Usage instructions
Activate the virtual enviroment first:
```
source venv/bin/activate
```
We will operate with 'cli.py file'

By running
```
python3 cli.py
```
you can see all the commands this pizzeria has.

### menu
You can display menu (all avaliable pizzas and sizes) with 'menu' command:
```
python3 cli.py menu
```

### order
You can order a pizza from menu with 'order' command (the pizza name has to be exactly like in menu).
You can also specify, if you want it to be delivered to you with --delivery flag and if you want it to be extra-large with --large flag.
Example of ordering extra-large Pepperoni with delivery:
```
python3 cli.py order Pepperoni --large --delivery
```
That will also output baking and delivering time (both are random from 0 to 5 seconds).

