from neo4j import GraphDatabase

# Neo4j Database Configuration
NEO4J_URI = "bolt://localhost:7687"  
NEO4J_USERNAME = "neo4j"  
NEO4J_PASSWORD = "Neoj1234"  

# Initialize the Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Function to store user preferences
def store_user_preference(user_id, preference_type, preference_value):
    with driver.session() as session:
        session.write_transaction(_create_preference, user_id, preference_type, preference_value)

# Function to create a preference in the database
def _create_preference(tx, user_id, preference_type, preference_value):
    query = """
    MERGE (u:User {id: $user_id})
    MERGE (p:Preference {type: $preference_type, value: $preference_value})
    MERGE (u)-[:PREFERS]->(p)
    """
    tx.run(query, user_id=user_id, preference_type=preference_type, preference_value=preference_value)

# Function to retrieve user preferences
def get_user_preferences(user_id):
    with driver.session() as session:
        result = session.read_transaction(_fetch_preferences, user_id)
        return result

# Function to fetch preferences from the database
def _fetch_preferences(tx, user_id):
    query = """
    MATCH (u:User {id: $user_id})-[:PREFERS]->(p:Preference)
    RETURN p.type AS type, p.value AS value
    """
    result = tx.run(query, user_id=user_id)
    preferences = [{"type": record["type"], "value": record["value"]} for record in result]
    return preferences

# Example usage
if __name__ == "__main__":
    # Sample user ID
    user_id = "user123"

    # Storing preferences
    preferences_to_store = [
        {"type": "Activity", "value": "Historical Sites"},
        {"type": "Food", "value": "Italian Cuisine"},
        {"type": "Budget", "value": "Moderate"}
    ]

    for pref in preferences_to_store:
        store_user_preference(user_id, pref["type"], pref["value"])

    print("User preferences have been stored successfully!")

    # Retrieving preferences for the next chat
    user_preferences = get_user_preferences(user_id)
    print("Retrieved user preferences for the next chat:")
    for pref in user_preferences:
        print(f"{pref['type']}: {pref['value']}")

# Close the Neo4j driver
driver.close()
