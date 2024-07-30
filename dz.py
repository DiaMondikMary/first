for co,ca,po in zip (['Russia','USA','UK','Germany','France','India'],['Moscow','Washington','London','Berlin','Paris','Delhi'],[i.replace('_','') for i in ['145_934_462','331_002_651','80_345_321','67_886_011','65_273_511','1_380_004_385']]):
    print(f'{ca} is the capital of {co} , population equal {po} people')
