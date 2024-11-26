def calculate_current(voltage, resistance):
    """
    Calculate electric current using Ohm's law.

    Parameters:
        voltage (float): The voltage in volts.
        resistance (float): The resistance in ohms. Must be non-zero.

    Returns:
        float: The current in amperes.

    Raises:
        Exception: If resistance is zero, as this would result in division by zero.
    """
    if resistance == 0:
        raise ValueError("Resistance must be non-zero.")
    return voltage / resistance


def calculate_voltage(current, resistance):
    """
    Calculate electric voltage using Ohm's law.

    Parameters:
        current (float): The current in amperes.
        resistance (float): The resistance in ohms.

    Returns:
        float: The voltage in volts.

    Raises:
        Exception: If resistance is zero, as this would result in incorrect calculations.
    """
    if resistance == 0:
        raise ValueError("Resistance must be non-zero.")
    return current * resistance


def calculate_resistance(voltage, current):
    """
    Calculate electrical resistance using Ohm's law.

    Parameters:
        current (float): The current in amperes.
        voltage (float): The voltage in volts.

    Returns:
        float: The resistance in ohms.
    
    Raises:
        Exception: If resistance is zero, as this would result in incorrect calculations.
    """
    if current == 0:
        raise ValueError("Current must be non-zero.")
    return voltage / current


def calculate_coulomb(q1, q2, r, epsilon_r):
    """
    Calculate the electrostatic force between two charges.

    Parameters:
        q1 (float): The first charge in nanocoulombs (nC).
        q2 (float): The second charge in nanocoulombs (nC).
        r (float): The distance between charges in centimeters (cm).
        epsilon_r (float): The relative permittivity of the medium.

    Returns:
        float: The electrostatic force in newtons (N).

    Notes:
        The function uses the vacuum permittivity constant (epsilon_0 = 8.85e-12 F/m).
    """
    epsilon_0 = 8.85e-12  # Permittivity of free space (F/m)
    epsilon = epsilon_0 * epsilon_r
    force = (1 / (4 * 3.14 * epsilon)) * abs(q1 * q2) / (r ** 2)
    
    return force
