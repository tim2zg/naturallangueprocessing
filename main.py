import npl_first
import runner
import interpreter

input_text = input("Enter text: ")
result = npl_first.make_first_nlp(input_text)

if runner.run(result["Action"]) == "DO":
    interpreter.dooer(runner.run(result["Wo"]), runner.run(result["Was"]), result["Wann"], runner.run(result["Wie"]))

