import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

Barang_terjual = ctrl.Antecedent(np.arange(0, 101), 'Barang Terjual')
Permintaan = ctrl.Antecedent(np.arange(0, 301), 'Permintaan')
Harga_per_item = ctrl.Antecedent(np.arange(1, 100001), 'Harga per Item')
Profit = ctrl.Antecedent(np.arange(0, 4000001), 'Profit')
Stok_Makanan = ctrl.Consequent(np.arange(0, 1001), 'Stok Makanan')

Barang_terjual['rendah'] = fuzz.trimf(Barang_terjual.universe, [0, 0, 40])
Barang_terjual['sedang'] = fuzz.trimf(Barang_terjual.universe, [30, 50, 70])
Barang_terjual['tinggi'] = fuzz.trimf(Barang_terjual.universe, [60, 100, 100])

Permintaan['rendah'] = fuzz.trimf(Permintaan.universe, [0, 0, 100])
Permintaan['sedang'] = fuzz.trimf(Permintaan.universe, [50, 150, 250])
Permintaan['tinggi'] = fuzz.trimf(Permintaan.universe, [200, 300, 300])

Harga_per_item['murah'] = fuzz.trimf(Harga_per_item.universe, [0, 0, 40000])
Harga_per_item['sedang'] = fuzz.trimf(Harga_per_item.universe, [30000, 50000, 80000])
Harga_per_item['mahal'] = fuzz.trimf(Harga_per_item.universe, [60000, 100000, 100000])

Profit['rendah'] = fuzz.trimf(Profit.universe, [0, 0, 1000000])
Profit['sedang'] = fuzz.trimf(Profit.universe, [1000000, 2000000, 2500000])
Profit['tinggi'] = fuzz.trimf(Profit.universe, [1500000, 2500000, 4000000])


Stok_Makanan['sedang'] = fuzz.trimf(Stok_Makanan.universe, [100, 500, 900])
Stok_Makanan['banyak'] = fuzz.trimf(Stok_Makanan.universe, [600, 1000, 1000])


aturan1 = ctrl.Rule(Barang_terjual['tinggi'] & Permintaan['tinggi'] & Harga_per_item['murah'] & Profit['tinggi'], Stok_Makanan['banyak'])
aturan2 = ctrl.Rule(Barang_terjual['tinggi'] & Permintaan['tinggi'] & Harga_per_item['murah'] & Profit['sedang'], Stok_Makanan['sedang'])
aturan3 = ctrl.Rule(Barang_terjual['tinggi'] & Permintaan['sedang'] & Harga_per_item['murah'] & Profit['sedang'], Stok_Makanan['sedang'])
aturan4 = ctrl.Rule(Barang_terjual['sedang'] & Permintaan['tinggi'] & Harga_per_item['murah'] & Profit['sedang'], Stok_Makanan['sedang'])
aturan5 = ctrl.Rule(Barang_terjual['sedang'] & Permintaan['tinggi'] & Harga_per_item['murah'] & Profit['tinggi'], Stok_Makanan['banyak'])
aturan6 = ctrl.Rule(Barang_terjual['rendah'] & Permintaan['rendah'] & Harga_per_item['sedang'] & Profit['sedang'], Stok_Makanan['sedang'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6])
system = ctrl.ControlSystemSimulation(engine)

system.input['Barang Terjual'] = 80
system.input['Permintaan'] = 255
system.input['Harga per Item'] = 25000
system.input['Profit'] = 3500000



system.compute()
print(system.output['Stok Makanan'])

Stok_Makanan.view(sim=system)
input("Tekan Enter untuk keluar...")
                                 