from sqlalchemy import create_engine, text

def create_database_connection():
    db_params = {
        "database": "myrecipes",
        "user": "onderi",
        "password": "0909",
        "host": "localhost",
        "port": "5432"
    }

    # Create a connection to the PostgreSQL database using SQLAlchemy
    db_url = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
    engine = create_engine(db_url)

    return engine

def count_total_recipes(engine):
    with engine.connect() as connection:
        # Use SQLAlchemy's text() function to create an SQL expression
        sql = text("SELECT COUNT(*) FROM csv_imported_data")
        result = connection.execute(sql)
        total_recipes = result.scalar()  # Retrieve the count from the query result
    return total_recipes

def fetch_first_recipe(engine):
    with engine.connect() as connection:
        # Use SQLAlchemy's text() function to create an SQL expression
        sql = text("SELECT * FROM csv_imported_data LIMIT 1")
        result = connection.execute(sql)
        first_recipe = result.fetchone()

    # Convert the tuple result to a dictionary
    first_recipe_dict = dict(zip(result.keys(), first_recipe))
    return first_recipe_dict


if __name__ == "__main__":
    engine = create_database_connection()
    total_recipes = count_total_recipes(engine)
    print(f"Total number of recipes: {total_recipes}")



