from App import create_app

# Initialise the app
app = create_app()

if __name__ == "__main__":
	# Runs the app in debug mode
	app.run(debug=True) 