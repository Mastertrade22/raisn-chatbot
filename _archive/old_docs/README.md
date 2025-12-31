# LangGraph Chatbot PoC - Model Comparison

A Proof of Concept chatbot using LangGraph to compare Qwen 2.5 and DeepSeek V3 models via OpenRouter API.

## Features

- **LangGraph State Machine**: Implements a complete stateful workflow
- **Model Comparison**: Side-by-side comparison of Qwen 2.5 and DeepSeek V3
- **Intelligent Routing**: Classifies queries as data/general/factual
- **SQL Generation**: Auto-generates SQL from natural language
- **Self-Correction**: Automatically retries failed SQL queries (up to 2 attempts)
- **Chat History**: Maintains conversation context

## Architecture

### State Flow

```
User Question
     ↓
[Router Node] ──→ Classify query type
     ↓
     ├─→ "data" ──→ [SQL Generator] ──→ [Execute SQL] ──→ [Response]
     │                      ↑                  │
     │                      └──── error ───────┘ (Cyclic edge for retry)
     │
     └─→ "general/factual" ──→ [Response]
```

### Graph Nodes

1. **Router Node**: Classifies intent using LLM
2. **SQL Generator Node**: Creates SQL queries from natural language
3. **Execute SQL Node**: Runs queries and handles errors
4. **Response Node**: Synthesizes final natural language answer

### Edges

- **Conditional Edge**: Routes based on query type
- **Cyclic Edge**: Retries SQL generation on errors (max 2 attempts)

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenRouter API key:

```
OPENROUTER_API_KEY=your_api_key_here
```

Get your API key from: https://openrouter.ai/keys

### 3. Run the Application

```bash
python app.py
```

## Real Estate Database

The PoC includes a comprehensive SQLite database with real estate project and unit data. See [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) for full documentation.

### Two Main Tables

**1. projects table** - Project-level information:
- **Core Identity**: project_name, developer_name, city, description
- **Structure & Area**: total_project_area_acres, open_space_percentage, number_of_towers, total_units_count
- **Legal & Dates**: RERA registration, launch dates, possession dates
- **Construction Status**: construction_status, completion_percentage, construction_technology
- **Financials**: stamp_duty_percentage, registration_charges_percentage
- **Amenities & Features**: JSON fields for amenities, payment_plans, unique_selling_propositions
- **Connectivity**: JSON fields for schools, colleges, hospitals, IT parks, shopping malls, metro stations, etc.

**2. project_units table** - Unit-level pricing and details:
- **Classification**: configuration_type (2BHK, 3BHK, 4BHK), property_type (Apartment, Villa, Penthouse)
- **Areas**: built_up_area_sqft, carpet_area_sqft
- **Pricing**: base_price, current_average_psf, market_psf
- **Premiums**: view_premium_details, high_floor_premium_details, corner_unit_premium_details
- **Offers**: current_festive_offers, price revision tracking

### Sample Data

**4 Projects:**
1. **Brigade Eldorado** - Bagalur (8 towers, 1080 units, 35% complete, 3 unit types)
2. **Prestige Lavender Fields** - Whitefield (12 towers, 1520 units, 62% complete, 3 unit types including Penthouse)
3. **Sobha Dream Acres** - Panathur (Villas, 280 units, 89% complete, 2 villa types)
4. **Godrej Woodsville** - Devanahalli (6 towers, 720 units, 18% complete, 2 unit types)

**10 Unit Configurations:**
- Price range: ₹55 lakhs to ₹2.8 crores
- PSF range: ₹4,661 to ₹8,833 per sqft
- Multiple configurations: 2BHK, 3BHK, 4BHK, Villas, Penthouse

## Example Questions

```python
# Project-level queries
"How many projects are under construction?"
"Which projects have more than 75% open space?"
"Show me all projects in Bangalore by Prestige Group"
"List projects near the airport"

# Unit-level queries
"What is the cheapest 2BHK apartment available?"
"Show me all 3BHK units with their prices"
"Which units have festive offers right now?"
"What is the average price per sqft for villas?"

# Combined queries
"List all projects by Prestige Group with their unit types"
"Show me projects near the airport with pricing details"
"Find ready-to-move villas under 2 crores"

# General conversation
"Hello, how are you?"
"Thank you!"

# Factual questions
"What is RERA registration?"
"Explain carpet area vs built-up area"
```

## Model Comparison Output

The app will show:
- Query classification for each model
- SQL generated (if applicable)
- Final natural language response
- Side-by-side comparison summary

## Project Structure

```
raisn_chatbot/
├── app.py                  # Main LangGraph application
├── real_estate_db.py       # Database setup and schema
├── test_db.py              # Database verification script
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment file
├── .env                    # Your API keys (create this)
├── README.md               # This file
├── DATABASE_SCHEMA.md      # Detailed database documentation
├── SYSTEM_PROMPTS.md       # System prompts documentation
└── real_estate_data.db     # SQLite database (auto-created)
```

## Key Components

### AgentState (TypedDict)

The shared memory carrying:
- `question`: User's query
- `chat_history`: Conversation context
- `query_type`: Classification result
- `sql_query`: Generated SQL
- `sql_result`: Query results
- `final_answer`: Final response
- `error`: Error tracking for retries
- `retry_count`: Number of retry attempts
- `model_name`: Current model being used

### OpenRouterLLM Client

Simple wrapper for OpenRouter API calls supporting both models.

### Graph Functions

- `route_query()`: Conditional routing logic
- `check_sql_error()`: Retry logic for failed SQL
- `create_graph()`: Builds the LangGraph workflow
- `compare_models()`: Runs both models and compares results

## Models Used

- **Qwen 2.5 72B Instruct**: `qwen/qwen-2.5-72b-instruct`
- **DeepSeek V3**: `deepseek/deepseek-chat`

## Next Steps

- Add more complex database schemas
- Implement semantic search for embeddings
- Add conversation memory persistence
- Create web interface
- Add more models for comparison
- Implement A/B testing metrics

## License

MIT
