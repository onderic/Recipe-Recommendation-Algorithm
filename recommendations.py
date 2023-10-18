import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Function to recommend recipes based on cosine similarity
def recommend_recipes(recipe_id, recipes):
    data = [[recipe['recipe_id'], recipe['Ingredients']] for recipe in recipes]
    
    data = pd.DataFrame(data,  columns=['recipe_id', 'Ingredients'])
    data['Ingredients'] = data['Ingredients'].fillna('')
    data["Ingredients"] = data["Ingredients"].str.lower()
    data["recipe_text"] = data["recipe_id"].astype(str) + " " + data["Ingredients"]

    # Remove any rows with NaN values in the "recipe_text" column
    data = data.dropna(subset=['recipe_text'])

    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(data["recipe_text"])

    # Calculate the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)

    # Get recipe IDs
    recipe_ids = data['recipe_id'].tolist()

    if recipe_id not in recipe_ids:
        print(f"Recipe ID '{recipe_id}' does not exist.")
        return []
    
    recipe_idx = recipe_ids.index(recipe_id)
    
    # Get the pairwise similarity scores
    similar_recipes = list(enumerate(cosine_sim[recipe_idx]))
    
    # Sort recipes by similarity score
    similar_recipes = sorted(similar_recipes, key=lambda x: x[1], reverse=True)

    # Get the top recommendations (excluding the input recipe)
    top_recipes = similar_recipes[1:11]

    # Retrieve the IDs of recommended recipes
    recommended_ids = [recipe_ids[i[0]] for i in top_recipes]

    return recommended_ids

    