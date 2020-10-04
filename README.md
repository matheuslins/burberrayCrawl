# Burberray Crawl

A spider from Burberray store! https://us.burberry.com/

The spider only capture women products.

### Environment vars

````.env
See the .env-example file to know the environments vars
````

### Pre Run

Create a virtualenv and install dependencies: ```make install``` 

### Running

If you just ro run without save in DB, use:

````python
scrapy crawl burberry
````
If you want to save in ElasticSearch and use Kibana to see the result, following this steps: 

````.env
1 - Set this var: SAVE_DB=True
2 - By default the host of ElasticSearch is the http://localhost:9200, but if you want to change it, 
    set this var with the new host. ES_HOST=<link_of_the_host>
````

While the spider is running and you can see the result here: http://0.0.0.0:5601/app/kibana in **Discover** tab