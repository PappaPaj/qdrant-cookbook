from shared_utils import (
    create_embeddings,
    read_products_data
)

def main():
    save_path = 'data/products_with_embeddings.csv'

    # Read the product data from the CSV file
    products_df = read_products_data('data/products.csv')

    # Extract product names and descriptions as lists
    product_names = products_df['Product Name'].tolist()
    product_descriptions = products_df['Description'].tolist()

    # Create embeddings for product names and descriptions
    name_embeddings = create_embeddings(product_names)
    description_embeddings = create_embeddings(product_descriptions)

    # Add the embeddings to the DataFrame
    products_df['name_vector'] = name_embeddings
    products_df['description_vector'] = description_embeddings

    # Save the DataFrame to a new CSV file with embeddings
    products_df.to_csv(save_path, index=False)

    print(f"Created embeddings for {len(products_df)} products and saved to {save_path}")

if __name__ == "__main__":
    main()
