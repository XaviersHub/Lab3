import Lab2.bmi as bmi


def test_bmi_normal_weight():
    BMI = bmi.calculate_bmi(1.73,57)
    num = 0
    assert(BMI == num)
def test_bmi_under_weight():
    BMI = bmi.calculate_bmi(1.70,40)
    num = -1
    assert(BMI == num)
def test_bmi_over_weight():
    BMI = bmi.calculate_bmi(1.40,90)
    num = 1
    assert(BMI == num)


