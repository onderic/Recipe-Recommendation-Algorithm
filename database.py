from sqlalchemy import create_engine
import asyncpg

async def create_database_connection():
    db_params = {
        "database": "myrecipes",
        "user": "onderi",
        "password": "0909",
        "host": "localhost",
        "port": "5432"
    }

    db_url = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
    engine = create_engine(db_url)
    return engine

# def count_total_recipes(engine):
#     with engine.connect() as connection:
#         # Use SQLAlchemy's text() function to create an SQL expression
#         sql = text("SELECT COUNT(*) FROM csv_imported_data")
#         result = connection.execute(sql)
#         total_recipes = result.scalar()  # Retrieve the count from the query result
#     return total_recipes


# Function to fetch all recipe data from the database
async def fetch_all_recipes(engine):
    async with asyncpg.create_pool(
        user="onderi",
        password="0909",
        database="myrecipes",
        host="localhost",
        port="5432"
    ) as pool:
        async with pool.acquire() as conn:
            result = await conn.fetch("SELECT * FROM csv_imported_data")
    return result


# if __name__ == "__main__":
#     engine = create_database_connection()
#     total_recipes = count_total_recipes(engine)
#     print(f"Total number of recipes: {total_recipes}")


