from colorama import init, Fore
init()


def show_report(counts, percents) -> str:

    if not counts:
        return ("There are no comments for analysis on this video.")

    for label in counts:
        if label == "negative":
            print(f"{Fore.RED} + {counts[label]} comments ({percents[label+'_percent']})")
        elif label == "positive":
            print(f"{Fore.GREEN} + {counts[label]} comments ({percents[label+'_percent']})")
        elif label == "neutral":
            print(f"{Fore.YELLOW} + {counts[label]} comments ({percents[label+'_percent']}) ")
