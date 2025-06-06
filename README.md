# Flask Model Project

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.9 or higher installed
- pip package manager installed

### Steps

1. Clone the repository (if you haven't already):

   ```bash
   git clone <repository-url>
   cd backend-model-flask
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set environment variables if needed (optional):

   Create a `.env` file in the project root and add your environment variables.

6. Run the Flask application:

   ```bash
   python app.py
   ```

   By default, the app will run on `http://127.0.0.1:5000`.

## API Documentation

### POST /api/v1/predict

This endpoint predicts food items based on a list of input ingredients. It returns the top 5 matching food items with similarity scores.

- **URL:** `/api/v1/predict`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Request Body

```json
{
  "ingredients": ["ingredient1", "ingredient2", "ingredient3"]
}
```

- `ingredients`: A list of strings representing the ingredients to use for prediction. This field is required.

#### Success Response (200 OK)

```json
{
  "code": 200,
  "status": "success",
  "data": [
    {
      "food_id": 1,
      "score": 0.95
    },
    {
      "food_id": 5,
      "score": 0.89
    }
  ]
}
```

- `data`: An array of objects containing matched food IDs and their similarity scores.

#### Error Responses

- **400 Bad Request**

  ```json
  {
    "code": 400,
    "status": "error",
    "message": "Please send 'ingredients' in string list format."
  }
  ```

  Returned when the `ingredients` field is missing or not a list of strings.

- **404 Not Found**

  ```json
  {
    "code": 404,
    "status": "not found",
    "message": "No food found that matches the given ingredients.",
    "data": []
  }
  ```

  Returned when no matching food items are found for the given ingredients.

- **500 Internal Server Error**

  ```json
  {
    "code": 500,
    "status": "error",
    "message": "An error occurred on the server: <error details>"
  }
  ```

  Returned when an unexpected server error occurs.

#### Description

The endpoint takes a list of ingredients, vectorizes the input, and calculates cosine similarity against a pre-trained model dataset to find the closest matching food items. It returns the top 5 matches with their similarity scores if they meet a minimum threshold.
  }
