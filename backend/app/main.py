from fastapi import FastAPI
from data import article_list
from fastapi.exceptions import HTTPException

app = FastAPI()

fake_ass_data = [{'name': 'Azeem', 'mobile': 123}, {'name': 'Mariya', 'mobile': 345}, {'name': 'Zuni', 'mobile': 100}]

@app.get('/items/')
async def get_items(skip: int = 0, limit: int = 10):
    return fake_ass_data[skip: skip + limit]

@app.get('/')
async def root():
    return {'message': 'Welcome to Content Aggregator'}

@app.get('/article/')
async def get_all_articles():
    return article_list


@app.get('/article/{article_id}')
async def get_single_article(article_id: int):
    if article_id not in article_list:
        raise HTTPException(status_code=404, detail=f'Article with {article_id=} does not exist.')
    article = article_list.get(article_id)
    return article

@app.delete('/delete-article/{article_id}')
async def delete_article(article_id: int):
    if article_id not in article_list:
        raise HTTPException(status_code=404, detail=f'Article with {article_id=} does not exist.')
    article = article_list.pop(article_id)
    return article


@app.put('/update-article/{article_id}')
async def update_article(article_id: int, id: int | None = None, title: str|None = None, link: str|None = None):
    if article_id not in article_list:
        raise HTTPException(status_code=404, detail=f'Article with {article_id=} does not exist.')
    article = article_list[article_id]
    print(title)
    if id is not None:
        article.id = id

    if title is not None:
        article.title = title

    if link is not None:
        article.link = link

    return {'updated': article}
        