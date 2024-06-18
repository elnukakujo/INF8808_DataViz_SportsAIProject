'''
    Contains the server to run our application.
'''
from flask_failsafe import failsafe
import time

@failsafe
def create_app():
    '''
        Gets the underlying Flask server from our Dash app.

        Returns:
            The server to be run
    '''
    # the import is intentionally inside to work with the server failsafe
    from app import app  # pylint: disable=import-outside-toplevel
    return app.server


if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    server = create_app()
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Time taken to create and run the app: {elapsed_time:.2f} seconds")

    server.run(port="8050", debug=True)
