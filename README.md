## Prerequisite
- Python 3.10
- Connection to a running Kafka instance

## How to

### Step 1: 
Make a `.env_custom` file (in the root folder) and update content based on `.env_template` file

### Step 2:
Setup and active the virtual env
```
pipenv install
pipenv shell
```

### Step 3:
Start Kafka consumer using the following command
```
python manage.py payoutpool
```

### Note
You can make a dump request to Kafka using
```
python manage.py dumprequest
```

## TODO
- Validate data from Kafka
- Dispatch result somewhere to show it for end user
- I heard [Faust](faust.readthedocs.io/en/latest/) provides some interestring features, will give a try later