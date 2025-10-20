import os
import threading
from openai import OpenAI

def timed_input(prompt, timeout=30):
    """Get user input with a timeout."""
    result = [None]
    
    def get_input():
        try:
            result[0] = input(prompt)
        except:
            pass
    
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(timeout)
    
    if input_thread.is_alive():
        print("\n\nNo input received in the last 30 seconds. Exiting the program.")
        return None
    
    return result[0]

def main():
    # Get API key from Windows environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found.")
        print("Please set your OpenAI API key in Windows environment variables.")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Inform user about one-sentence response limit
    print("=" * 60)
    print("Note: For simplicity, all responses are limited to one sentence.")
    print("=" * 60)
    print()
    
    # Hardcoded message
    message = "Hello! Can you explain what you are in one sentence?"
    
    print(f"Sending request to OpenAI API...")
    print(f"Message: {message}\n")
    
    try:
        # Send request to OpenAI API using gpt-3.5-turbo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You must respond in exactly one sentence. Keep your answer concise and complete."},
                {"role": "user", "content": message}
            ]
        )
        
        # Extract and print the response
        assistant_message = response.choices[0].message.content
        print(f"Response from OpenAI:")
        print(f"{assistant_message}\n")
        
        # Now allow user to ask up to 5 questions
        max_questions = 5
        print("-" * 50)
        print(f"\nYou can now ask up to {max_questions} questions.")
        print("(Note: You have 30 seconds to type each question)\n")
        
        for question_num in range(1, max_questions + 1):
            print(f"Question {question_num}/{max_questions}:")
            user_message = timed_input("Enter your message: ", timeout=30)
            
            # Check if timeout occurred
            if user_message is None:
                break
            
            # Check if user entered something
            if not user_message.strip():
                print("No message entered. Exiting.")
                break
            
            print(f"\nSending your request to OpenAI API...")
            print(f"Message: {user_message}\n")
            
            # Send user's message to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You must respond in exactly one sentence. Keep your answer concise and complete."},
                    {"role": "user", "content": user_message}
                ]
            )
            
            # Extract and print the response
            user_response = response.choices[0].message.content
            print(f"Response from OpenAI:")
            print(f"{user_response}\n")
            
            # Check if this was the last question
            if question_num < max_questions:
                print("-" * 50)
        
        # If user completed all questions
        if question_num == max_questions and user_message is not None and user_message.strip():
            print("\nYou've reached the maximum of 5 questions. Exiting the program.")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()





