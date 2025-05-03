from setuptools import find_packages,setup

setup(name="agentic-trading-system",
      version="0.0.1",
      author="Vijay Kukreja",
      author_email="vj_1900@yahoo.com",
      packages=find_packages(),
      install_requires=[
          "langchain",
          "lancedb",
          "langgraph",
          "tavily-python",
          "polygon"
      ])
