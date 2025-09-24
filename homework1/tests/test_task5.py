import task5

def test_books_slice():
    assert len(task5.first_three_books()) == 3
    assert task5.books[0][0] == "The Hobbit"

def test_students_dict():
    assert task5.students["Alice"] == 1001