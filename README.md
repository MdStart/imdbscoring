# IMDB Scoring RESTFul api Demo app
### Demo REST api's to allow users to enter imdb scores in the db and retrieve, edit, delete or search


# IMDB Scoring URLs
```python
    http or https for initials with <host_address>
    
    <host_address>/imdb-scores/list # To list the imdb scores with pagination 
    <host_address>/admin # Admin login url
    <host_address>/create # To create a new imdb score entry in the database
    <host_address>/<score_id>/edit #To edit existing records based on id
    <host_address>/search # Allows to search a record based on search fields
    <host_address>/<score_id>/delete #Deletes a record based on id
    <host_address>/doc # Swagger API documentation url extension

```

### To test these api's create superuser admin credential from terminal like the below sample auth credentials

```python
# Sample API auth credentials -  
username:- score
pass:- pass123
```

# Note-
### These REST API's are just for demo purpose and has no relation with the real imdb application or the imdb api's.   