from typing import Optional

from fastapi import FastAPI


app = Optional[FastAPI]


if __name__ == '__main__':
    from poketeam import init_db
    init_db('default.db')

    from poketeam.routes import router
    from poketeam.about import __version__

    app = FastAPI(
        title='Pokemon API',
        version=__version__,
        description='A simple API for creating a team of Pokemon',
        debug=True,
    )

    app.include_router(router)
