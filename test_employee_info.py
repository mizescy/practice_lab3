import employee_info

print("Test Employee info")

def test_get_by_age_range():
    result = employee_info.get_employees_by_age_range(23, 35)
    expected = ["Jane", "John", "Mike"]

    assert len(result) == 3
    assert all(employee["name"] in expected for employee in result)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected = (361000) /6
    assert result == expected

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Sales")
    expected = ["John", "Peter"]

    assert len(result) == 2
    assert all(employee["name"] in expected for employee in result)