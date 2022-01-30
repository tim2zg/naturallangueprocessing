import npl_first
import runner
import interpreter


def run_nlp(text):
    result = npl_first.make_first_nlp(text)

    if runner.run(result["Action"]) == "DO":
        interpreter.dooer(runner.run(result["Wo"]), runner.run(result["Was"]), result["Wann"],
                          runner.run(result["Wie"]))


if __name__ == "__main__":
    while True:
        text = input("\n> ")
        run_nlp(text)