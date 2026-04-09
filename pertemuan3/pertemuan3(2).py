import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

Informasi  = ctrl.Antecedent(np.arange(0, 101, 1), 'Kejelasan Informasi')
Persyaratan= ctrl.Antecedent(np.arange(0, 101, 1), 'Kejelasan Persyaratan')
Petugas    = ctrl.Antecedent(np.arange(0, 101, 1), 'Kemampuan Petugas')
Sarpras    = ctrl.Antecedent(np.arange(0, 101, 1), 'Ketersediaan Sarpras')


Kepuasan   = ctrl.Consequent(np.arange(0, 401, 1), 'Kepuasan Pelayanan')


for var in [Informasi, Persyaratan, Petugas, Sarpras]:
    var['Tidak Memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['Cukup Memuaskan'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['Memuaskan']       = fuzz.trapmf(var.universe, [75, 90, 100, 100])


Kepuasan['Tidak Memuaskan']  = fuzz.trapmf(Kepuasan.universe, [0, 0, 50, 75])
Kepuasan['Kurang Memuaskan'] = fuzz.trimf(Kepuasan.universe, [50, 75, 100])
Kepuasan['Cukup Memuaskan']  = fuzz.trapmf(Kepuasan.universe, [100, 150, 250, 275])
Kepuasan['Memuaskan']        = fuzz.trimf(Kepuasan.universe, [250, 275, 325])
Kepuasan['Sangat Memuaskan'] = fuzz.trapmf(Kepuasan.universe, [325, 350, 400, 400])


aturan1 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Tidak Memuaskan'] & Sarpras['Tidak Memuaskan'], Kepuasan['Tidak Memuaskan'])
aturan2 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Tidak Memuaskan'] & Sarpras['Cukup Memuaskan'], Kepuasan['Tidak Memuaskan'])
aturan3 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Tidak Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Tidak Memuaskan'])

aturan4 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Cukup Memuaskan'] & Sarpras['Tidak Memuaskan'], Kepuasan['Tidak Memuaskan'])
aturan5 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Cukup Memuaskan'] & Sarpras['Cukup Memuaskan'], Kepuasan['Tidak Memuaskan'])
aturan6 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Cukup Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Cukup Memuaskan'])

aturan7 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Memuaskan'] & Sarpras['Tidak Memuaskan'], Kepuasan['Tidak Memuaskan'])
aturan8 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Memuaskan'] & Sarpras['Cukup Memuaskan'], Kepuasan['Cukup Memuaskan'])
aturan9 = ctrl.Rule(Informasi['Tidak Memuaskan'] & Persyaratan['Tidak Memuaskan'] & Petugas['Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Cukup Memuaskan'])

aturan10 = ctrl.Rule(Informasi['Cukup Memuaskan'] & Persyaratan['Cukup Memuaskan'] & Petugas['Cukup Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Memuaskan'])
aturan11 = ctrl.Rule(Informasi['Cukup Memuaskan'] & Persyaratan['Cukup Memuaskan'] & Petugas['Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Memuaskan'])

aturan12 = ctrl.Rule(Informasi['Cukup Memuaskan'] & Persyaratan['Memuaskan'] & Petugas['Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Sangat Memuaskan'])
aturan13 = ctrl.Rule(Informasi['Memuaskan'] & Persyaratan['Memuaskan'] & Petugas['Memuaskan'] & Sarpras['Memuaskan'], Kepuasan['Sangat Memuaskan'])


engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9, aturan10, aturan11, aturan12, aturan13])
system = ctrl.ControlSystemSimulation(engine)


system.input['Kejelasan Informasi'] = 80
system.input['Kejelasan Persyaratan'] = 60
system.input['Kemampuan Petugas'] = 50
system.input['Ketersediaan Sarpras'] = 90

print("=== HASIL LOGIKA FUZZY PELAYANAN MASYARAKAT ===")
print("Input: Info=80, Syarat=60, Petugas=50, Sarpras=90\n")

try:
    system.compute()
    print(f"{system.output['Kepuasan Pelayanan']}")
    Kepuasan.view(sim=system)
    
except Exception as e:
    print("PROGRAM TIDAK DAPAT MENGHITUNG OUTPUT!")
    print("Alasan: Incomplete Rule Base (Basis Aturan Tidak Lengkap).")
    print("Dari 13 aturan yang tersedia di soal, tidak ada satu pun aturan yang")
    print("mengatur kondisi ketika: Info=Cukup Memuaskan/Memuaskan, Syarat=Tidak Memuaskan, dan Petugas=Tidak Memuaskan.")


input("\nTekan Enter untuk keluar...")