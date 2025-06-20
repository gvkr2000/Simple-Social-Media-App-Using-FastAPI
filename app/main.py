from fastapi import FastAPI
from . import models
from .database import  engine
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
   
@app.get("/")
def root():
    return {"message": "Hello World..."}





    

















# import time
# from typing import Optional
# from fastapi import FastAPI, HTTPException, Response , status , Depends
# from fastapi.params import Body
# import psycopg
# from pydantic import BaseModel
# from psycopg.rows import dict_row
# from . import models,schemas
# from .database import  engine , get_db
# from sqlalchemy.orm import Session

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()



# while True:

#     try:
       
#         conn = psycopg.connect( host="localhost",port=5432,dbname="Fast_API",user="postgres", password="Vamshi@123456")

#         cursor=conn.cursor()
#         print("Database connection was  succesfull :-)")
#         break
#     except Exception as error:
#         print("Connecting to database failed!!!")
#         print("error was",error)
#         time.sleep(60)
   
# @app.get("/")
# def root():
#     return {"message": "Hello World..."}


# @app.get("/posts")
# def get_posts(db:Session =Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts=cursor.fetchall()
#     posts = db.query(models.Post).all()
#     return  posts

# @app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate,db:Session =Depends(get_db)):
#     # we are using this kind of prepared statement to prevent sql inj attack
#     # cursor.execute("INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING *",(post.title,post.content,post.published))
#     # fetching only one so we are using this and saving to new_post
#     # new_post=cursor.fetchone()
#     # saving changes to Database
#     # conn.commit()
#     # we use ** to pack and unpack dictionary
#     new_post= models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get("/posts/{id}",)
# def get_post(id: int,db:Session =Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts WHERE id=%s """,(id,))
#     # # the comma after the id is to indicate that it is a tuple
#     # post = cursor.fetchone()
#     post = db.query(models.Post).filter(models.Post.id== id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return{"message":f"post with id :{id} is not found"}
#     return post

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int,db:Session =Depends(get_db)):
#     # index = find_delete_post(id)
#     # cursor.execute(
#     #     """DELETE FROM posts WHERE id = %s RETURNING *""",(id,))
#     # deleted_post=cursor.fetchone()
#     # conn.commit()
#     del_post = db.query(models.Post).filter(models.Post.id== id).first()

#     if del_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id:{id} is not found")
    
#     db.delete(del_post)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, updated_post : schemas.PostCreate,db:Session =Depends(get_db)):

#     # cursor.execute("""UPDATE posts SET title = %s,content=%s,published=%s WHERE id = %s RETURNING *""",
#     #             (post.title,post.content,post.published,(id),))
#     # updated_post=cursor.fetchone()
#     # conn.commit()
#     post_query=db.query(models.Post).filter(models.Post.id==id)
#     post=post_query.first()

#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id:{id} is not found")
    
#     post_query.update(updated_post.dict(),synchronize_session=False)

#     db.commit()
    
#     return post_query.first()
    


