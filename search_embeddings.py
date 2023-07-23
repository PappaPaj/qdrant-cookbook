from shared_utils import query_qdrant

def main():
    while True:
        user_query = input("Enter your query (type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        collection_name = 'Products'  # Modify this according to your collection name
        query_results = query_qdrant(user_query, collection_name)

        print("\nSearch Results:")
        for i, article in enumerate(query_results):
            product_name = article.payload.get("name", "Unknown Product")
            product_description = article.payload.get("content", "Unknown Description")
            product_id = article.id
            score = round(article.score, 3)
            print(f'{i + 1}. {product_name} (ID: {product_id}) (Score: {score}) - {product_description}')
        
        print()

if __name__ == "__main__":
    main()
