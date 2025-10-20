import os
from openai import OpenAI

def main():
    # Get API key from Windows environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found.")
        print("Please set your OpenAI API key in Windows environment variables.")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Hardcoded message
    message = "Hello! Can you explain what you are in one sentence?"
    
    print(f"Sending request to OpenAI API...")
    print(f"Message: {message}\n")
    
    try:
        # Send request to OpenAI API using gpt-3.5-turbo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        # Extract and print the response
        assistant_message = response.choices[0].message.content
        print(f"Response from OpenAI:")
        print(f"{assistant_message}\n")
        
        # Now prompt user for their own message
        print("-" * 50)
        user_message = input("\nNow enter your own message: ")
        
        if user_message.strip():
            print(f"\nSending your request to OpenAI API...")
            print(f"Message: {user_message}\n")
            
            # Send user's message to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )
            
            # Extract and print the response
            user_response = response.choices[0].message.content
            print(f"Response from OpenAI:")
            print(f"{user_response}")
        else:
            print("No message entered. Exiting.")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()





