import gas_pump_core


def test_gas_types():
    inventory = [
        ['regular', 4501.0, 2.0],
        ['mid-grade', 4982.14, 2.24],
        ['premium', 4787.81, 3.2]
        ]
    assert gas_pump_core.gas_types(inventory) == ['regular', 'mid-grade', 'premium']

def test_convert_back():
    inventory = [
    ['regular', 4501.0, 2.0],
    ['mid-grade', 4982.14, 2.24],
    ['premium', 4787.81, 3.2]
    ]
    assert gas_pump_core.convert_back(inventory) == '\nregular, 4501.0, 2.0\nmid-grade, 4982.14, 2.24\npremium, 4787.81, 3.2'

def test_price_of():
    inventory = [
    ['regular', 4501.0, 2.0],
    ['mid-grade', 4982.14, 2.24],
    ['premium', 4787.81, 3.2]
    ]
    # 1 is for the input choices. In this case it stands for 'regular'
    assert gas_pump_core.price_of(inventory, '1') == 2.0
def test_pay_after_fill():
    inventory = [
    ['regular', 4501.0, 2.0],
    ['mid-grade', 4982.14, 2.24],
    ['premium', 4787.81, 3.2]
    ]
    # 1 is for the input choices. In this case it stands for 'regular'
    assert gas_pump_core.pay_after_fill(inventory, '1', 20) == 40
def test_pre_pay():
    inventory = [
    ['regular', 4501.0, 2.0],
    ['mid-grade', 4982.14, 2.24],
    ['premium', 4787.81, 3.2]
    ]
     # 1 is for the input choices. In this case it stands for 'regular'
    assert gas_pump_core.pre_pay(inventory, '1', 20) == 10