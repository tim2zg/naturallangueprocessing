import npl_first
import runner
import interpreter

input_text = input("Enter text: ")
result = npl_first.make_first_nlp(input_text)

print(result)

print(runner.run(result["Action"]))

if runner.run(result["Action"]) == "DO":
    interpreter.dooer(runner.run(result["Wo"]), runner.run(result["Was"]), result["Wann"], runner.run(result["Wie"]))

print(runner.run(result["Wo"]))
print(runner.run(result["Was"]))
print(runner.run(result["Wie"]))