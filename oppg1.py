import datetime

alder = ""
while alder not in list(range(1900, int(datetime.date.today().year - 3))):
    # Listen med år det er menneskelig mulig å være født i, og samtidig bruke programmet, fikk jeg hjelp til av
    # ChatGTP. Jeg ba først om en liste men fikk en "list comprehension" til svar. Denne har jeg så endret ved å
    # bruke date modulen.
    try:
        alder = int(input(
            'Hvilket år er du født? \nOg ikke kødd med alderen, kødde tall fører til at du får se spørsmål og melding '
            'igjen.\n'))
    except:
        ValueError("Prøv igjen, bruk kun tall")

print(
    f'Da vil du herrens år {datetime.date.today().year} bli, om ikke du har fylt år i år, {int(datetime.date.today().year) - alder} år gammel. Inshallah!')
