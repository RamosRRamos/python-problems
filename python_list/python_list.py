# URL:
# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

# LIST #

class ListManipulator:
    """
    A class that manipulates a list of integers using different operations.

    Methods:
    --------
    __init__():
        Constructor that initializes an empty data list.
    insert(args: list) -> None:
        Inserts an integer into the list at a given index.
    print_f() -> None:
        Prints the current state of the data list.
    remove(args: list) -> None:
        Removes the first occurrence of an integer from the data list.
    append(args: list) -> None:
        Appends an integer to the end of the data list.
    sort() -> None:
        Sorts the data list in ascending order.
    pop() -> None:
        Removes and returns the last element from the data list.
    reverse() -> None:
        Reverses the data list in place.
    selector(selector: str, args: list) -> None:
        Returns the method corresponding to the selector string and calls
        it with the supplied list of arguments.
    get_list(input_: str) -> dict:
        Parses an input string and returns a dictionary with the operation
        selector and arguments.
    manipulate_list() -> None:
        Main program logic that reads inputs, parses them, and executes
        the corresponding operation on the data list.
    """

    def __init__(self):
        self.data_list = []

    def insert(self, args: list) -> None:
        """
        This is a Python method called insert which belongs to a class
        and takes a list args as an argument. The purpose of
        this method is to insert an element args[1] into a list
        self.data_list at the specified index args[0].
        This method does not return any value as it has a None return
        type annotation.
        :param args:
        :return:
        """
        self.data_list.insert(int(args[0]), int(args[1]))

    def remove(self, args: list) -> None:
        """
        This is a method called remove that takes a list of arguments args and
         returns nothing (None). The method removes an integer element from the
         instance variable data_list of the object that called the method.
         The integer element to be removed is determined by the first item in
         the args list, which is converted to an integer before removing it.
        :param args:
        :return:
        """
        self.data_list.remove(int(args[0]))

    def append(self, args: list) -> None:
        """
        This is a method definition in Python. It belongs to a class and it
        takes a list of integers as arguments. The append method adds
        the first integer in the argument list to another class attribute
        called data_list. The return type of this method is None, which means
        it doesn't return anything.
        :param args:
        :return:
        """
        self.data_list.append(int(args[0]))

    def print_f(self, *args) -> None:
        """
        This is a method named print_f which takes in a parameter self and
        returns None. It prints the attribute data_list of the object on which
        it is called. The code is written in Python.
        """
        print(self.data_list)

    def sort(self, *args) -> None:
        """
        This is a method called sort that belongs to a class.
        It takes in the self parameter and returns None.
        The method sorts a list of data (data_list) that is a member of
        the class instance.
        """
        self.data_list.sort()

    def pop(self, *args) -> None:
        """
        This is a method called pop defined in a Python class.
        It takes the instance of the class as its first parameter
        (self) and has a return type annotation of None.
        The method removes and returns the last item
        from a list stored in the instance variable data_list.
        :return:
        """
        self.data_list.pop()

    def reverse(self, *args) -> None:
        """
        This is a method called reverse defined in a Python class.
        It takes the instance of the class (self) as its first argument
        and has a return type annotation of None. The method simply calls
        the reverse() method on an attribute of the instance called data_list.
        This will reverse the order of elements in the list.
        :return:
        """
        self.data_list.reverse()

    def selector(self, selector: str, args: list) -> None:
        """
        This is a method called selector that takes in a string selector and a
        list args. It has a dictionary called selectors where the keys are
        strings representing the different operations that can be performed
        on a data structure, and the values are the corresponding methods to call.
        The method then retrieves the corresponding method based on the
        given selector from the selectors dictionary using indexing
        and calls it with the args list. The return value of the
        called method is ignored since the return type of this method is None.
        :param selector:
        :param args:
        :return:
        """
        selectors = {
            'insert': self.insert,
            'remove': self.remove,
            'append': self.append,
            'sort': self.sort,
            'pop': self.pop,
            'reverse': self.reverse,
            'print': self.print_f
        }
        selectors[selector](args)

    def get_list(self, input_: str) -> dict:
        """
        This is a method called get_list that accepts a string input as an
        argument, which is split into a list on whitespace characters.
        The method then returns a dictionary with two keys,
        'index' and 'split'. The value of 'index' is set to the first element
        of the split list, and the value of 'split' is set to a slice
        of the split list containing elements at indices 1 and 2
        (exclusive of index 3). The return type of this method is a dictionary.
        The code language used here is Python.
        :param input_:
        :return:
        """
        split = input_.split(' ')
        return {'index': split[0], 'split': split[1:3:]}

    def manipulate_list(self) -> None:
        """
        This is a method called manipulate_list that belongs to a class.
        It takes no arguments, but prompts the user for an integer value N.
        It then enters a loop and on each iteration extracts a dictionary
        of data from a list using the method self.get_list.
        The method self.selector is then called,
        passing in two values from the extracted dictionary.
        The return type of this method is None.

        :return:
        """
        N = int(input())
        for i in range(N):
            re = self.get_list(input())
            self.selector(re['index'], re['split'])


if __name__ == '__main__':
    list_manipulator = ListManipulator()
    list_manipulator.manipulate_list()
