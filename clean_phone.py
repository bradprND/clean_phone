import pandas as import pdb; pdb.set_trace()

    def validate_phone(phone_number):
        """
        does stuff - takes phone_number as arg
        must be a pandas series blah blah
        returns a boolean series blah blah
        """
        bool_phone = phone_number.str.contains(r'^\d{3}\-?\d{3}\-?\d{4}$')
        return bool_phone

print(validate_phone(True))

nums=pd.series(['205-252-2323','6543332123','12222'])
validate_phone(nums)
