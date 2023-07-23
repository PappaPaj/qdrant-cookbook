# Qdrant Cookbook

This repository contains a set of scripts and utilities for working with Qdrant, OpenAI, and embeddings. The scripts allow you to create embeddings for product data, upload the embeddings to a Qdrant collection, and perform search queries on the embeddings.

## Installation

To use the scripts in this repository, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/PappaPaj/qdrant-cookbook.git
   ```

2. Install the required Python packages by running the following command in the project directory:

   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables by creating a `.env` file in the project directory and adding the following lines:

   ```
   OPENAI_API_KEY=<your-openai-api-key>
   QDRANT_URL=<your-qdrant-url>
   QDRANT_API_KEY=<your-qdrant-api-key>
   ```

   Replace `<your-openai-api-key>`, `<your-qdrant-url>`, and `<your-qdrant-api-key>` with your respective API keys and URLs.

## Usage

### `make_embeddings.py`

This script creates embeddings for product names and descriptions using the OpenAI API.

**Usage:**

```
python make_embeddings.py
```

This script reads product data from the `data/products.csv` file, creates embeddings for each product name and description using the OpenAI API, and saves the embeddings into a new CSV file (`data/products_with_embeddings.csv`). The embeddings are added as new columns (`name_vector` and `description_vector`) in the CSV file.

### `upload_embeddings.py`

This script uploads the embeddings from the `data/products_with_embeddings.csv` file to a Qdrant collection.

**Usage:**

```
python upload_embeddings.py
```

This script reads the embeddings data from the `data/products_with_embeddings.csv` file, initializes the Qdrant client, creates a collection in Qdrant with the specified vector configuration, and inserts the embeddings data into the collection.

### `search_embeddings.py`

This script allows you to perform search queries on the Qdrant collection using user input.

**Usage:**

```
python search_embeddings.py
```

This script prompts the user to enter a query string and performs a search query on the Qdrant collection. It retrieves the top results based on the query and prints them to the console.

### `metadata_filtered_search.py`

This script demonstrates how to perform similarity search with metadata filtering on the Qdrant collection.

**Usage:**

```
python metadata_filtered_search.py
```

This script performs similarity search on the Qdrant collection for a set of queries. It applies a filter condition to further filter the results based on specific brands. The script prints the matched persona, metadata, and score for each query.

## Data

The `data` folder contains the following files:

- `products.csv`: CSV file containing the product data.
- `products_with_embeddings.csv`: CSV file containing the product data with embeddings.

Feel free to replace the `products.csv` file with your own data file in the same format.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
