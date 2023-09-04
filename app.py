#!/usr/bin/python3
""" main file with all the routes """
import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
