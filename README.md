
# Chef AI - Ingrid

Chef AI, also called "Ingrid," is a desktop application that acts as your personal chef assistant. With Ingrid's expertise, you can receive personalized dish suggestions and step-by-step cooking instructions based on the ingredients you have, your preferred dish type, cuisine, quality, and the maximum cooking time. Whether you're looking for a quick family meal or a gourmet experience, Ingrid has you covered!

## Features

- **Interactive GUI**: Simple and user-friendly interface created using Python's `Tkinter` library.
- **Customizable Meal Suggestions**: Receive dish suggestions based on ingredients, dish type, cuisine, quality, and cooking time.
- **Creative Dish Options**: Ingrid can still suggest a recipe even with limited or unusual ingredient combinations.
- **Step-by-Step Instructions**: Get detailed instructions on how to prepare your chosen dish.
- **Multiple Dish Quality Options**: Choose from restaurant-quality, family-style, or easy, healthy options.

## Installation

1. **Python**: Ensure Python is installed on your machine. You can download it [here](https://www.python.org/downloads/).
2. **Install Dependencies**: Run the following command to install required packages:
   ```bash
   pip install tkinter groq
   ```
3. **API Key**: Add your API key in the `Groq` client setup:
   ```python
   client = Groq(api_key="your_groq_api_key")
   ```

## Usage

1. **Start the Application**:
   - Run the script using:
     ```bash
     python chef_ai.py
     ```
   - The GUI window will open, displaying fields for your input.

2. **Enter Information**:
   - Fill out the fields with your ingredients, dish type, cuisine type, quality, and maximum cooking time.
   - Click **"Cook it, Ingrid!"** to receive your custom recipe suggestion.

3. **View Ingrid's Response**:
   - After submission, Ingrid will display a suggested recipe, including ingredients, instructions, and the cooking time.
   - To go back to the input scene, click **"Back"**.

## Code Structure

- **GUI Setup**: `Tkinter` manages the layout, colors, and buttons in the `show_input_scene` function.
- **Groq API Integration**: `Groq` API fetches dish suggestions based on user inputs.
- **Logic**: Functions capture inputs, create prompts for Ingrid, and handle responses, which are displayed in the GUI.

## Project Structure

```plaintext
├── chef_ai.py         # Main script to run Chef AI
├── README.md          # Project documentation
```

## Future Enhancements

- **Advanced Error Handling**: Improve response feedback for unusual or incompatible ingredient combinations.
- **Additional Cuisine & Dish Options**: Broaden recipe categories and regional cuisines.
- **Interactive Skill Level Selection**: Allow users to choose their cooking skill level for tailored recipes.

## License

This project is licensed under the MIT License.

Happy cooking with Ingrid, your personal Chef AI! 👩‍🍳
