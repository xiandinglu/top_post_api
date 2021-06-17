# top_post_api
Process the data from API endpoints

This repo shows the simple ETL of data taking from two API endpoints.
- comments endpoint – https://jsonplaceholder.typicode.com/comments
- Posts endpoint – https://jsonplaceholder.typicode.com/posts

This repo create an API with list of Top Posts ordered by their number of Comments.
The API response contains the following fields: 
	- post_id 
	- post_title
	- post_body 
	- total_number_of_comments
