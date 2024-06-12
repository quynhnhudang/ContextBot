Summary:
1. Backend Server: Handles chat requests, manages context, and generates responses using NLP models.
2. Rasa Dialogue Management: Manages conversation flows, intents, and entities.
3. Frontend Interface: Provides a user-friendly interface for interacting with the chatbot.

Components:

    1. Backend Server

        Technology: Flask, GPT-2 (via Hugging Face Transformers)

        Responsibilities:
            - Handle incoming chat requests.
            - Maintain conversation context.
            - Generate responses using GPT-2.

        Modules:
            - `server.py`: Main server script handling HTTP requests and response generation.
            - `user_profile.py`: Manages user profiles, preferences, and conversation history.
            - `knowledge_base.py`: Connects to the SQLite database to retrieve FAQ answers.
            - `setup_database.py`: Script to set up the SQLite database with sample data.

        Data Flow:
            1. Receives user input from the frontend.
            2. Updates and maintains conversation context.
            3. Uses GPT-2 to generate a response based on the context.
            4. Interacts with Rasa for dialogue management and additional information retrieval.
            5. Sends the response back to the frontend.

    2. Rasa Dialogue Management

        Technology: Rasa

        Responsibilities:
            - Manage conversation states and flows.
            - Handle intents and entities.
            - Integrate with the backend server for generating responses.

        Files:
            - `domain.yml`: Defines intents, entities, slots, responses, and actions.
            - `stories.yml`: Specifies conversation flows and how the chatbot should respond to different inputs.
            - `config.yml`: Configuration file for Rasa settings.
            - `credentials.yml`: Contains credentials for connecting to various messaging channels.
            - `requirements.txt`: Lists Rasa dependencies.

        Data Flow:
            1. Receives context and user input from the backend.
            2. Manages dialogue state and flow.
            3. Updates slots and entities based on user input.
            4. Returns updated state and responses to the backend.

    3. Frontend Interface

        Technology: React

        Responsibilities**:
            - Provide a chat interface for users.
            - Send user messages to the backend server.
            - Display chatbot responses and maintain chat history.

        Files:
            - `public/index.html`: Main HTML file for the React application.
            - `src/App.js`: Main React component handling user input and chatbot interaction.
            - `src/index.js`: Entry point for the React application.
            - `src/App.css`: CSS file for styling the React application.
            - `src/setupProxy.js`: Proxy setup for API requests to the backend.

        Data Flow:
            1. User types a message in the chat interface.
            2. Sends the message to the backend server via an API call.
            3. Receives the chatbot's response from the backend.
            4. Displays the response in the chat interface.
