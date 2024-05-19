#   First take input (patinet data) then create a list of pill objects positions.

from Project.Extra.patientClass import Patient
from createList import ListCreator


listA = ["A", "B"]
listB = ["B", "B"]

pat1 = Patient("Per", listA, listA, listB, listA)
fullList = pat1.fullList
list2 = ListCreator(fullList)

