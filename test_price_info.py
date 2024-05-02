import price_info

def test_cost_shopping():
    testunit = 46.75
    assert(print("total cost = ", testunit)==price_info.total_cost_shopping())
def test_cost_of_fruits():
    testunit = 2.40
    assert(price_info.cost_of_fruits('apple',2) == print("cost of 2 apple =",testunit))

