"""
This module is for solving Ohm's Law by functions
to get Voltage (U), Current (I) and Resistance (R).
---------------------------------------------------
Ohm's Law:
U = I*R
I = U/R
R = U/I
"""


def calculate_voltage(current: float, resistance: float) -> float:
    """
    - Calculation of Voltage (U) in Volts
    - Current (I) input is in Amperes
    - Resistance (R) input is in Ohms
    U = I*R
    """
    if resistance < 0:
        raise ValueError("Resistance can't be negative")
    else:
        return  current * resistance


def calculate_current(voltage: float, resistance: float) -> float:
    """
    - Calculation of Current (I) in Amperes
    - Voltage (U) input is in Volts
    - Resistance (R) input is in Ohms
    I = U/R
    """
    if resistance <= 0:
        raise ValueError("Resistance cannot be 0")
    if voltage < 0:
        raise ValueError("Voltage cannot be negative")
    else:
        return voltage / resistance


def calculate_resistance(voltage: float, current: float) -> float:
    """
    - Calculation of Resistance (R) in Ohms
    - Voltage (U) input is in Volts
    - Current (I) input is in Amperes
    R = U/I
    """
    if current == 0:
        raise ValueError("Current cannot be 0")
    else:
        return voltage / current