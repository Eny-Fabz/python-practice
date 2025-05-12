# So this is the practice for the linked list, but I'm trying to work with a list where the data type for each node is a String.


class Item:
    def __init__(self, value: str):
        self.value: str = value
        self.next: Item | None = None

class TheList:
    def __init__(self):
        self.head: Item | None = None

    def insert_at_end(self, value: str) -> None:
        #So this method will add another node of data type string to the end of the list
        new_node = Item(value)

        if self.head is None:
            self.head = new_node
            return
        cursor = self.head

        while cursor.next:
            cursor = cursor.next
        cursor.next = new_node

    def insert_at_start(self, value: str) -> None:
        #This one will add a node to the beginning of the list. Of course a string data type again
        new_node = Item(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, idx: int, value: str) -> None:
        #This basically just inserts a node at my preferred point
        if idx < 0:
            raise IndexError("You cannot input a negative index.")
        if idx == 0:
            return self.insert_at_start(value)
        new_node = Item(value)
        cursor = self.head
        for _ in range(idx - 1):
            if cursor is None:
                raise IndexError("the index is out of range.")
            cursor = cursor.next
        if cursor is None:
            raise IndexError("the index is out of range.")
        new_node.next = cursor.next
        cursor.next = new_node

    def delete_at_index(self, idx: int) -> None:
        #This deletes a node at the given index/point
        if self.head is None or idx < 0:
            raise IndexError("The index is invalid or the list is empty.")
        if idx == 0:
            self.head = self.head.next
            return
        prev = self.head
        for _ in range(idx - 1):
            if prev.next is None:
                raise IndexError("the index is out of range")
            prev = prev.next
        if prev.next is None:
            raise IndexError("the index is out of range")
        prev.next = prev.next.next

    def search(self, goal: str) -> int:
        #This one will return the index of the string `value`, or -1 if the value is not found.
        idx = 0
        cursor = self.head
        while cursor:
            if cursor.value == goal:
                return idx
            cursor = cursor.next
            idx += 1
        return -1

    def display(self) -> None:
        #Lastly, this method is just to print all my values in the list as strings
        cursor = self.head
        elems: list[str] = []
        while cursor:
            elems.append(cursor.value)
            cursor = cursor.next
        print(" -> ".join(elems))


if __name__ == "__main__":
    ll = TheList()
    ll.insert_at_end("Kakashi Hatake")
    ll.insert_at_start("Minato Namikaze")
    ll.insert_at_index(1, "Dattebayo")
    ll.display()
    # So, my expected output should look like: Minato Namikaze -> Dattebayo -> Kakashi Hatake

    ll.delete_at_index(2)
    ll.display()
    # Expected output: Minato Namikaze -> Dattebayo

    print("Index of 'Minato Namikaze':", ll.search("Minato Namikaze"))   # This should give me a 0. Its showing me the index of the value

