# Function to handle prompt dialogs
def handle_alert_dialog(dialog):
    text_alert = dialog.message
    dialog.dismiss()
    print(f"Alert message: {text_alert}")

# Function to handle prompt dialogs
def handle_prompt_dialog(dialog):
    text_to_insert = "This is a test."
    dialog.accept(text_to_insert)  # Insert the text into the prompt and accept it
    print("Prompt handled with custom text.")
