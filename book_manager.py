def add_book(books):

    print("\n-Add a book-")

    while True:
        title = input("Enter book title: ")
        if not title:
            print("Can't be blank.")
            continue
        author = input("Enter author: ")
        if not author:
            print("Can't be blank.")
            continue
        genre = input("Enter genre: ")
        if not genre:
            print("Can't be blank.")
            continue
        try:
            year = int(input("Enter book year: "))
        except ValueError:
            print("Year must be a number.")
            continue
        try:
            rating = float(input("Enter book rating (0-5): "))
        except ValueError:
            print("Rating must be a number, e.g. 4 or 4.5.")
            continue
        
        book = {
            'title': title.strip(),
            'author': author.strip(),
            'genre': genre.strip(),
            'year': year,
            'rating': rating
        }
        books.append(book)
        print(f"Added '{title}' by {author}.")
        break


def remove_book(books):

    print("\n-Remove Book-")

    while True:
        title = input("Enter title of book to remove: ")
        if not title:
            print("Can't be blank.")
            continue

        for book in books:
            if book['title'].lower() == title.lower():
                books.remove(book)
                print(f"Removed '{book['title']}'.")
                return  # done after one removal

        print("No book found with that title. Try again or type 'done' to cancel.")
        if title.lower() == "done":
            return


def view_stats(books):

    print("\n-Book Stats-")

    if not books:
        print("No books in your list yet.")
        return

    print(f"Total books: {len(books)}")

    # Average rating
    avg_rating = sum(book['rating'] for book in books) / len(books)
    print(f"Average rating: {avg_rating:.2f}")

    # Books per genre
    genres = {}
    for book in books:
        genre = book['genre']
        genres[genre] = genres.get(genre, 0) + 1
    print("Books by genre:")
    for genre, count in genres.items():
        print(f"  {genre}: {count}")

    # Newest and oldest books
    newest = max(books, key=lambda b: b['year'])
    oldest = min(books, key=lambda b: b['year'])
    print(f"Newest book: {newest['title']} ({newest['year']})")
    print(f"Oldest book: {oldest['title']} ({oldest['year']})")


def main():

    books = []

    print("-Welcome To Your Book Manager-")

    while True:
        
        menu = input("\nTo add a book, type 'add'. To remove, 'remove'. For stats, 'stats.' Type 'done' to quit: ")

        if not menu:
            print("You must select and option, or type 'done' to quit. ")
            continue

        if menu.lower() == 'add':
            add_book(books)
        elif menu.lower() == 'remove':
            remove_book(books)
        elif menu.lower() == 'stats':
            view_stats(books)
        elif menu.lower() == 'done':
            print("\nGoodbye!")
            break
        else:
            print("\nThat's not a valid option. Try again.")
            continue


if __name__ == "__main__":
    main()