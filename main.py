import npl_first
import processing

input_text = input("Enter text: ")
result = npl_first.make_first_nlp(input_text)

print(result)

print(processing.chat(result["Action"]))