for co,ca,po in zip (['Russia','USA','UK','Germany','France','India'],['Moscow','Washington','London','Berlin','Paris','Delhi'],[i.replace('_','') for i in ['145_934_462','331_002_651','80_345_321','67_886_011','65_273_511','1_380_004_385']]):
    print(f'{ca} is the capital of {co} , population equal {po} people')
"""
def ignore_command(command):
    for word in ['alias','configuration','ip','sql','select','updata','exec','del','truncate']:
        print(True if word in command  else False)
ignore_command=(lambda command : for word in ['alias','configuration','ip','sql','select','updata','exec','del','truncate']: True if word in command  else False)
"""