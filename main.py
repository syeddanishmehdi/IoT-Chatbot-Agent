from cumulocity_api import get_current_user
from llm_interface import query_llm

def map_prompt_to_function(prompt):
    prompt = prompt.lower()
    if "alarms" in prompt:
        return get_current_user
    return None

def main():
    print("Cumulocity IoT AI Chatbot (current user version)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        function = map_prompt_to_function(user_input)
        if function:
            result = function()
            print(f"Bot: {result}")
        else:
            result = query_llm(user_input)
            print(f"Bot: {result}")

if __name__ == "__main__":
    main()
