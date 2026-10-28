from app import create_app

app = create_app()

if __name__ == "__main__":
    # Local development only. Do not expose Flask's debug server to the internet.
    app.run(debug=True)
