def classify_books(*book, **book_code):
    sorted_fiction = []
    sorted_non_fiction = []
    while book_code:
        for genre, book_name in book:
            if book_name in book_code.values():
                for code, name in list(book_code.items()):
                    if name == book_name:
                        if genre == "fiction":
                            sorted_fiction.append(f"~~~{code}#{book_name}")
                        else:
                            sorted_non_fiction.append(f"***{code}#{book_name}")
                        del book_code[code]
                        break
        if not book_code:
            break

    sorted_fiction.sort(key=lambda x: x.split('#')[0])
    sorted_non_fiction.sort(key=lambda x: x.split('#')[0], reverse=True)
    sorted_books = ""
    if sorted_fiction:
        sorted_books += "Fiction Books:\n" + "\n".join(sorted_fiction)

    if sorted_non_fiction:
        if sorted_fiction:
            sorted_books += "\n"
        sorted_books += "Non-Fiction Books:\n" + "\n".join(sorted_non_fiction)

    return sorted_books

# Test Example 1
import unittest


class TestTaskThree(unittest.TestCase):

    def test_func(self):
        result = classify_books(
            ("fiction", "Brave New World"),
            ("non_fiction", "The Art of War"),
            NF3421NN="The Art of War",
            FF1234UU="Brave New World"
        )

        expected_result = """Fiction Books:
~~~FF1234UU#Brave New World
Non-Fiction Books:
***NF3421NN#The Art of War"""
        self.assertEqual(result.strip(), expected_result)


if __name__ == "__main__":
    unittest.main()










"""
print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))

print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
"""