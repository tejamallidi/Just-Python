class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        # create a node and mark head as next of that item
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print('Linked list is empty.')
            return
        # iterate through linked list
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        # Check if linked list is empty, add it as first element
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            # iterate by incrementing
            itr = itr.next
        # once the iteration reaches end of ll
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # create new linked list from the given list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index.')

        # To remove first element set it's head to next element of head
        if index == 0:
            self.head = self.head.next

        # Iterate through ll till index - 1 and change the next of that element
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index.')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        if self.head is None:
            return

        # insert at first position in ll, so append to head
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                # Now insert data_to_insert after data_after node
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        # remove at first position in ll, so remove after head
        if self.head.data == data:
            self.head = self.head.next
            return

         # Remove first node that contains data
         # To acheive that check if next elements data == data, if so remove it.
        itr = self.head
        # count = 0
        while itr.next:
            if itr.next.data == data:
                # This is valid but try writing another approach
                # self.remove_at(count)
                itr.next = itr.next.next
                break
            itr = itr.next
            # count += 1


if __name__ == '__main__':
    ll = Linkedlist()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(6)
    # ll.insert_at_begining(7)
    # ll.insert_at_end(8)
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    # ll.insert_at(2, 'apple')
    # ll.remove_at(2)
    # ll.print()
    # print(ll.get_length())
