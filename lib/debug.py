#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb


payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)


hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)

hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)

hr.save()
print(hr)
print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)
ipdb.set_trace()
