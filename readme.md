# RESTful BucketList API built Test Driven Development

## Description
This is simply a bucketlist API which lists the goals an individual wants to achieve, dreams to fulfill and those desired life experiences (like traveling to Dubai and also, having worked at Google and or seeing the inside of Intel and Samsung manufactoring :stuck_out_tongue_winking_eye:)

## Installation
You can and should create a virtual environment for it before you run it on your machine.

Use the link found [here](https://virtualenvwrapper.readthedocs.io/en/latest/) to setup a virtualenvwrapper on your dev machine.

To create a virtual environment, simply run `mkvirtualenv bucketlist` OR `virtualenv bucketlist`. You can run your own command to create it though, as most will default to running `virtualenv venv`. Either case, it works.

However, by setting the project directory, you can eventually come back and run `workon bucketlist` and it will immediately take you the project directory and well as activate the virtual environment.

Finally run the below command to install all the necessary packages and modules. 

```
pip install -r requirements.txt
```

## Setup and Run
Simply run `python3 app.py` or `python app.py` (condition that your default python is python3 and not python2.7).
If you are using a virtual machine (vagrant) like I am, then you can do the following:

Change directory to where the source code is located on the VM (eg. `/home/vagrant/Codes/bucketlist`).
Run `flask run --port=8000 --host=192.168.44.10` where `192.168.44.10` is the IP of my VM. Change it to reflect to yours.

Ensure to also have your database setup and running on your machine. In this case we are using Postgresql. Follow the link here, [Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04) to setup on your machine (VM in my case.)

## Tests
Run the below command to execute the tests against the bucketlists

'''
python tests/test_bucket.py
'''

## Contribution and Acknowledgements

This fun project was built based on a blog I had read earlier on about TDD which can be found here, [Build a RESTful API with Flask the TDD Way](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way). However there are some slight variations if you are observant.

The link shared above have some minor mistakes here are there which have been fixed in this repository. In case you can to learn more about TDD, kindly visit the link at [Intro to Flask Test Driven Development](https://github.com/mjhea0/flaskr-tdd)

Thank you.