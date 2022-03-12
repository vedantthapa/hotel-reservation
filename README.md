# Hotel-Reservation

Solution to REST API project posted in the MCDA5550 class by Prof. Sanjeevi Ramachandran

## Functions

1. Hotels can be viewed and new hotels can be added into the database.
2. Users can book an Hotel by providing the hotel name, check-in date, check-out date and information of the guests.
3. Check-in and Check-out date validations are added.
   - Check-out date must be greater than the check-in date.
   - Check-in date must be greater than the current date.
4. Character field validations are added.
   - City field in the Hotel model must only contain alphabets.
   - Name field in the Guest model must only contain alphabets.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/vedantthapa/django-hotelapi.git
$ cd django-hotelapi
```

Then install the dependencies:

```sh
# using pip
$ pip install -r requirements.txt

# using Conda
$ conda create --name <env_name> --file requirements.txt
```

Once the dependencies has finished downloading, edit your database settings in the `DATABASES` dictionary in the `hotelsite/settings.py` file.

After configuring the database run the below commands to add tables into the schema.

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Now, run the app by executing the following command

```sh
$ python manage.py runserver
```

## API Endpoints

Access endpoints using Postman or any other API platform to do a GET or POST request.

- Hotel: `http://127.0.0.1:8000/app/hotels/`

- Booking: `http://127.0.0.1:8000/app/booking/`

### POST Request Params

#### Hotel

```json
{
  "name": "Hilton",
  "email": "hilton@hilton.ca",
  "city": "Dartmouth"
}
```

#### Booking

```json
{
  "hotel": "Hilton",
  "check_in": "2024-03-08",
  "check_out": "2024-03-10",
  "guest": [
    {
      "name": "Mike",
      "age": 24,
      "email": "mike@gmail.com"
    },
    {
      "name": "Robin",
      "age": 39,
      "email": "rj@yahoo.com"
    }
  ]
}
```
