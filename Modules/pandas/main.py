import pandas as pd

mortar_probes = pd.Series([8.9, 8.8, 6.1, 6.4], index = [122, 123, 124, 125])

mortar_probes.name = 'brick particles'
mortar_probes.index.name = "probes"


mb = pd.DataFrame({'residue':[41.3, 35.9, 39.5, 33.3],
                   'brick particles': [8.9, 8.8, 6.1, 6.4],
                   'sand': [25.8, 20.1, 28.7, 24.1],
                   'clay':[6.6, 7, 4.7, 2.7]},index= [122, 123, 124, 125])
mb.index.name = 'Probe Number'

print(mb["brick particles"])

print(mb["sand"].mean())

res = mb[mb.residue > 36][["brick particles",'sand']]
print(res)

