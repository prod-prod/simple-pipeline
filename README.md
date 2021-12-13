## About

A simple pipeline implemented with python3.

## Requirements

For easy reproduction of the scenario, we use Docker. Implementation is done in python3. To connect to the data bases from python3 we use oficcial libraries.

## How to run

Make sure you have docker installed. Visit [Docker Official Page](https://docs.docker.com/engine/install/ubuntu/).

Install python dependencies:
```bash
python pip3 install -r requirements.txt
```

Start the docker:
```bash
bash start_db.sh
```

Now you can on any iteration run insert data (emulation of the production DB):
```bash
python3 insert_data.py
```

And you can run pipeline:
```bash
python3 copy_data.py
```
