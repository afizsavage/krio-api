from .letters import router as letters_router
# from .words import router as words_router
from .translations import router as translations_router
# from .examples import router as examples_router

all_routers = [
    (letters_router, "/letters", ["letters"]),
    # (words_router, "/words", ["words"]),
    (translations_router, "/translations", ["translations"]),
    # (examples_router, "/examples", ["examples"]),
]
