import openai


class ChatBot:
    def __init__(self):
        openai.api_key = "https%3A%2F%2Fchat.openai.com"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("write a joke")
    print(response)
