from collections import namedtuple,deque
from typing import DefaultDict, OrderedDict


def task1()->DefaultDict:
 obj1=DefaultDict(lambda:"Unknown")
 obj1['Alan']='Manchester'
 return obj1;

def task2(arg_od:OrderedDict):
 arg_od.popitem(last=True)
 arg_od.popitem(last=False)
 arg_od.move_to_end("Bob", last=True)
 arg_od.move_to_end("Dan",last=False)
 
def task3(name:str,club:str)->namedtuple:
 NT=namedtuple("Player",['name',"club"])
 return NT(name,club)

def task4(arg_deque:deque):
 arg_deque.pop();
 ele=arg_deque.popleft();
 arg_deque.append(ele)
 arg_deque.appendleft("Zack")