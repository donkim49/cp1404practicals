"""
CP1404/CP5632 Practical
Wikipedia API program - search for pages and display title, summary and URL.
"""
import wikipedia


def main():
    """Prompt user for Wikipedia page titles in a loop until blank input."""
    page_title = input("Enter page title: ")
    while page_title:
        display_page(page_title)
        page_title = input("\nEnter page title: ")
    print("Thank you.")


def display_page(title):
    """Fetch and display the title, summary and URL of a Wikipedia page.

    title: string, the page title or search phrase to look up
    """
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')


main()