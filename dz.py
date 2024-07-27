"""
countries=['Russia','USA','UK','Germany','France','India']
capitals=['Moscow','Washington','London','Berlin','Paris','Delhi']
population=['145_934_462','331_002_651','80_345_321','67_886_011','65_273_511','1_380_004_385']
popul_list=[]
for i in population:
    popul_list.append(i.replace('_',''))
for co,ca,po in zip (countries,capitals,popul_list):
    print(f'{ca} is the capital of {co} , population equal {po} people')
"""
def ignore_command(command):
    ignore=['alias','configuration','ip','sql','select','updata','exec','del','truncate']
    for word in ignore:
        print(True if word in command  else False)

