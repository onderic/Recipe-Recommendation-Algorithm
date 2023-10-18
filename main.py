from fastapi import FastAPI
from database import create_database_connection, fetch_all_recipes
from recommendations import recommend_recipes


app = FastAPI()

# Create a database connection
@app.on_event("startup")
async def startup_event():
    app.engine = await create_database_connection()
    app.recipes = await fetch_all_recipes(app.engine)


@app.get("/")
def root_app():
    return {"Hello": "world"}


@app.get("/recommend/{recipe_id}")
async def get_recommendations(recipe_id: int):
    recommended_ids = recommend_recipes(recipe_id, app.recipes)
    if not recommended_ids:
        return {"message": "Recipe not found or no recommendations available."}
    
    recommended_titles = [
        recipe['Title']
          for recipe in app.recipes if recipe['recipe_id'] in recommended_ids]

    return {"recommendations": recommended_titles}


