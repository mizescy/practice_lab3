import practice_lab2.main as lab2

def test_find_min_max():
    input = [3.0, 5.0, 1.0]
    min_val, max_val = lab2.find_min_max(input)
    
    assert min_val == 1.0
    assert max_val == 5.0

def test_calc_average():
    input = [3,5,1]
    result = lab2.calc_average(input)

    assert result == 3

def test_calc_median_temperature():
    input = [3, 5, 1, 2, 4]
    result = lab2.calc_median_temperature(input)

    assert result == 3