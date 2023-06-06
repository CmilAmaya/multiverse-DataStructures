from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Tuple
from fastapi.middleware.cors import CORSMiddleware
import graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def mostrar_diccionario(request: Request):
    ##diccionario = graph.G1.graph_dict
    diccionario = graph.final_names
    return templates.TemplateResponse("grafo.html", {"request": request, "grafo": diccionario})

class Graph(BaseModel):
    nodes: List[int]
    edges: List[Tuple[int, int]]

@app.post("/graph/")
async def create_graph(graph: Graph):
    # You can add any additional processing of the graph here
    return graph
