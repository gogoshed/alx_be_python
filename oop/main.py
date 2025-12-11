from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)

    print(repr(my_book))

    del my_book

if __name__ == "__main__":
    main()



from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()





    from class_static_methods_demo import Calculator

def main():
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()