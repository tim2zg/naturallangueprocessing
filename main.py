import npl_first
import runner

input_text = input("Enter text: ")
result = npl_first.make_first_nlp(input_text)

print(result)

print(runner.run(result["Action"]))
