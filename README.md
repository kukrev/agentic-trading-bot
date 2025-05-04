### keys needs to be mention inside the .env
```
POLYGON_API_KEY
GOOGLE_API_KEY
TAVILY_API_KEY
GROQ_API_KEY
PINECONE_API_KEY
```

### for running the fastapi endpoint
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```

### for running the streamlit ui
```
streamlit run streamlit_ui.py

```

### for installing the requirements
```
pip install -r requirements.txt
```

### for creating the env
```
conda create -p env python=3.10 -y
```

### for activate the env through cmd
```
conda activate <env_path>
```

### for activate the env through git-bash
```
source activate ./env
```