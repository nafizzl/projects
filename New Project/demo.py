from configparser import ConfigParser
import google.generativeai as genai

config = ConfigParser()
config.read('credentials.ini')
api_key = config["API_KEY"]["gemini_api_key"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

if __name__ == "__main__":
    print("--"*25 + "\n")
    print("nafizzl: Welcome to nafizzl's AI chatbot, if you have any questions, please type them below\n")
    print("--"*25)
    run = True
    while (run):
        token = input("\nuser: ")
        print("\n" + "--"*25 + "\n")
        if (token != "exit"):
            response = model.generate_content(token)
            print("nafizzl: " + response.text + "\n")
            print("--"*25)
        else:
            run=False
    print("Thank you for using nafizzl's AI chatbot!")