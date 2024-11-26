
import physics_calculator
import physical_laws as alternative

print("U=10mV, R=1KiloOhm, kolik je proud?")
print(physics_calculator.calculate_current(0.01,1000))
print()
print("Namerite-li proud 2mA a napeti 3V, jaka musi byt hodnota R?")
print(physics_calculator.calculate_resistance(3,0.002))
print()
print("Je-li R=2Ohmy a proteka-li prodou 20miliAmper, jake je napeti?")
print(physics_calculator.calculate_voltage(0.02,2))

print()
print()
print()

print("U=10mV, R=1KiloOhm, kolik je proud?")
print(alternative.calculate_current(0.01,1000))
print()
print("Namerite-li proud 2mA a napeti 3V, jaka musi byt hodnota R?")
print(alternative.calculate_resistance(3,0.002))
print()
print("Je-li R=2Ohmy a proteka-li prodou 20miliAmper, jake je napeti?")
print(alternative.calculate_voltage(0.02,2))