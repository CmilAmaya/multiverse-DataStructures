from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Tuple
from fastapi.middleware.cors import CORSMiddleware
from graph import DirectedGraph, build_graph

class Graph(BaseModel):
    nodes: List[int]
    edges: List[Tuple[int, int]]

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000/graph/",
    "http://127.0.0.1:8000",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Graph(BaseModel):
    nodes: List[int]
    edges: List[Tuple[int, int]]

@app.post("/graph/")
async def create_graph():
    # You can add any additional processing of the graph here
    G1, nodes = build_graph(DirectedGraph)
    print(nodes)
    final_names = []
    for elemento in nodes:
        if elemento not in final_names:
            final_names.append(elemento)
    g = G1.graph_dict
    edges = []

    for key, value in g.items():
        key.get_name()
        if len(value)>0:
            edges.append((key.get_name(), value[0].get_name()))
        else:
            edges.append((key.get_name(), None))

    print(edges)
    return {"nodes":final_names, "edges":edges}

