from flask import Flask, app
import requests
import pandas as pd
import json


app = Flask(__name__)

#Get Top Post
comment_url = 'https://jsonplaceholder.typicode.com/comments'
post_url = 'https://jsonplaceholder.typicode.com/posts'

def get_data(url):
    data = requests.get(url)
    json_data = data.json()
    df = pd.DataFrame(json_data)
    return df

comment_df = get_data(comment_url)
post_df = get_data(post_url)

summary_comment = comment_df.groupby(['postId']).size().reset_index(name='number_of_comments')
summary_comment = summary_comment.rename(columns={'postId':'id'})

full_df = post_df.merge(summary_comment, on='id', how='left')
full_df = full_df.sort_values(by=['number_of_comments'])
top_post = full_df[['id','title','body','number_of_comments']]
top_post = top_post.rename(columns={'id':'post_id', 'title':'post_title', 'body':'post_body', 'number_of_comments':'total_number_of_comments'})
response = json.dumps(json.loads(top_post.to_json(orient='records')), indent=2)


@app.route('/')
def top_post():
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8080)
