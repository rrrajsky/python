
# Rozšiřte modul z úlohy 7.1. o funkce, třídy nebo konstanty na výpočet Coulombova zákona. Následně napište skript, který importuje jen část modulu nezbytnou pro následující výpočet:

# Dva prvky s nabojem Q1 = 50 nC, druhá Q2 = 70 nC, jsou umístěny vedle sebe ve vzdálenosti 1cm. Jakými velkými silami na sebe prvky působí pokud je mezi nimy vzduch s εr = 1

from physics_calculator import calculate_coulomb

print(calculate_coulomb(50,70,1,1))
