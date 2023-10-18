from database import create_database_connection, fetch_first_recipe
from sqlalchemy import create_engine, text

def count_total_recipes(engine):
    with engine.connect() as connection:
        sql = text("SELECT COUNT(*) FROM csv_imported_data")
        result = connection.execute(sql)
        total_recipes = result.scalar()
    return total_recipes    


if __name__ == "__main__":
    engine = create_database_connection()
    total_recipes = count_total_recipes(engine)
    print(f"Total number of recipes: {total_recipes}")





# if __name__ == "__main__":
#     engine = create_database_connection()

#     # Fetch the first recipe
#     first_recipe = fetch_first_recipe(engine)

#     if first_recipe:
#         # Print the details of the first recipe
#         print("First Recipe Details:")
#         print(f"Title: {first_recipe['Title']}")
#         print(f"Ingredients: {first_recipe['Ingredients']}")
#         print(f"Instructions: {first_recipe['Instructions']}")
#         print(f"Image Name: {first_recipe['Image_Name']}")
#         print(f"Cleaned Ingredients: {first_recipe['Cleaned_Ingredients']}")
#     else:
#         print("No recipes found in the database.")
