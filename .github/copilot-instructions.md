# Copilot Instructions for blank-homeworkJHS

## Project Overview
This is a **Streamlit application** template for building interactive Python web apps. The project is minimal and intentionally designed as a starter template for custom development.

## Tech Stack
- **Framework**: Streamlit (Python web framework for data apps)
- **Python**: 3.7+ required
- **Single dependency**: `streamlit` package (see [requirements.txt](requirements.txt))

## Project Structure
```
.
├── streamlit_app.py      # Main application file - entry point
├── requirements.txt      # Python dependencies (minimal)
├── README.md            # Project documentation
└── .github/
    └── CODEOWNERS      # Repository code ownership
```

## Key Workflows

### Running the Application
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
The app will be available at `http://localhost:8501` by default.

### Development Patterns
- **Single-file structure**: All UI logic lives in [streamlit_app.py](streamlit_app.py)
- **Streamlit API usage**: Use `st.title()`, `st.write()`, `st.button()`, etc. directly without custom wrappers
- **No state management**: Streamlit reruns the entire script on user interaction; use `st.session_state` for persistent data across reruns

## Guidelines for AI Agents
1. **Keep it simple**: This is a template - favor clarity and simplicity over complex abstractions
2. **Minimize dependencies**: Only add new packages to `requirements.txt` if essential; prefer Streamlit's built-in features
3. **Incremental growth**: Extend [streamlit_app.py](streamlit_app.py) functionally first; refactor into modules only when file complexity exceeds 300+ lines
4. **Testing limitations**: Streamlit apps are difficult to unit test; focus on code organization and documentation over test coverage
5. **Deployment ready**: The repo structure supports Streamlit Cloud deployment out-of-the-box - avoid breaking this compatibility

## Common Streamlit Gotchas
- **Reruns**: Every user interaction reruns the entire script from top to bottom
- **Imports**: Place imports at the top; they'll be cached by Streamlit
- **Performance**: Use `@st.cache_data` for expensive computations
- **Secrets**: Store sensitive data in `.streamlit/secrets.toml` (excluded from git), not in code

## References
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference)
