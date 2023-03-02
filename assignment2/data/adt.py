from typing import TypeVar
Item = TypeVar('Item')  

class Bag:
  # define the constructor with 2 private attributes
  def __init__(self) -> None:
    self.__N     = 0     # number of items - private 
    self.__first = None  # point to first item in the bag - private 

  # add an item to bag
  def add(self, item: Item) -> None:
    oldFirst = self.__first 
    self.__first = self.Node()   # create a new node
    self.__first.item = item     # add content to that node
    self.__first.next = oldFirst # create a reference to next node
    self.__N += 1                # increment the size of bag by 1

  # nested class Node inside class Bag
  class Node:
    def __init__(self) -> None:
      self.item = None
      self.next = None

  # method to check if bag is empty
  def isEmpty(self) -> bool:
    return self.__N == 0

  # method to return the size of bag
  def __len__(self) -> int:
    return self.__N

  # print the content of the bag
  def __str__(self) -> str:
    output_str = "["
    self.__iter_node = self.__first
    while True:
      if self.__iter_node is not None:
        output_str += f'{self.__iter_node.item}'
        self.__iter_node = self.__iter_node.next
      if self.__iter_node is not None:
        output_str += ','
      else: 
        break
    output_str += ']'
    return output_str

  # The 2 methods below make the objects iterable
  def __iter__(self):
    self.__iter_node = self.__first
    return self

  def __next__(self):
    if self.__iter_node is not None:
      x = self.__iter_node.item
      self.__iter_node = self.__iter_node.next
      return x
    else:
      raise StopIteration

class Queue:
  # define the constructor with 3 private attributes
  def __init__(self) -> None:
    self.__N     = 0     # number of items - private 
    self.__first = None  # point to least recently added node - private 
    self.__last  = None  # point to most recently added node - private 

  # nested class Node inside class Queue
  class Node:
    def __init__(self) -> None:
      self.item = None
      self.next = None

  # add an item to queue
  def enqueue(self, item: Item) -> None:
    oldLast = self.__last
    self.__last = self.Node()
    self.__last.item = item
    self.__last.next = None
    if (self.isEmpty()): self.__first = self.__last 
    else               : oldLast.next = self.__last 
    self.__N += 1                # increment the size of queue by 1

  # remove an item from the queue
  def dequeue(self) -> Item:
    item = self.__first.item
    self.__first = self.__first.next
    if self.isEmpty(): self.__last = None
    self.__N -= 1                # decrement the size of queue by 1
    return item

  # method to check if queue is empty
  def isEmpty(self) -> bool:
    return self.__N == 0

  # method to return the size of queue
  def __len__(self) -> int:
    return self.__N

  # print the content of the queue
  def __str__(self) -> str:
    output_str = "["
    self.__iter_node = self.__first
    while True:
      if self.__iter_node is not None:
        output_str += f'{self.__iter_node.item}'
        self.__iter_node = self.__iter_node.next
      if self.__iter_node is not None:
        output_str += ','
      else: 
        break
    output_str += ']'
    return output_str

  # The 2 methods below make the objects iterable
  def __iter__(self):
    self.__iter_node = self.__first
    return self

  def __next__(self):
    if self.__iter_node is not None:
      x = self.__iter_node.item
      self.__iter_node = self.__iter_node.next
      return x
    else:
      raise StopIteration

class Stack:
  # define the constructor with 2 private attributes
  def __init__(self) -> None:
    self.__N     = 0     # number of items - private 
    self.__first = None  # point to top of stack (most recently addded) - private 

  # nested class Node inside class Stack
  class Node:
    def __init__(self) -> None:
      self.item = None
      self.next = None

  # add an item to stack
  def push(self, item: Item) -> None:
    oldFirst = self.__first
    self.__first = self.Node()
    self.__first.item = item
    self.__first.next = oldFirst
    self.__N += 1                # increment the size of stack by 1

  # remove an item from the stack
  def pop(self) -> Item:
    item = self.__first.item
    self.__first = self.__first.next
    self.__N -= 1                # decrement the size of stack by 1
    return item

  # method to check if stack is empty
  def isEmpty(self) -> bool:
    return self.__N == 0

  # method to return the size of stack
  def __len__(self) -> int:
    return self.__N

  # print the content of the stack
  def __str__(self) -> str:
    output_str = "["
    self.__iter_node = self.__first
    while True:
      if self.__iter_node is not None:
        output_str += f'{self.__iter_node.item}'
        self.__iter_node = self.__iter_node.next
      if self.__iter_node is not None:
        output_str += ','
      else: 
        break
    output_str += ']'
    return output_str

  # The 2 methods below make the objects iterable
  def __iter__(self):
    self.__iter_node = self.__first
    return self

  def __next__(self):
    if self.__iter_node is not None:
      x = self.__iter_node.item
      self.__iter_node = self.__iter_node.next
      return x
    else:
      raise StopIteration