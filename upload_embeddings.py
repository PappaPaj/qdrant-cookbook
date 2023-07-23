from shared_utils import (
    read_embeddings_from_csv,
    initialize_qdrant_client,
    create_collection,
    insert_embeddings_into_collection,
    get_num_products,
)

def main():
    file_path = 'data/products_with_embeddings.csv'
    vector_size = 1536  # Assuming ADA always outputs in 1536 dimensions

    embeddings_df = read_embeddings_from_csv(file_path)

    client = initialize_qdrant_client()

    collection_name = "Products"

    create_collection(client, collection_name, vector_size)

    insert_embeddings_into_collection(client, collection_name, embeddings_df)

    num_products = get_num_products(client, collection_name)

    print(f"Uploaded {num_products} products into the collection '{collection_name}'")

if __name__ == "__main__":
    main()
