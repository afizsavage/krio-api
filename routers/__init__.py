from .letters import router as letters_router
from .words import router as words_router
from .search import router as search_router
from .examples import router as examples_router

all_routers = [
    (letters_router, "/letters", ["letters"]),
    (words_router, "/words", ["words"]),
    (search_router, "/search", ["search"]),
    (examples_router, "/examples", ["examples"]),
]
