
# Chef AI - Ingrid

Chef AI, also called "Ingrid," (the name “Ingrid” is inspired by the word “Ingredient” but in short) is a desktop application that acts as your personal chef assistant. With Ingrid's expertise, you can receive personalized dish suggestions and step-by-step cooking instructions based on the ingredients you have, your preferred dish type, cuisine, quality, and the maximum cooking time. Whether you're looking for a quick family meal or a gourmet experience, Ingrid has you covered!

## Features

- **Interactive GUI**: Simple and user-friendly interface created using Python's `Tkinter` library.
- **Customizable Meal Suggestions**: Receive dish suggestions based on ingredients, dish type, cuisine, quality, and cooking time.
- **Creative Dish Options**: Instead of providing only the existent dishes, Ingrid can create a new dish or alter to suit users’s preference.
- **Step-by-Step Instructions**: Get detailed instructions on how to prepare your chosen dish, and cooking time for each step.
- **Ingredient Alternatives**: If the given information can not be a good combination, Ingrid will suggest alternatives, or be creative if user provides insufficient details.

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
     python main.py
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
├── main.py         # Main script to run Chef AI
├── README.md          # Project documentation
```

## Future Upgrades

- **Advanced Error Handling**: Improve response feedback for unusual or incompatible ingredient combinations.
- **Interactive Chatbot**: Easily change the step and ask AI for more detail.
- **Multi-platform**: Can be developed to be suitable and run smoothly on various type of devices, allowing users to use in various situations.

Happy cooking with Ingrid, your personal Chef AI! 👩‍🍳
