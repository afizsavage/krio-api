from .letters import router as letters_router
# from .words import router as words_router
# from .definitions import router as definitions_router
# from .examples import router as examples_router

all_routers = [
    (letters_router, "/letters", ["letters"]),
    # (words_router, "/words", ["words"]),
    # (definitions_router, "/definitions", ["definitions"]),
    # (examples_router, "/examples", ["examples"]),
]
